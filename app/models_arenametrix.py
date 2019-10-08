from . import db


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    Numero_billet = db.Column(db.Integer)
    Prix = db.Column(db.Integer)
    Type_de_produit = db.Column(db.String)
    Filiere_de_vente = db.Column(db.String)

    def __repr__(self):                              # pragma: no cover
        return '<Ticket N.%r>' % self.Numero_billet  # pragma: no cover


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Reservation = db.Column(db.Integer)
    Date_reservation = db.Column(db.Integer)
    Heure_reservation = db.Column(db.Integer)

    def __repr__(self):                              # pragma: no cover
        return '<Reservation N.%r>' % self.Reservation  # pragma: no cover


class Spectacle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Cle_spectacle = db.Column(db.Integer)
    Spectacle = db.Column(db.String)

    def __repr__(self):                              # pragma: no cover
        return '<Spectacle : %r>' % self.Spectacle  # pragma: no cover


class Representation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Cle_representation = db.Column(db.Integer)
    Representation = db.Column(db.String)
    Date_representation = db.Column(db.Integer)
    Heure_representation = db.Column(db.Integer)
    Date_fin_representation = db.Column(db.Integer)
    Heure_fin_representation = db.Column(db.Integer)

    def __repr__(self):                                         # pragma: no cover
        return '<Representation : %r>' % self.Representation    # pragma: no cover


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String)
    Prenom = db.Column(db.String)
    Email = db.Column(db.String)
    Adresse = db.Column(db.String)
    Code_postal = db.Column(db.Integer)
    Pays = db.Column(db.String)
    Age = db.Column(db.Integer)
    Sexe = db.Column(db.String)

    def __repr__(self):                              # pragma: no cover
        return '<Client : %r>' % self.Email  # pragma: no cover
