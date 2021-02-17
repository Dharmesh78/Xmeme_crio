#!/bin/bash
source ~/venv_django/bin/activate
sudo pip3 install -r requirements.txt
cd projectCRIO/projectCRIO
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
