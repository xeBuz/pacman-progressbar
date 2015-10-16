#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='pacmanprogressbar',
    version='1.0',
    py_modules=['pacmanprogressbar'],

    author='Jesús Roldán',
    author_email='jesus.roldan@gmail.com',    
    url='https://github.com/xeBuz/pacman-progressbar',
    license='MIT',

    description='ProgreessBar for Python, based on Arch progressbar, with "ILoveCandy" option enabled',
    long_description=open('README.md').read(),

    classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            "Programming Language :: Python",
            "Topic :: Utilities",
        ],
)   