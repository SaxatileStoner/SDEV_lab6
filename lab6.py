"""Main python to run flask website
SDEV 300 - Lab 6
@author Christopher Stoner

TODO Grammer and spelling checks for html files
TODO Documentation document
"""
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders index.html and gives date and time as a variable
    for index.html to use. Allows user to see time and date of access.
    """
    return render_template('index.html',
                           current_date_time=datetime.today().ctime())


@app.route('/games-list')
def games_list():
    """
    Renders games-list.html web page
    """
    return render_template('games-list.html')


@app.route('/photogrpahy')
def photography():
    """
    Renders photography.html web page
    """
    return render_template('photography.html')


if __name__ == '__main__':
    app.run(debug=True)
