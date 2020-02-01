### Generate connection between Google API

* Create new project in [Google API](https://console.developers.google.com  "Heading link")
* Enable calendar
![](https://gitlab.deployed.pl/viciu/django-google-calendar/uploads/e3985394563ed86817919efbb3af9328/Google_Calendar_API_Enable.PNG)
* Create credential (OAuth2.0) and download .json file and path file 
![](https://gitlab.deployed.pl/viciu/django-google-calendar/uploads/acdf4d274f84364f2af1fd74102d4b94/create_credential.PNG)
* Open script - token_generator.py and define path 
* Run script and follow the instructions

###  Install require libraries
	To install require library put to terminal pip install -r requirements.txt
	
### Run an application
    To run application put to terminal:
            1. python manage.py makemigrations
            2. python manage.py migrate
            3. python manage.py runserver
### Tests
    To establisth tests put command manage.py test event
### Main page

### Add new record
* Data picker available 

### My event table
* You can edit and remove records (with synchronization)

### Synchronize records with google calendar
* To synchronize records between google calendar and database put synchronize
