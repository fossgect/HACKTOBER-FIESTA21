from flask import Flask, render_template, url_for
import os

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def home():
    return render_template('main/index.html')


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
