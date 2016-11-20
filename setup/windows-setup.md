# Setup the Django Environment (Windows)

## Python Setup for Windows 10
Download and install Python 3 from python.org

For the rest of this tutorial, we're going to assume the use of PowerShell. 

## Setup PowerShell environment variables
Search for `Edit the system environment variables` then click _Environment Variables..._  

or

In `run` type `sysdm.cpl`, click _Advanced_ tab, click _Environment Variables..._  

Then click `Path` then click `Edit`. 

Click the `New` button and enter the path to Python's installation. It will be something like `C:\Users\<username>\AppData\Local\Programs\Python\Python35-32` and also the scripts directory in that folder `C:\Users\<username>\AppData\Local\Programs\Python\Python35-32\Scripts`

Test that you can access Python in Command Prompt or Powershell by typing `python --version` 

### Install virtualenv using pip (pip is a package manager)
Type `pip install virtualenv`

### Update PowerShell SecurityPolicy
In order to run the virtualenv you will have to modify PowerShell's script security policy

Open PowerShell as an administrator. 
Type `Set-ExecutionPolicy Unrestricted` (There may be a safer way to do this)
Close PowerShell.
Reopen as non-administrator.  

### Create a virtual environment
Type `virtualenv <env name>`

### Activate the virtual environment
Type `.\<env name>\Scripts\activate`

**Note:**
To leave the virtual environment type `deactivate`

### Install Django from PyPi (Will install the most recent version)
Type `pip install django`

### Create a Django project
Type `django-admin startproject <project name>`

### Create a Django app (there can be many of these)
Type `cd <name>`
Type `python manage.py startapp <app name>`