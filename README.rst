=================
gocept.xmlrpcskin
=================

This package is an extension to the Zope Publisher that provides a ZCML
directive for XML-RPC views that supports a ``layer`` parameter.

It collects the changes that briefly were contained in 3.5.0alpha releases (but
subsequently have been removed) of the following packages

- zope.app.publisher (removed in r82484)
- zope.traversing (removed in r82482)
- zope.publisher (removed in r82493)


Usage
=====

The ``gocept:xmlrpcview`` directive is like the ``xmlrpc:view`` directive of
``zope.app.publisher``, but with an additional parameter ``layer``.

Here's an abbriged example (also available as
``gocept.xmlrpcskin.tests.fixture``)::

    <include package="zope.component" file="meta.zcml" />

    <include package="gocept.xmlrpcskin" file="meta.zcml" />
    <include package="gocept.xmlrpcskin" />

    <interface
      interface=".interfaces.IFooLayer"
      type="gocept.xmlrpcskin.interfaces.IXMLRPCSkinType"
      name="foo"
      />

    <gocept:xmlrpcview
      for="*"
      class=".view.Example"
      permission="zope.Public"
      methods="
      all_layers
      "
      />

    <gocept:xmlrpcview
      for="*"
      class=".view.Example"
      layer=".interfaces.IFooLayer"
      permission="zope.Public"
      methods="
      foo_layer
      "
      />


    class IFooLayer(zope.publisher.interfaces.xmlrpc.IXMLRPCRequest):
        pass

    class Example(zope.app.publisher.xmlrpc.XMLRPCView):

        def all_layers(self):
            return dict(returncode=1)

        def foo_layer(self):
            return dict(returncode=2)


The method ``all_layers`` will then be available on all layers, while
``foo_layer`` only is available on ``/++skin++foo``.
