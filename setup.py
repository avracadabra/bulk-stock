#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script for bulk-stock"""
import os

from setuptools import find_packages
from setuptools import setup

version = "0.1.0"
here = os.path.abspath(os.path.dirname(__file__))

with open(
    os.path.join(here, "README.rst"), "r", encoding="utf-8"
) as readme_file:
    readme = readme_file.read()

with open(
    os.path.join(here, "CHANGELOG.rst"), "r", encoding="utf-8"
) as changelog_file:
    changelog = changelog_file.read()

requirements = [
    "sqlalchemy",
    "anyblok",
    "psycopg2-binary",
    "anyblok_pyramid",
    "anyblok_pyramid_beaker",
    "gunicorn",
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name="bulk_stock",
    version=version,
    description="An application to manage bulk stock in stores",
    long_description=readme + "\n\n" + changelog,
    author="Pierre Verkest",
    author_email="pierreverkest84@gmail.com",
    url="https://github.com/petrus-v/bulk-stock",
    packages=find_packages(),
    entry_points={"bloks": ["graphql=bulk_stock.graphql:Graphql"]},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords="bulk-stock",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    test_suite="tests",
    tests_require=test_requirements,
)
