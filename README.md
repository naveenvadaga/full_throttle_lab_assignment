# full_throttle_lab_assignment

heroku deployed url: https://ftlassignment.herokuapp.com/users/

## Implementation

**Architecture**: followed clean architecture  
    ref:- `https://jordifierro.com/django-clean-architecture`

* User app contains two models
  * User model which contains id, real_name, time_zone
  * UserActivityPeriod model which contains
     user(fk to User Model), start_time, end_time
* user/management/command/populate_database contains
  custom management command for populating the data to db
  from test_json.json file
* `/users/` endpoints returns a responses that contains
  all the users information
* test module contains test cases for the views, interactors,
  storages, presenters

## Running locally
* create a virtual environment
* then pip install requirements
* then run both commands
  `
    python manage.py makemigrations
    python manage.py migrate
  `
* then use the custom command
   `python manage.py populate_database` command for populating db
* then run
  `python manage.py runserver`
* then go to `http://127.0.0.1:8000/users/` to we
  list of users

**Note**:  
  If you don't run custom command( `python manage.py populate_database`  
  ), you will get empty list in get_users_data api

**To run test cases**
  * user command `pytest` in current repository


## Deployment

* For deployment, used heroku
* Used `Postgres` database given by heroku

**Note**:  
Heroku deployed code is present in  `heroku-deploy` branch





