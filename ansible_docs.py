#!/usr/bin/env python

# This library has been adapted from the 'ansible-doc' script from Ansible.
# You may find the original here:
# https://github.com/ansible/ansible/blob/afd8cca3452c0700e154a4f430aa73d97efe162a/bin/ansible-doc

# Original copyright {{{
# (c) 2012, Jan-Piet Mens <jpmens () gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
# }}}

import os
import sys
from ansible import utils
from ansible.utils import module_docs
import ansible.constants as C
from ansible.utils import version
import traceback

MODULEDIR = C.DEFAULT_MODULE_PATH

BLACKLIST_EXTS = ('.pyc', '.swp', '.bak', '~', '.rpm')
IGNORE_FILES = [ "COPYING", "CONTRIBUTING", "LICENSE", "README" ]

def find_modules(path):
    if not os.path.isdir(path):
        yield
    for module in os.listdir(path):
        if module.startswith('.'):
            continue
        elif os.path.isdir(module):
            for module in find_modules(module):
                yield module
        elif any(module.endswith(x) for x in BLACKLIST_EXTS):
            continue
        elif module.startswith('__'):
            continue
        elif module in IGNORE_FILES:
            continue
        elif module.startswith('_'):
            fullpath = '/'.join([path,module])
            if os.path.islink(fullpath): # avoids aliases
                continue

        module = os.path.splitext(module)[0] # removes the extension
        yield module

def get_modules(module_path=None):
    # Because Python doesn't like variables as defaults
    if module_path is None:
        module_path = MODULEDIR
    for i in module_path.split(os.pathsep):
        utils.plugins.module_finder.add_directory(i)
    paths = utils.plugins.module_finder._get_paths()
    for path in paths:
        for module in find_modules(path):
            yield module

def print_paths(finder):
    ''' Returns a string suitable for printing of the search path '''

    # Uses a list to get the order right
    ret = []
    for i in finder._get_paths():
        if i not in ret:
            ret.append(i)
    return os.pathsep.join(ret)

def get_docs(module_dir=None, warnings=False):
    for module in get_modules(module_dir):
        filename = utils.plugins.module_finder.find_plugin(module)
        if filename is None:
            if warnings:
                sys.stderr.write("WARNING: module %s not found in %s\n" % (module, print_paths(utils.plugins.module_finder)))
            continue

        try:
            doc, plainexamples = module_docs.get_docstring(filename)
        except:
            traceback.print_exc()
            sys.stderr.write("ERROR: module %s has a documentation error formatting or is missing documentation\n" % module)
            continue

        if doc is not None:
            yield module, doc
        else:
            # this typically means we couldn't even parse the docstring, not just that the YAML is busted,
            # probably a quoting issue.
            sys.stderr.write("ERROR: module %s missing documentation (or could not parse documentation)\n" % module)
