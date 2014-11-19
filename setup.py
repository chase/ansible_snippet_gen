#!/usr/bin/env python

import os
import sys
from glob import glob

sys.path.insert(0, os.path.abspath('lib'))
from ansible_snippet_gen import __version__, __author__
try:
    from setuptools import setup, find_packages
except ImportError:
    print("Install snippet_gen using your package manager (python-setuptools) or via pip (pip install setuptools).")
    sys.exit(1)

setup(name='ansible_snippet_gen',
        version=__version__,
        description="Generates some useful Ansible module snippets for SnipMate/UltiSnips",
        author=__author__,
        author_email="chase@colman.io",
        url="https://github.com/chase/ansible-vim-snippet-generator",
        license='GPLv3',
        install_requires=['ansible'],
        package_dir={'': 'lib'},
        scripts=[ 'bin/ansible_snippet_gen' ],
        data_files=[])
