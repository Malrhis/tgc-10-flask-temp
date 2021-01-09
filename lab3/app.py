#import
from flask import Flask, render_template, request, redirect, url_for
import os
import random
from datetime import datetime

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

@app.route('/say-hi')
def greetings():
    firstname = "Ah Kow"
    lastname = "Tan"
    today = datetime.now()
    return render_template('greetings.template.html',
                            fname = firstname, lname = lastname, today_date = today)

@app.route('/wish/<username>')
def wish_happy_new_year(username):
    return "Happy new year 2021, " + username

# weight / height ** 2
@app.route('/calculate/<weight>/<height>')
def calculate_bmi(weight, height):
    # any parameters read in from the URL is string
    weight = float(weight)
    height = float(height)
    bmi = weight / height ** 2
    return render_template('bmi_results.template.html',
     bmi=bmi)

# Write a route with the following url: /add/<n1>/<n2>
# n1 and n2 are supposed to be integers, for example, /add/4/5.  Display in the template, using <h1>, display the sum of n1 and n2. 
@app.route('/add/<n1>/<n2>')
def add_url(n1,n2):
    n1 = float(n1)
    n2 = float(n2)
    result = n1 + n2
    return render_template('add_results.template.html', n1 = n1, n2 = n2, result=result)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)
# usually anything below port number 1000 is reserved for ISO standards and different communities
# https://www.utilizewindows.com/list-of-common-network-port-numbers/

