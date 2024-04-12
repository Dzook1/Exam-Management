from flask import Flask, render_template, request, send_from_directory
from sqlalchemy import create_engine, text

app = Flask(__name__)

conn_str = 'mysql://root:cset155@localhost/exams'
engine = create_engine(conn_str, echo=True)
conn = engine.connect()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loginTeacher.html', methods=['GET'])
def loginT():
    return render_template('loginTeacher.html')

@app.route('/loginTeacher.html', methods=['POST'])
def loginTgo():
    email = request.form['Email']
    password = request.form['Password']

    query = text('Select Teacher_ID from Teachers where Email = :email and Password = :password')
    user = conn.execute(query, {'email': email, 'password': password}).fetchone()
    if user:
        print("Yes")
        return render_template('myTestsTeacher.html')
    else:
        print("No")
        return render_template('loginTeacher.html')
    
@app.route('/registrationTeacher.html', methods=['GET'])
def signupT():
    return render_template('registrationTeacher.html')

@app.route('/registrationTeacher.html', methods=['POST'])
def signupTgo():
    conn.execute(text('Insert into Teachers (First_Name, Last_Name, Email, Password) values(:Firstname, :Lastname, :Email, :Password)'), request.form)
    conn.commit()
    return render_template('registrationTeacher.html')

@app.route('/myTestsTeacher.html')
def myTestsTeacher():
    return render_template('myTestsTeacher.html')

@app.route('/static/index.js')
def send_js(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True)