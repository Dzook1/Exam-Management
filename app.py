
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/registration')
def registration():
    return render_template('registrate.html')