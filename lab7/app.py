from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.template.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.template.html')

@app.route('/our-products')
def our_products():
    return 'our products'


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)