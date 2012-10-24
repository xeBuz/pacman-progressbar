#from distutils.core import setup
from setuptools import setup, find_packages
setup(
    name='pacmanprogressbar',
    version='0.2.1',
    py_modules=['pacmanprogressbar'],

    author='Jesús F. Roldán',
    author_email='jesus.roldan@gmail.com',    
    url='https://github.com/xeBuz/pacman-progressbar',
    license='LICENSE.txt',
    description='Progressbar based on Arch\'s Pacman progressbar',
    long_description=open('README.md').read(),
    classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3",
            "Topic :: Utilities",
        ],
)   
