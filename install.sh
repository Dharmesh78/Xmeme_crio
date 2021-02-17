#!/bin/bash
sudo apt install -y python3-pip
sudo pip3 install virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
source /usr/local/bin/virtualenvwrapper.sh
source ~/.bashrc
sudo pip3 install virtualenv
sudo mkvirtualenv --python=python3.6.9  ~/venv_django
sudo apt install -y python3-pip
sudo pip3 install -r requirements.txt
