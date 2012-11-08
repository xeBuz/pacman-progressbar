#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
setup(
    name='pacmanprogressbar',
    version='0.3.2',
    py_modules=['pacmanprogressbar'],

    author='Jesús F. Roldán',
    author_email='jesus.roldan@gmail.com',    
    url='https://github.com/xeBuz/pacman-progressbar',
    license='LICENSE.txt',
    description='ProgreessBar for Python, based on Arch progressbar, with "ILoveCandy" option enabled',
    long_description=open('README.md').read(),
    classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python",
            "Topic :: Utilities",
        ],
)   