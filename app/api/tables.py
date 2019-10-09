import io
import csv
from flask import request
from ..models import Customer, Spectacle, Representation, Reservation, Ticket
from app import db

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


def tickettodb(data):
    if Ticket.query.filter_by(
            Numero_billet=data['Numero_billet']).first():
        return
    ticket = Ticket(
        Numero_billet=data['Numero_billet'],
        Prix=data['Prix'],
        Type_de_produit=data['Type_de_produit'],
        Filiere_de_vente=data['Filiere_de_vente'],

        reservation_id=Reservation.query.filter_by(
            Reservation=data['Reservation']).first().id,
        spectacle_id=Spectacle.query.filter_by(
            Cle_spectacle=data['Cle_spectacle']).first().id,
        representation_id=Representation.query.filter_by(
            Cle_representation=data['Cle_representation']).first().id,
        customer_id=Customer.query.filter_by(
            Email=data['Email'].lower()).first().id
    )
    db.session.add(ticket)
    db.session.commit()
    return


def reservationtodb(data):
    if Reservation.query.filter_by(
            Reservation=data['Reservation']).first():
        return
    reservation = Reservation(
        Reservation=data['Reservation'],
        Date_reservation=data['Date_reservation'],
        Heure_reservation=data['Heure_reservation'],
        customer_id=Customer.query.filter_by(
            Email=data['Email'].lower()).first().id,
        spectacle_id=Spectacle.query.filter_by(
            Cle_spectacle=data['Cle_spectacle']).first().id,
        representation_id=Representation.query.filter_by(
            Cle_representation=data['Cle_representation']).first().id
    )
    db.session.add(reservation)
    db.session.commit()
    return


def representationtodb(data):
    if Representation.query.filter_by(
            Cle_representation=data['Cle_representation']).first():
        return
    representation = Representation(
        Cle_representation=data['Cle_representation'],
        Representation=data['Representation'],
        Prix=data['Prix'],
        Date_representation=data['Date_representation'],
        Heure_representation=data['Heure_representation'],
        Date_fin_representation=data['Date_fin_representation'],
        Heure_fin_representation=data['Heure_fin_representation'],
        spectacle_id=Spectacle.query.filter_by(
            Cle_spectacle=data['Cle_spectacle']).first().id,
    )
    db.session.add(representation)
    db.session.commit()
    return


def spectacletodb(data):
    if Spectacle.query.filter_by(Cle_spectacle=data['Cle_spectacle']).first():
        return
    spectacle = Spectacle(
        Cle_spectacle=data['Cle_spectacle'],
        Spectacle=data['Spectacle'],
    )
    db.session.add(spectacle)
    db.session.commit()
    return


def customertodb(data):
    if Customer.query.filter_by(Email=data['Email'].lower()).first():
        return
    customer = Customer(
        Nom=data['Nom'],
        Prenom=data['Prenom'],
        Email=data['Email'].lower(),
        Adresse=data['Adresse'],
        Code_postal=data['Code_postal'],
        Pays=data['Pays'],
        Age=data['Age'],
        Sexe=data['Sexe'],
    )
    db.session.add(customer)
    db.session.commit()
    return


def importcsvfromrequest():
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
    tickets = [dict(zip(fields, l)) for l in csv_data]
    return tickets
