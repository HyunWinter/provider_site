# Provider Site

Django-based web application for a generic healthcare provider that we can reuse. Landing page, contact us, blog, etc.

## Features

- Search services by name.
- Sort services by cash price (ascending or descending).

## Local Development Set-up

### Pre requirements
1. PostgreSQL
2. Python 3
3. Heroku CLI

### Configuration

1. Create a virtual environment and install the requirements from requirements.txt:

```
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

2. Create the environment variables on `venv/bin/active`:

3. Run the migrations:
```
python manage.py migrate
```

5. Run the dev server:
```
python manage.py runserver
```

Then you should be able to access the site at http://127.0.0.1:8000/

