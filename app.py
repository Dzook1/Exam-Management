from sqlalchemy import create_engine, text
from flask import Flask, render_template, request

app = Flask(__name__)

conn_str = 'mysql://root:Savier010523$@localhost/exams'
engine = create_engine(conn_str, echo=True)
conn = engine.connect()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrate.html', methods = ["GET"])

if __name__ == '__main__':
    app.run(debug=True)

