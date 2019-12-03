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

from setuptools import setup, find_packages


setup(
    name='gocept.xmlrpcskin',
    version='1.1',
    author='gocept',
    author_email='mail@gocept.com',
    url='https://github.com/zopefoundation/gocept.xmlrpcskin',
    description="""\
An extension to ``zope.publisher`` that provides a ZCML \
directive for XML-RPC views that supports a ``layer`` parameter.""",
    long_description=(
        open('README.rst').read()
        + '\n\n'
        + open('CHANGES.rst').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',
    keywords='zope2 zope3 xmlrpc zope.publisher',
    classifiers=[
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 5 - Production/Stable',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    namespace_packages=['gocept'],
    install_requires=[
        'setuptools',
        'zope.app.publisher',
        'zope.component[zcml]',
        'zope.configuration',
        'zope.interface',
        'zope.publisher>=3.6.0',
        'zope.security',
        'zope.traversing',
    ],
    extras_require=dict(test=[
        'unittest2',
        'zope.app.appsetup',
        'zope.app.publication',
        'zope.app.testing',
        'zope.browserpage',
        'zope.location',
        'zope.principalregistry',
        'zope.securitypolicy',
        'zope.testbrowser[zope-functional-testing]',
        'zope.testrunner',
    ]),
)
