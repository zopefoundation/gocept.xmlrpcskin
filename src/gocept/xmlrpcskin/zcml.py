#############################################################################
#
# Copyright (c) 2011 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from zope.app.publisher.xmlrpc import MethodPublisher
from zope.component.interface import provideInterface
from zope.component.zcml import handler
from zope.configuration.exceptions import ConfigurationError
from zope.interface import Interface
from zope.publisher.interfaces.xmlrpc import IXMLRPCRequest
from zope.security.checker import CheckerPublic, Checker
from zope.security.checker import getCheckerForInstancesOf
import zope.app.publisher.xmlrpc.metadirectives
import zope.configuration.fields


class IXMLRPCViewDirective(
    zope.app.publisher.xmlrpc.metadirectives.IViewDirective):

    layer = zope.configuration.fields.GlobalInterface(
        title=u"The layer the view is declared for",
        description=u"The default layer for which the default view is "
                    u"applicable. By default it is applied to all layers.",
        required=False
        )


def xmlrpc_view(_context, for_=None, interface=None, methods=None,
                class_=None, permission=None, name=None, layer=IXMLRPCRequest):
    # copy&paste from zope.app.publisher.xmlrpc.metaconfigure.view
    # to make layer a parameter instead of hardcoding it to IXMLRPCRequest

    interface = interface or []
    methods = methods or []

    # If there were special permission settings provided, then use them
    if permission == 'zope.Public':
        permission = CheckerPublic

    require = {}
    for attr_name in methods:
        require[attr_name] = permission

    if interface:
        for iface in interface:
            for field_name in iface:
                require[field_name] = permission
            _context.action(
                discriminator=None,
                callable=provideInterface,
                args=('', for_)
                )

    # Make sure that the class inherits MethodPublisher, so that the views
    # have a location
    if class_ is None:
        class_ = original_class = MethodPublisher
    else:
        original_class = class_
        class_ = type(class_.__name__, (class_, MethodPublisher), {})

    if name:
        # Register a single view

        if permission:
            checker = Checker(require)

            def proxyView(context, request, class_=class_, checker=checker):
                view = class_(context, request)
                # We need this in case the resource gets unwrapped and
                # needs to be rewrapped
                view.__Security_checker__ = checker
                return view

            class_ = proxyView
            class_.factory = original_class
        else:
            # No permission was defined, so we defer to the checker
            # of the original class
            def proxyView(context, request, class_=class_):
                view = class_(context, request)
                view.__Security_checker__ = getCheckerForInstancesOf(
                    original_class)
                return view
            class_ = proxyView
            class_.factory = original_class

        # Register the new view.
        _context.action(
            discriminator=('view', for_, name, layer),
            callable=handler,
            args=('registerAdapter',
                  class_, (for_, layer), Interface, name,
                  _context.info)
            )
    else:
        if permission:
            checker = Checker({'__call__': permission})
        else:
            raise ConfigurationError(
              "XML/RPC view has neither a name nor a permission. "
              "You have to specify at least one of the two.")

        for name in require:
            # create a new callable class with a security checker;
            cdict = {'__Security_checker__': checker,
                     '__call__': getattr(class_, name)}
            new_class = type(class_.__name__, (class_,), cdict)
            _context.action(
                discriminator=('view', for_, name, layer),
                callable=handler,
                args=('registerAdapter',
                      new_class, (for_, layer), Interface, name,
                      _context.info)
                )

    # Register the used interfaces with the site manager
    if for_ is not None:
        _context.action(
            discriminator=None,
            callable=provideInterface,
            args=('', for_)
            )
