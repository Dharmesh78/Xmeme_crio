#!/bin/bash
sudo apt install -y python3-pip
sudo ln /usr/bin/python3 /usr/bin/python
#to handle the meme endpoint issue in django
#sudo echo "APPEND_SLASH=False" >> ~/dharmeshsinghpaliwal-7-me_buildout_xmeme/projectCRIO/projectCRIO/settings.py

pip3 install -r requirements.txt
