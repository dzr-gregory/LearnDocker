#!/usr/bin/env python3
import datetime
import os
import sys
import uuid

import requests

from flask import Flask, render_template, request
from markupsafe import escape

FLASK_APP_NAME = "SampleFlaskApp"
app = Flask(FLASK_APP_NAME)

allowed_currencies = ['USD', 'EUR', 'CAD', 'UAH', 'RUB']

common_template_vars = {
    "PageTitle": "Welcome to the sample Flask app",
    "Author": "Grigory Balashov",
    "AuthorEmail": "dzr.gregory@gmail.com",
    "PageGenerationTime": datetime.datetime.now(),
    "sys": sys,
    "os": os,
    "allowed_currencies": allowed_currencies
}


def error_page(variables, message):
    variables['ErrorMessage'] = message
    return render_template('error.html', **variables)


@app.route("/")
def index():
    template_vars = {
        **common_template_vars,
    }
    return render_template('index.html', **template_vars)


@app.errorhandler(404)
def not_found(error):
    template_vars = {
        **common_template_vars,
        "ErrorMessage": "OOPS! The page you're looking for is not available. Try again, please, or use the links above"
    }
    return render_template('error.html', **template_vars), 404


@app.route("/math/add", methods=['POST', 'GET'])
def math_add():
    template_vars = {
        **common_template_vars,
    }
    if request.method == "GET":
        return render_template('add.html', **template_vars)
    elif request.method == "POST":
        try:
            value1 = int(request.form['value1'])
            value2 = int(request.form['value2'])
        except ValueError:
            template_vars['ErrorMessage'] = "At least one entered number is not actually a number!"
            return render_template('error.html', **template_vars)
        result = value1 + value2
        template_vars['ResultText'] = "The result is: %s + %s = %s" % (value1, value2, result)
        return render_template('result.html', **template_vars)
    else:
        raise ValueError("Unknown method type: %s!" % request.method)


@app.route('/random_uuid')
def random_uuid():
    template_vars = {
        **common_template_vars,
    }
    my_uuid = str(uuid.uuid4())
    template_vars['ResultText'] = "I hope this UUID4 is good enough for you: %s" % my_uuid
    return render_template('result.html', **template_vars)


@app.route("/exchange_rates/<currency>")
def exchange_rates(currency):
    template_vars = {
        **common_template_vars,
    }
    currency = escape(currency)
    if currency in allowed_currencies:
        # Not sure if this key will work forever, so in case of any issues obtain a new one
        api_key = "488fada9f36a61b6dc9ca5a1"
        url = 'https://v6.exchangerate-api.com/v6/%s/latest/%s' % (api_key, currency)

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['result'] == 'success':
                template_vars['currency'] = currency
                template_vars['rates'] = data['conversion_rates']
                return render_template('exchange_rates.html', **template_vars)

    msg = "We can't provide exchange rates for this currency: %s" % currency
    return error_page(template_vars, msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
