# djangoShell

### This is a django shell. It contains everything you need to begin building your own django site. Follow the instructions below and feel free to come to me with any questions or issues.
### Note: This shell was created using python 3.7 and Django 2.2.

## Steps to get started:

#### 1. Fork or clone the djangoShell repo:
`enter repo`

#### 2. Create your own local virtual environment via:
`python3.7 -m venv .`

#### 3. Create a database file called: 
`cd src` -->
`touch db.sqlite3`

#### 4. Update your database with the following commands:

Execute migration of data models to database.

`python manage.py migrate`
    
#### 5. Create your admin account:
`python manage.py createsuperuser`

Enter your desired username and press enter.

`Username: admin`

You will then be prompted for your desired email address:

`Email address: admin@example.com`

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

```
Password: **********
Password (again): *********
Superuser created successfully.
```

#### 6. Spin up the local server: 
`python manage.py runserver`

## Additional Recommendations
In order to use custom domain names, I recommend updating your local host file. 

`sudo nano /etc/hosts`

```
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost
127.0.0.1       www.MySite.io
```


