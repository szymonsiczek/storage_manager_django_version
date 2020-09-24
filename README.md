# storage_manager_django_version
This web lets you manage items in your storage by adding item to the storage, deleting item from the storage, showing all items from the storage, showing items from one category, deleting all items in the storage.

Step 1, create a virtual environment:
- run terminal and change cwd to folder containing the project storagemanager (there should be a requirements.txt file)
- in the terminal type python –m venv venv_name (where venv_name is your virtual environment name)
- in the terminal type venv_name\Scripts\activate.bat to activate your virtual environment
- in the terminal type pip install –r requirements.txt to install all the packages required for that project (make sure that your cwd is in the same directory as the requirements.txt file) 

How to run an app:
- Change your CWD in terminal to folder storagemanager (the one that contains file "manage.py")
- Run command: python manage.py runserver
- Open "localhost:8000" in yor browser
