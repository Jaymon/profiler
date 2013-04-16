#!/usr/bin/env python
# http://docs.python.org/distutils/setupscript.html

import sys
from setuptools import setup

version = '0.3'


setup(
    name='Profiler',
    version=version,
    description='Easy Profiling of blocks of code',
    author='Jay Marcyes',
    author_email='jay@marcyes.com',
    url='http://github.com/Jaymon/profiler',
    py_modules=['profiler'],
    license="MIT",
    zip_safe=True,
    classifiers=[
        'Development Status :: {}'.format(version),
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Topic :: Debug',
        ],
    test_suite = "profilertest",
)
