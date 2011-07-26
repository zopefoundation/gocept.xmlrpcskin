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

import gocept.xmlrpcskin.testing
import gocept.xmlrpcskin.tests.fixture
import zope.configuration.xmlconfig
import zope.testbrowser.testing


class SkinTest(gocept.xmlrpcskin.testing.TestCase):

    def test_view_is_registered_only_for_layer(self):
        zope.configuration.xmlconfig.file(
            'configure.zcml', gocept.xmlrpcskin.tests.fixture)

        b = zope.testbrowser.testing.Browser()
        b.handleErrors = False
        b.open('http://localhost/index.html')
        self.assertEqual('Hello, world!', b.contents)
