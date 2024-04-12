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

@app.route('/loginStudent.html', methods=['GET'])
def loginS():
    return render_template('loginStudent.html')

@app.route('/loginStudent.html', methods=['POST'])
def loginSgo():
    email = request.form['Email']
    password = request.form['Password']

    query = text('Select Student_ID from Students where Email = :email and Password = :password')
    user = conn.execute(query, {'email': email, 'password': password}).fetchone()
    if user:
        print("Yes")
        return render_template('take_hub.html')
    else:
        print("No")
        return render_template('loginStudent.html')
    
@app.route('/registrationStudent.html', methods=['GET'])
def signupS():
    return render_template('registrationStudent.html')

@app.route('/registrationStudent.html', methods=['POST'])
def signupSgo():
    conn.execute(text('Insert into Students (First_Name, Last_Name, Email, Password) values(:Firstname, :Lastname, :Email, :Password)'), request.form)
    conn.commit()
    return render_template('registrationStudent.html')

@app.route('/take_hub.html')
def takeHub():
    render_template('take_hub.html')


@app.route('/accounts.html')
def accounts():
    query = text("SELECT Teacher_ID, First_Name, Last_Name FROM Teachers")
    teacher_data = conn.execute(query)
    query = text("SELECT Student_ID, First_Name, Last_Name FROM Students")
    student_data = conn.execute(query)

    return render_template('accounts.html', teacher_data=teacher_data, student_data=student_data)



if __name__ == '__main__':
    app.run(debug=True)