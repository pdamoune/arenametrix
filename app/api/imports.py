import io
import csv
from flask import render_template, jsonify, request
from . import api

original_fields = [
    'Numero_billet',
    'Reservation',
    'Date_reservation',
    'Heure_reservation',
    'Cle_spectacle',
    'Spectacle',
    'Cle_representation',
    'Representation',
    'Date_representation',
    'Heure_representation',
    'Date_fin_representation',
    'Heure_fin_representation',
    'Prix',
    'Type_de_produit',
    'Filiere_de_vente',
    'Nom',
    'Prenom',
    'Email',
    'Adresse',
    'Code_postal',
    'Pays',
    'Age',
    'Sexe']

@api.route('/ImportCsv', methods=['POST'])
def importcsvtodb():
    f = request.files.get('file')
    if f is None:
        return 'TODO error need csv file'

    stream = io.StringIO(f.stream.read().decode("UTF8"))
    csv_input = csv.reader(stream, delimiter=';')

    # parse the csv to get a list of lists
    csv_data = [row for row in csv_input]

    # get the first line of data as the fields reference
    fields = [field.replace(' ', '_') for field in csv_data.pop(0)]

    # compare the fields to what they are supposed to be
    if fields != original_fields:
        return 'TODO error bad data'
    liste_tickets = [dict(zip(fields, l)) for l in csv_data]

    # for ticket in liste_tickets:
    #     t = Ticket.query.filter_by(Numero_billet=ticket['Numero_billet']).first()
    #     if t:
    #         continue
    #     db.session.add(Ticket(**ticket))
    #     db.session.commit()
    return jsonify(liste_tickets)


    return jsonify([{'test': 'success'}])
