from flask import render_template, redirect, url_for, abort, flash, request
from . import main
from .forms import FileForm
from app.api.imports import importcsvtodb

from flask_login import current_user


@main.route('/', methods=['GET', 'POST'])
def index():
    # if form.validate_on_submit():
    #     return redirect(url_for('.index'))
    return render_template('index.html')


@main.route('/import_csv', methods=['GET', 'POST'])
def import_csv():
    form = FileForm()
    if form.validate_on_submit():
        data = importcsvtodb()
        if data.status_code == 200:
            flash('Fichier {} importé avec succès'.format(request.files['file'].filename))
            return render_template('arenametrix/import_csv.html', form=form, data=data.json)
    return render_template('arenametrix/import_csv.html', form=form)


@main.route('/internal', methods=['GET', 'POST'])
def internal():
    abort(500)
