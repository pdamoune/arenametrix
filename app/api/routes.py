from . import api
from app import db
from flask import jsonify

from ..models import (
    Customer,
    Spectacle,
    Representation,
    Reservation,
    Ticket)

from .tables import (
    importcsvfromrequest,
    customertodb,
    spectacletodb,
    representationtodb,
    reservationtodb,
    tickettodb
)


@api.route('/ImportCsv', methods=['POST'])
def importcsv():
    return jsonify(importcsvfromrequest())


@api.route('/ImportCsvToDb', methods=['POST'])
def importcsvtodb():
    data_parsed = importcsvfromrequest()
    for data in data_parsed:
        customertodb(data)
        spectacletodb(data)
        representationtodb(data)
        reservationtodb(data)
        tickettodb(data)

    return jsonify(data_parsed)


@api.route('/GetNumberUnicBuyers', methods=['GET'])
def getnumberunicbuyers():
    customers = Customer.query.all()
    unic_buyers = [buyer for buyer in customers if buyer.tickets.count() == 1]
    number_unic_buyers = len(unic_buyers)
    return jsonify(number_unic_buyers)


@api.route('/GetAverageBuyersAge', methods=['GET'])
def getaveragebuyersage():
    customers = Customer.query.all()
    ages = [c.Age for c in customers if c.Age is not '']
    if len(ages) is None:
        return jsonify('error no age')
    average_age = sum(ages) / len(ages)
    return jsonify(average_age)


@api.route('/GetNumberBooking', methods=['GET'])
def getnumberbooking():
    number_booking = Reservation.query.count()
    return jsonify(number_booking)


@api.route('/GetAverageRepresentationPrice', methods=['GET'])
def getaveragerepresentationprice():
    representations = Representation.query.all()

    prices = [p.Prix for p in representations]
    if len(prices) is None:
        return jsonify('error no price')
    average_price_representation = sum(prices) / len(prices)
    return jsonify(average_price_representation)


@api.route('/GetAverageCustomerPrice', methods=['GET'])
def getaveragecustomerprice():
    customers = Customer.query.all()
    price_average = []
    for c in customers:
        price_list = [prices.Prix for prices in c.tickets.all()]
        price_average.append(sum(price_list) / len(price_list))
    average_price_customer = sum(price_average) / len(price_average)
    return jsonify(average_price_customer)


@api.route('/GetStats', methods=['GET'])
def getstats():
    stats = {
        'Nombre de réservations': getnumberbooking().json,
        'Nombre d’acheteurs uniques': getnumberunicbuyers().json,
        'Age moyen des acheteurs': getaveragebuyersage().json,
        'Prix moyen par représentation': getaveragerepresentationprice().json,
        'Prix moyen par client': getaveragecustomerprice().json
        }
    return jsonify(stats)
