#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    setup.py
    ~~~~~~~~

"""


import os
import sys
from setuptools import setup, find_packages


dot = __import__('dot')
readme = os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.rst'))

try:
   long_description = open(readme).read()
except IOError as e:
   sys.stderr.write("File not found for long description: {}".format(readme))
   sys.exit(1)

install_requires = [
    'cliff',
    'vcs',
    'mock',
]


setup(
    name='dot',
    version=dot.version(),
    url='https://github.com/dustinrc/dot',
    author='Dustin Chapman',
    author_email='dustin.r.chapman@gmail.com',
    description=dot.__doc__,
    long_description=long_description,
    zip_safe=False,
    packages=find_packages(),
    scripts=[],
    test_suite='',
    install_requires=install_requires,
    provides=['dot'],
    platforms=['Any'],
    include_package_date=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
    entry_points={}
)
