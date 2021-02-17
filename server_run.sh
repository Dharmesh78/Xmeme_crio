#!/bin/bash
#source ~/venv_django/bin/activate
pip3 install -r requirements.txt
cd ~/dharmeshsinghpaliwal-7-me_buildout_xmeme/projectCRIO/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
