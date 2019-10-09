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
