#from distutils.core import setup
from setuptools import setup, find_packages
setup(
    name='PacmanProgressbar',
    version='0.2',
    py_modules=['PacmanProgressbar'],

    author='Jesús F. Roldán',
    author_email='jesus.roldan@gmail.com',    
    url='https://github.com/xeBuz/pacman-progressbar',
    license='LICENSE.txt',
    description='Progressbar based on Arch\'s Pacman progressbar',
    long_description=open('README.md').read(),
    classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3",
            "Topic :: Utilities",
        ],
)   
