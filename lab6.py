"""Main python to run flask website
SDEV 300 - Lab 6
@author Christopher Stoner

TODO Grammer and spelling checks for html files
"""
from datetime import datetime
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', current_date_time=datetime.today().ctime())


@app.route('/games-list')
def games_list():
    return render_template('games-list.html')


@app.route('/photogrpahy')
def photography():
    return render_template('photography.html')


if __name__ == '__main__':
    app.run(debug=True)
