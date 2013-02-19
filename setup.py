#!/usr/bin/env python
# http://docs.python.org/distutils/setupscript.html

import sys
from setuptools import setup

install_requires = []
extra = {}
version = '0.2.0'


setup(
    name='Profiler',
    version=version,
    description='Easy Profiling',
    author='Jay Marcyes',
    author_email='jay@marcyes.com',
    url='http://github.com/Jaymon/profiler',
    packages=['profiler'],
    license="MIT",
    install_requires=install_requires,
    zip_safe=True,
    classifiers=[
        'Development Status :: {}'.format(version),
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Topic :: Debug',
        ],
    test_suite = "profiler.profilertest",
    **extra
)
