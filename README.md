# Flask Boilerplate
### _Flask boilerplate inspired by The Flask Mega-Tutorial by Miguel Grinberg_

![License](http://img.shields.io/:license-mit-blue.svg)

When i started learning Flask, I found a lot of boilerplates on the web. However, I decided to create mine as i was learning, in order to have a clean custom base for future projects.
Special thanks to Miguel Grinberg for his amazing tutorial, and Max Halford for the inspiration of doing my own boilerplate.

## Features

- [x] User account sign up, sign in, password reset, all through asynchronous email confirmation.
- [x] Form generation.
- [x] Error handling.
- [ ] HTML macros and layout file.
- [x] "Functional" file structure.
- [x] Python 3.x compliant.
- [x] Administration panel.
- [ ] Websockets (for example for live chatting)
- [x] Virtual environment example.
- [x] Tests.
- [x] Logging.
- [ ] Language selection.
- [ ] Automatic API views.
- [ ] API key generator.

I am open to any suggestions or help, don't hesitate to contact me at <pdamoune@gmail.com> or create an issue.

## Libraries

### Backend

- [Flask](http://flask.pocoo.org/), obviously.
- [Flask-Login](https://flask-login.readthedocs.org/en/latest/) for the user accounts.
- [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) interacting with the database.
- [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/) and [WTForms](https://wtforms.readthedocs.org/en/latest/) for the form handling.
- [itsdangerous](http://pythonhosted.org/itsdangerous/) for generating random tokens for the confirmation emails.
- [Flask-Admin](https://flask-admin.readthedocs.org/en/latest/) for building an administration interface.
- [Flask-DebugToolBar](https://flask-debugtoolbar.readthedocs.io/en/latest/) for adding a performance toolbar in development.

### Frontend

- [Bootstrap](http://getbootstrap.com/).

## Structure

I did what most people recommend for the application's structure. Basically, everything is contained in the `app/` folder.

- There you have the classic `static/` and `templates/` folders. The `templates/` folder contains error views and a common layout.
- The `models.py` script contains the SQLAlchemy code.

## Setup

### Install

- Install and Setup a virtual environment.

	`brew install mkvirtualenv`
    `mkvirtualenv project_name`

- Create the database.

    `flask db init`
    `flask db migrate`
    `flask db upgrade`

- Create Roles.

    `flask createroles`


- Create Admin account (admin@admin.com // password).

    `flask createadmin`


- Run the application.

	`flask run`

- Navigate to `localhost:8080`.


## Deployment


## Configuration

The goal is to keep most of the application's configuration in a single file called `config.py`.

Read [this](http://flask.pocoo.org/docs/0.10/config/) for information on the possible configuration options.


## Inspiration

- [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
- [Explore Flask](https://exploreflask.com/index.html).


## Other possibilities

- [flask-boilerplate](https://github.com/mjhea0/flask-boilerplate) by [Michael Herman](https://github.com/mjhea0).
- [Flask-Foundation](https://github.com/JackStouffer/Flask-Foundation) by [Jack Stouffer](https://github.com/JackStouffer).
- [fbone](https://github.com/imwilsonxu/fbone) by [Wilson Xu](https://github.com/imwilsonxu).

## License

The MIT License (MIT). Please see the [license file](LICENSE) for more information.
