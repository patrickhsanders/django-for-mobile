# Setup the Django Environment (Mac)

## Python Setup for Mac
Download and install Python 3 from python.org

### Install virtualenv using pip (pip is a package manager)
Open **Terminal**.
Type `sudo pip3 install virtualenv`

### Find the path of Python 3
Type `which python3`
__/Library/Frameworks/Python.framework/Versions/3.6/bin/python3__

### Create a virtual environment
Type `virtualenv -p <path to python 3> <env name>`

### Activate the virtual environment
Type `source <env name>/bin/activate`

**Note:**
To leave the virtual environment type `deactivate`

### Install Django from PyPi (Will install the most recent version)
Type `pip install django`

### Create a Django project
Type `django-admin startproject <project name>`

### Create a Django app (there can be many of these)
Type `cd <name>`
Type `./manage.py startapp <app name>`