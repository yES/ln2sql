from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ln2sql

ln2sql_classifiers = [
    "Programming Language :: Python :: 2",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

with open("README.md", "r") as fp:
    ln2sql_long_description = fp.read()

setup(name="ln2sql",
      version="0.1.0",
      author="Ferrero Jeremy",
      author_email="jeremy.ferrero@compilatio.net",
      url="http://pypi.python.org/pypi/ln2sql/",
      py_modules=["ln2sql"],
      description="ln2sql is a NLP tool to query a database in natural language",
      long_description=ln2sql_long_description,
      license="MIT",
      classifiers=ln2sql_classifiers
      )
