#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pypaytabs",
    version="1.0.1",
    description="PyPaytabs is a Python library for Paytabs Payment Gateway.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/itiblog/pypaytabs",
    author='Belal Salah, Mohamed Hammad',
    author_email='belalsalah140@gmail.com, mmhy2003@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["pypaytabs"],
)