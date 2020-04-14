[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=C8FBBG2RZ5WYS&currency_code=EUR&source=url)

# Daily Reflection
A small python, command line tool that helps you conduct your daily self-reflection, morning and or evening. It allows you to define questions that you want to ask to your selves and stores your daily answers in a password protected storage.

# Installation

## Via pip
* pip install daily-reflection
daily-reflection

## Via pip + git
* pip install git+git://github.com/stefanthaler/daily-reflection.git#egg=daily-reflection
daily-reflection

## Via git
* git clone git@github.com:stefanthaler/daily-reflection
* python3 -m venv .env
* . .env/bin/activate.fish  
* pip3 install -r requirements.txt
* ./daily-reflection

# Building package
* git clone git@github.com:stefanthaler/daily-reflection
* python3 -m venv .env
* . .env/bin/activate.fish  
* pip3 install -r requirements-building.txt
* python setup.py bdist_wheel

# OS Dependencies:
* python3, python3-venv, python3-pip

# Python Dependencies:
* [PyInquirer](https://github.com/CITGuru/PyInquirer)
* [TinyDB](https://tinydb.readthedocs.io/en/latest/getting-started.html)
* [tinydb-encrypted-jsonstorage](https://github.com/stefanthaler/tinydb-encrypted-jsonstorage)

# Python Dependencies Building:
* [setuptools](https://packaging.python.org/tutorials/installing-packages/)
* [wheel](https://pythonwheels.com/)
* [tqdm](https://github.com/tqdm/tqdm)
* [twine](https://pypi.org/project/twine/)

# Thanks to:
* Deepak Kumar for his tutorial on how to publish your python package on pip, https://dzone.com/articles/executable-package-pip-install
* Shields.io, for providing the github paypal button: https://shields.io/
