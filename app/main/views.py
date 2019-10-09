from flask import render_template, redirect, url_for, abort, flash, request
from . import main
from .forms import FileForm
from app.api.routes import importcsvtodb
from app.api.routes import getstats

from flask_login import current_user, login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/import_csv', methods=['GET', 'POST'])
@login_required
def import_csv():
    form = FileForm()
    if form.validate_on_submit():
        data = importcsvtodb()
        if data.status_code == 200:
            flash('Fichier {} importé avec succès'.format(request.files['file'].filename))
            return render_template('arenametrix/import_csv.html', form=form, data=data.json)
    return render_template('arenametrix/import_csv.html', form=form)


@main.route('/extract_data', methods=['GET', 'POST'])
@login_required
def extract_data():
    data = getstats().json
    return render_template('arenametrix/extract_data.html', data=data)



@main.route('/internal', methods=['GET', 'POST'])
def internal():
    abort(500)
