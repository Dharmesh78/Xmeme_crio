The project is developed in virtual environment


FOR MANUAL EXECUTION:

    The repository contains two folder :
        1.venv_django  : the virtual environment
        2.projectCRIO:   the actual project parent directory
        
    After cloning the repository, 
    CD into the cloned repo
    activate the virtual environment first by following command:
        source venv_django/bin/activate
        
    CD into projectCRIO
    Then give following commands to run the project:
        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver
        
        
FOR TESTING:
    After cloning the repository
    CD into the cloned repo
    chmod +x test_server.sh
    ./test_server.sh
