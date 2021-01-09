#import
from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)

# allow us to create a server where people can connect to depending on the url
@app.route('/')
def home():
    return "<h1>Hello World. My name is gab this is a port test</h1>"

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