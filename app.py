from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def card():
    return render_template('card.html', name = "Your name here")


if __name__ == '__main__':
    app.run()