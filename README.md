Ansible Snippet Generator for Vim
=============================

Generates some useful Ansible module snippets for SnipMate/UltiSnips.

## Prerequisites
**Python 2.7** 
**Ansible >= 1.7** *Note: Make sure you install this through your package manager and not pip, as the standard module path may not be set.*

## Installation
If your system default is Python 2:
`[sudo] ./setup.py install`
*Note: If you don't know you don't know, try running *`python --version`

If your system default is Python 3 but you have Python 2.7 installed as well:
`[sudo] python2 setup.py install`

## Usage
```
usage: ansible_snippet_gen [-h] [-v] [-w NUM] [-f {U,S,B,u,s,b}] [--verbose]
                           [-M MODULE_PATH]

Generate Ansible module snippets for Vim SnipMate/UltiSnips

UltiSnips snippets are written to 'UltiSnips/ansible.snippets'
SnipMate snippets are written to 'snippets/ansible.snippets'

Defaults to generating SnipMate snippets.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -w NUM, --wrap NUM    wrap module options if over NUM options, default is 4
  -f {U,S,B,u,s,b}      output format: (U)ltiSnips, (S)nipMate, or (B)oth
  --verbose             show warnings
  -M MODULE_PATH, --module-path MODULE_PATH
                        add a Ansible modules directory
```
