#!/usr/bin/python3 -W default
import warnings; warnings.simplefilter('default')

import distutils.sysconfig
import os 
import sys

try:
  from setuptools import setup, Extension
except ImportError:
  from distutils.core import setup, Extension

long_description = """\
Embeds the Python interpreter into PAM \
so PAM modules can be written in Python"""

classifiers = [
  "Development Status :: 4 - Beta",
  "Intended Audience :: Developers",
  "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
  "Natural Language :: English",
  "Operating System :: Unix",
  "Programming Language :: C",
  "Programming Language :: Python",
  "Topic :: Software Development :: Libraries :: Python Modules",
  "Topic :: System :: Systems Administration :: Authentication/Directory"]

if "Py_DEBUG" not in os.environ:
  Py_DEBUG = []
else:
  Py_DEBUG = [('Py_DEBUG',1)]

libpython_so = distutils.sysconfig.get_config_var('INSTSONAME')
python_ldversion = distutils.sysconfig.get_config_var('LDVERSION')
ext_modules = [
    Extension(
      "pam_python3",
      sources=["pam_python.c"],
      include_dirs = [],
      library_dirs=[],
      define_macros=[('LIBPYTHON_SO','"'+libpython_so+'"')] + Py_DEBUG,
      libraries=["pam", "python"+python_ldversion],
    ), ]

setup(
  name="pam_python",
  version="1.0.7",
  description="Enabled PAM Modules to be written in Python",
  keywords="pam,embed,authentication,security",
  platforms="Unix",
  long_description=long_description,
  author="Russell Stuart",
  author_email="russell-pampython@stuart.id.au",
  url="http://pam-python.sourceforge.net/",
  license="AGPL-3.0",
  classifiers=classifiers,
  ext_modules=ext_modules,
)
