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

from gocept.xmlrpcskin.interfaces import IXMLRPCSkinType
import zope.component.interfaces
import zope.location.interfaces
import zope.publisher.skinnable
import zope.traversing.namespace


class xmlrpc_skin(zope.traversing.namespace.view):
    # copy&paste of zope.traversing.namespace.skin to use a different skin-type
    # interface

    def traverse(self, name, ignored):
        self.request.shiftNameToApplication()
        try:
            skin = zope.component.getUtility(IXMLRPCSkinType, name)
        except zope.component.interfaces.ComponentLookupError:
            raise zope.location.interfaces.LocationError("++skin++%s" % name)
        zope.publisher.skinnable.applySkin(self.request, skin)
        return self.context
