#!/usr/bin/env python3

# eraInterim Util
#
#
# Author: Yoann Moreau
# Contributes: Benjamin Tadry, Xavier Corredor Llano
#
# License: CC0 1.0 Universal

from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="gfsdownload",
    version='0.0.3',
    description="A utility to download GFS and ERA INTERIM meteo data",
    long_description=readme(),
    author="Yoann M, Xavier Corredor",
    author_email="yoann.moreau@gmail.com, xavier.corredor.llano@gmail.com",
    scripts=["gfsdownload/GFSDownload.py", "gfsdownload/eraInterimDownload.py"],
    url="https://github.com/XavierCLL/gfsDownload",
    packages=find_packages(),
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
