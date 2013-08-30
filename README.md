Knotcrafters
============

This is the code that runs [http://www.knotcrafters.com]().

Development Environment
-----------------------

Use the following steps to get a development environment up and running. Make
sure you already have git, pip and virtualenvwrapper set up.

    # Create teh virtual env
    mkvirtualenv knotcrafters
    # Clone the project
    git clone https://github.com/althalus/knotcrafters.git
    cd  knotcrafters
    # Install requirements
    pip install -r requirements/local.txt
    # You'll need a facebook application for login to work properly.
    export FACEBOOK_APP_ID=yourappid
    export FACEBOOK_API_SECRET=yourapisecret
    # sync the database
    python knotdirectory/manage.py syncdb
    python knotdirectory/manage.py migrate
    # Start up the dev server
    python knotdirectory/manage.py runserver

Production Environment
----------------------

The production settings expect to load a lot of things from environment
variables, but some of it will still be specific to my webfaction account.
You may want to write your own settings file for production use.

Contributing
------------

I'll gladly accept pull requests, particularly if you include tests, and
especially if you make up for my lack of them! :)

CONTRIBUTORS
------------

* Justin Steward / justin@justinsteward.com

This project uses the [django-twoscoops-project](https://github.com/twoscoops/django-twoscoops-project) template.
