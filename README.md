# todo-list

### Setting up project (Have used python 2.7)
1. git clone <repo_url>
2. Navigate to the directory and create virtual environment `virtualenv .`
3. Activate the virtualenv `source bin/activate`
4. Install the dependencies `pip install -r requirements.txt`
5. Create the database `./manage.py migrate`
6. Create Superuser `./manage.py createsuperuser`
7. Run the server `./manage.py runserver`

### Endpoints associated
1. `/accounts/` - Contains all the django's auth urls i.e. login, logout, etc.
2. `/signup/` - Signup for user
3. `/detail/pk/` - Detail for task corresponding to pk
4. `/update/pk/` - Edit the task (login and object_permission required).
5. `/delete/pk/` - Delete the task (login and object_permission required).
6. `/create/` - Create the task (login required)
7. `
