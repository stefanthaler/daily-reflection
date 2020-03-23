# Daily Reflection
A smallpython, command line tool that helps you conduct your daily self-reflection, morning and or evening. It allows you to define questions that you want to ask to your selves and stores your daily answers in a password protected storage.

# Installation

## Via pip
* TBD 

## Via pip + git
* TBD

## Via git
* git clone git@github.com:stefanthaler/daily-reflect
* python3 -m venv .env
* . .env/bin/activate.fish  
* pip3 install -r requirements.txt
* ./daily-reflect



# Building package
* git clone git@github.com:stefanthaler/daily-reflect
* python3 -m venv .env
* . .env/bin/activate.fish  
* pip3 install -r requirements-building.txt
* python setup.py bdist_wheel

# OS Dependencies:
* python3, python3-venv, python3-pip

# Python Dependencies:
* PyInquirer
* TinyDB
* PyCryptodome

# Python Dependencies Building:
* setuptools
* wheel
* tqdm
* twine

# Thanks to::
* Deepak Kumar for his tutorial on how to publish your python package on pip, https://dzone.com/articles/executable-package-pip-install
