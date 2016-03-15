#!/usr/bin/env python
from flask import Flask, render_template, send_from_directory
import getpass
app = Flask(__name__)

@app.route('/')
def homepage():
    username = getpass.getuser()
    return render_template('homepage.html',
                           active_page='home')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html',
                            active_page='gallery')

@app.route('/album')
def contact():
    return render_template('album.html',
                            active_page='album')

@app.route('/bower_components/<path:path>')
def send_bower_components(path):
    return send_from_directory('bower_components', path)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
