# Installation

1. Create a virtualenv and install python dependencies (requires [Pipenv](https://docs.pipenv.org/)):

        pipenv install

2. Create and fill out the local configuration file:

       mv tikn/settings/local.py.example tikn/settings/local.py

3. Run database migrations:

        pipenv run ./manage.py migrate

4. Start the development server:

       pipenv run ./manage.py runserver
