from flask import Flask, render_template, url_for
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main/index.html')

@app.route('/&namelist')
def namelist_not_allowed():
    return render_template('main/404.html', content="Page")

@app.route('/participants')
def participants():
    return render_template('main/all-participants.html')

@app.route('/<name>')
def card(name):
    try:
    	return render_template('%s.html' %name)
    except Exception as e:
    	return render_template('main/404.html', content="Template")

    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('main/404.html', content="Page")


if __name__ == '__main__':
    app.run(debug=True)
