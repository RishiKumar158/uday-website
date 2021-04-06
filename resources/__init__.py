from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/reference')
def reference():
    return render_template('reference.html')


@app.route('/team')
def team():
    return render_template('team.html')
