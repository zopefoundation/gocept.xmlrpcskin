=================
gocept.xmlrpcskin
=================

This package is an extension to ``zope.publisher`` that provides a ZCML
directive for XML-RPC views that supports a ``layer`` parameter.

It collects the changes that briefly were contained in 3.5.0alpha releases (but
subsequently have been removed) of the following packages

- zope.app.publisher (removed in r82484)
- zope.traversing (removed in r82482)
- zope.publisher (removed in r82493)


Usage
=====

Include the necessary ZCML::

    <include package="gocept.xmlrpcskin" file="meta.zcml" />
    <include package="gocept.xmlrpcskin" />

