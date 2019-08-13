# APIs for sample mobile application

## Setup Instructions ##

1. Prerequisites
    * System must have `python 2.7` installed
    * System must have `PostgreSQL 9.5 or higher`
        * Create a database named `mobileapidb`

2. Install requirements by running `pip install -r requirements/dev.txt`

3. Apply Migrations by running this command from the project dir

      `python manage.py migrate`

4. Create Super User

    `python manage.py createsuperuser`

6. Load data using `python manage.py loaddata fixtures.json`

5. Finally run your dev server by running this command from your project dir

    `python manage.py runserver`

## API endpoints ##

1. Docs at http://localhost:8000/
2. API root at http://localhost:8000/api/
3. Mobile API at http://localhost:8000/api/mobiles/
