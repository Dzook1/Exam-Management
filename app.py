from sqlalchemy import create_engine, text
from flask import Flask, render_template, request

app = Flask(__name__)

conn_str = 'mysql://root:Savier010523$@localhost/exams'


@app.route('/')
def register():
    return 'Hello, Flask!'


if __name__ == '__main__':
    app.run(debug=True)
