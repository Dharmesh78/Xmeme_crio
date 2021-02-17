#!/bin/bash
sudo apt install -y python3-pip
sudo ln /usr/bin/python3 /usr/bin/python
#to handle the meme endpoint issue in django
sudo echo "urlpatterns.append(path('memes/',include('appCRIO.urls')))" >> ~/dharmeshsinghpaliwal-7-me_buildout_xmeme/projectCRIO/projectCRIO/urls.py
pip3 install -r requirements.txt
