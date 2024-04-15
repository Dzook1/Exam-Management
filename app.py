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
        global teachID
        teachID = user[0]
        return render_template('teacherTools.html')
    else:
        return render_template('loginTeacher.html')
    
@app.route('/registrationTeacher.html', methods=['GET'])
def signupT():
    return render_template('registrationTeacher.html')

@app.route('/registrationTeacher.html', methods=['POST'])
def signupTgo():
    conn.execute(text('Insert into Teachers (First_Name, Last_Name, Email, Password) values(:Firstname, :Lastname, :Email, :Password)'), request.form)
    conn.commit()
    return render_template('registrationTeacher.html')

@app.route('/myTestsTeacher.html', methods=['GET'])
def get_myTestsTeacher():
    return render_template('myTestsTeacher.html')

@app.route('/myTestsTeacher.html', methods=['POST'])
def post_myTestsTeacher():
    data = request.form['TestName']

    query = text("INSERT INTO Tests (Test_Name, Number_Questions, Teacher_ID) VALUES (:Test_Name, 10, :Teacher_ID);")

    conn.execute(query, {'Test_Name' : data, 'Teacher_ID' : teachID})
    conn.commit()

    query = text("SELECT Test_ID FROM Tests WHERE Test_Name = :Test_Name")
    global TestID
    TestID = conn.execute(query, {'Test_Name' : data}).fetchone()[0]

    Q1 = request.form['Q1']
    Q2 = request.form['Q2']
    Q3 = request.form['Q3']
    Q4 = request.form['Q4']
    Q5 = request.form['Q5']
    Q6 = request.form['Q6']
    Q7 = request.form['Q7']
    Q8 = request.form['Q8']
    Q9 = request.form['Q9']
    Q10 = request.form['Q10']

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q1})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q2})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q3})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q4})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q5})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q6})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q7})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q8})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q9})
    conn.commit()

    query = text("INSERT INTO questions VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q10})
    conn.commit()

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
    return render_template('take_hub.html')


@app.route('/accounts.html')
def accounts():
    query = text("SELECT Teacher_ID, First_Name, Last_Name FROM Teachers")
    teacher_data = conn.execute(query)
    query = text("SELECT Student_ID, First_Name, Last_Name FROM Students")
    student_data = conn.execute(query)
    return render_template('accounts.html', teacher_data=teacher_data, student_data=student_data)

@app.route('/teacherTools.html')
def teacherTools():
    query = text("SELECT Test_ID, Test_Name, Number_Questions, Teacher_ID FROM Tests")
    test_data = conn.execute(query)
    return render_template('teacherTools.html', test_data=test_data)

@app.route('/edit.html', methods=['GET'])
def edit():
    return render_template('edit.html')

@app.route('/edit.html', methods=['POST'])
def editGo():
    conn.execute(text('update Tests set Test_ID = :Test_ID, Test_Name = :Test_Name, Number_Questions = :Number_Questions, Teacher_ID = :Teacher_ID where (Test_ID = :Test_ID)'), request.form)
    conn.commit()
    return render_template('edit.html')


@app.route('/delete.html', methods=['GET'])
def delete():
    return render_template('delete.html')


@app.route('/delete.html', methods=['POST'])
def deleteGo():
    conn.execute(text("delete from Tests where (Test_ID = :Test_ID)"), request.form)
    conn.commit()
    return render_template('delete.html')





if __name__ == '__main__':
    app.run(debug=True)