pip install django	- install file to someware

pipenv install django	- install file to project folder	# best way


# setps to setup pipenv
	pip install pipenv
		pip show pipenv
		pipenv --version


# activate virtual environment
pipenv shell


# to start project
django-admin	 show commands
django-admin startproject storefront .


# to run project
python manage.py	# show commands
python manage.py runserver 		# run server
python manage.py runserver 7000 	# run with custom port number

# set python interpreter as project directory virtual environment
Ctrl + P
>pyhton interpreter
copy current path using `pipenv --venv` 
select `enter interpreter path` paste it  with + \Scripts\python.exe
	eg: C:\Users\charith\.virtualenvs\storefront-JshKXDAk\Scripts\python.exe

# vs code tricks
Ctrl + `	- open terminal
Ctrl + L	- clear terminal

# create app
python manage.py startapp playground

*migration folder* generating database tables
*admin.py* how admin interface looks like
*apps.py* config app
*models.py* define model classes and pull up data from DB and present to user
*views.py* request -> response, request handler
