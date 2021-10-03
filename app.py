from flask import Flask, render_template, url_for
import os

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')

def card():
    return render_template('card.html', name = "Your name here")


if __name__ == '__main__':
    app.run()
