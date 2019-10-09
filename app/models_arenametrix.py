from . import db


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    Numero_billet = db.Column(db.Integer, unique=True, index=True)
    Prix = db.Column(db.Integer)
    Type_de_produit = db.Column(db.String)
    Filiere_de_vente = db.Column(db.String)

    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'))
    spectacle_id = db.Column(db.Integer, db.ForeignKey('spectacles.id'))
    representation_id = db.Column(db.Integer, db.ForeignKey('representations.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    def __repr__(self):                              # pragma: no cover
        return '<Ticket N.%r>' % self.Numero_billet  # pragma: no cover


class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    Reservation = db.Column(db.Integer, unique=True, index=True)
    Date_reservation = db.Column(db.Integer)
    Heure_reservation = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    spectacle_id = db.Column(db.Integer, db.ForeignKey('spectacles.id'))
    representation_id = db.Column(db.Integer, db.ForeignKey('representations.id'))

    tickets = db.relationship(
        'Ticket', backref='reservations', lazy='dynamic')

    def __repr__(self):                              # pragma: no cover
        return '<Reservation N.%r>' % self.Reservation  # pragma: no cover


class Spectacle(db.Model):
    __tablename__ = 'spectacles'
    id = db.Column(db.Integer, primary_key=True)
    Cle_spectacle = db.Column(db.Integer, unique=True, index=True)
    Spectacle = db.Column(db.String)

    tickets = db.relationship(
        'Ticket', backref='spectacles', lazy='dynamic')
    reservations = db.relationship(
        'Reservation', backref='spectacles', lazy='dynamic')
    representations = db.relationship(
        'Representation', backref='spectacles', lazy='dynamic')

    def __repr__(self):                              # pragma: no cover
        return '<Spectacle : %r>' % self.Spectacle  # pragma: no cover


class Representation(db.Model):
    __tablename__ = 'representations'
    id = db.Column(db.Integer, primary_key=True)
    Cle_representation = db.Column(db.Integer, unique=True, index=True)
    Representation = db.Column(db.String)
    Prix = db.Column(db.Integer)
    Date_representation = db.Column(db.Integer)
    Heure_representation = db.Column(db.Integer)
    Date_fin_representation = db.Column(db.Integer)
    Heure_fin_representation = db.Column(db.Integer)

    spectacle_id = db.Column(db.Integer, db.ForeignKey('spectacles.id'))

    tickets = db.relationship(
        'Ticket', backref='representations', lazy='dynamic')

    customers = db.relationship(
        'Customer', secondary='link', lazy='dynamic')



    def __repr__(self):                                         # pragma: no cover
        return '<Representation : %r>' % self.Representation    # pragma: no cover


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String)
    Prenom = db.Column(db.String)
    Email = db.Column(db.String, unique=True, index=True)
    Adresse = db.Column(db.String)
    Code_postal = db.Column(db.Integer)
    Pays = db.Column(db.String)
    Age = db.Column(db.Integer)
    Sexe = db.Column(db.String)

    tickets = db.relationship(
        'Ticket', backref='customers', lazy='dynamic')
    reservations = db.relationship(
        'Reservation', backref='customers', lazy='dynamic')

    representations = db.relationship(
        'Representation', secondary='link', lazy='dynamic')


    def __repr__(self):                              # pragma: no cover
        return '<Client : %r>' % self.Email  # pragma: no cover


link = db.Table(
    'link',
    db.Column(
        'customer_id',
        db.Integer,
        db.ForeignKey('customers.id'),
        primary_key=True),
    db.Column(
        'representation_id',
        db.Integer,
        db.ForeignKey('representations.id'),
        primary_key=True))
