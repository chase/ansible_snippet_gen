ansible-vim-snippet-generator
=============================

Generates some useful Ansible module snippets for SnipMate/UltiSnips.

## Installation
If your system default is Python 2:
`./setup.py install`

If your system default is Python 3 and you have Python 2.7 installed:
`python2 setup.py install`

## Usage
```
usage: ansible_snippet_gen [-h] [-v] [-f {U,S,B,u,s,b}] [--verbose] [-M MODULE_PATH]

Generate Ansible module snippets for Vim SnipMate/UltiSnips

UltiSnips snippets are written to 'UltiSnips/ansible.snippets'
SnipMate snippets are written to 'snippets/ansible.snippets'

Defaults to generating both snippet formats.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -f {U,S,B,u,s,b}      output choices: (U)ltiSnips, (S)nipMate, or (B)oth
  --verbose             show warnings
  -M MODULE_PATH, --module-path MODULE_PATH
                        add a Ansible modules directory
```
