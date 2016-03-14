#!/usr/bin/env python
from flask import Flask, render_template, send_from_directory
import getpass
app = Flask(__name__)

@app.route('/')
def homepage():
    username = getpass.getuser()
    return render_template('homepage.html',
                           username=username,
                           active_page='home')

@app.route('/gallery')
def gallery():
    photos = []
    for x in range(30):
        photos.append({
            "name" : "Chat %s" % (x+1),
            "caption" : "Super Chat %s" % (x+1),
            "url" : "http://lorempixel.com/300/200/cats/",
        })
    return render_template('gallery.html',
                            photos=photos,
                            active_page='gallery')

@app.route('/contact')
def contact():
    return render_template('contact.html',
                            active_page='contact')

@app.route('/bower_components/<path:path>')
def send_bower_components(path):
    return send_from_directory('bower_components', path)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
