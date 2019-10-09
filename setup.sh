#!/usr/bin/env bash
flask db init
flask db migrate
flask db upgrade
flask createroles
flask createadmin
flask run
