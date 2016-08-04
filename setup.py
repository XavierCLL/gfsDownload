#!/usr/bin/env python

# eraInterim Util
#
#
# Author: yoann Moreau, Xavier Corredor
# Contributer: benjamin tadry
#
# License: CC0 1.0 Universal

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(name="gfsdownload",
      version='0.0.3',
      description="A utility to download ERA INTERIM meteo data ",
      long_description=readme(),
      author="Yoann M, Xavier Corredor",
      author_email="yoann.moreau@gmail.com, xavier.corredor.llano@gmail.com",
      scripts=["gfsdownload/utils.py", "gfsdownload/eraInterimDownload.py"],
      url="https://github.com/XavierCLL/gfsDownload",
      # packages=["gfsdownload"],
      include_package_data=True,
      license="CCO",
      platforms="Posix; ",
      install_requires=[
          "GDAL",
          "OGR",
          "ecmwfapi"
      ],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Console",
          "Topic :: Scientific/Engineering :: GIS",
          "Programming Language :: Python",
      ]
      )
