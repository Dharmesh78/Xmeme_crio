#!/bin/bash
cd ~/dharmeshsinghpaliwal-7-me_buildout_xmeme/projectCRIO/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
