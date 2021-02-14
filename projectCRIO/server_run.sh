#!/bin/bash
source ~/venv_django/bin/activate
pip3 install -r requirements.txt
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
