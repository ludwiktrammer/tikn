# Installation

1. Create and ented virtualenv environment using Python 3:

        virtualenv -p python3 venv
        source venv/bin/activate
    (alternatively you can use a conda environment)

2. Install the requirements:

        pip install -r requirements.txt

3. Create and fill out the local configuration file:

       mv tikn/settings/local.py.example tikn/settings/local.py

4. Run database migrations:

        python manage.py migrate

5. Start the development server:

       python manage.py runserver
