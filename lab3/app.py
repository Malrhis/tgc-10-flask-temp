#import
from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)

# Flask is a server --> We are creating our own endpoint
# allow us to create a server where people can connect to depending on the url
# app.route is a 'view function'

###
@app.route('/')
def home():
    return render_template('home.template.html')
### this is a route

@app.route('/about-us')
def about():
    return "About Us. testing this return: the quick brown fox"

@app.route('/lucky')
def lucky_number():
    number = random.randint(1000,9999)
    return "Your lucky number is " + str(number)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)