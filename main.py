from flask import Flask, render_template,request,session,url_for,redirect,flash,jsonify
import mysql.connector as sql
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'
bcrypt = Bcrypt(app)

def sql_connection():
    conn = sql.connect(host="localhost",
            user='root',
            password='Root12345',
            database='livemedico'
)
    return conn

@app.route("/")
def index():
    return render_template('index.html')

#doctor login
@app.route("/dlogin",methods=['GET', 'POST'] )
def dlogin():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        conn=sql_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM doctors WHERE doctor_username = %s', (username,))
        user = cursor.fetchone()
        conn.close()
        if user and bcrypt.check_password_hash(user['doctor_password'], password):
            session['doc_name'] = user['doctor_name']
            session['doc_id'] = user['doctor_id']
            session['d_username']=user['doctor_username']
            return redirect(url_for('dhome'))
        else:
                flash('Invalid username or password','error')
   
    return render_template('dlogin.html')

#patient login
@app.route("/plogin",methods=['GET', 'POST'] )
def plogin():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        conn=sql_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM patients WHERE patients_username = %s', (username,))
        user = cursor.fetchone()
        conn.close()
        if user and bcrypt.check_password_hash(user['patient_password'], password):
            print("User authenticated, redirecting to phome...")
            session['pat_id'] = user['patient_id']
            session['name'] = user['patient_name']
            session['p_username']=user['patients_username']
            return redirect(url_for('phome'))
        else:
                flash('Invalid username or password','error')
    
    return render_template('plogin.html')


#admin login
@app.route("/alogin",methods=['GET', 'POST'] )
def alogin():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        conn=sql_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM admin WHERE admin_username = %s', (username,))
        user = cursor.fetchone()
        conn.close()
        if user and bcrypt.check_password_hash(user['admin_password'], password):
            
            session['a_username']=user['admin_username']
            return redirect(url_for('ahome'))
        else:
                flash('Invalid username or password','error')
    return render_template('alogin.html')


#signup
@app.route("/signup",methods=['GET', 'POST'] )
def signup():
    if request.method=='POST':
         username = request.form['username']
         email = request.form['email']
         password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
         name = request.form['name']
         dob = request.form['dob']
         cn = request.form['cn']
         city = request.form['city']
         conn=sql_connection()
         cursor=conn.cursor(dictionary=True)
         try:
             cursor.execute('INSERT INTO patients (patients_username,patient_email, patient_password,patient_name,patient_dob,patient_cn,patient_city) VALUES (%s, %s,%s,%s,%s,%s,%s)', (username,email, password,name,dob,cn,city))
             conn.commit()
             return redirect(url_for('phome'))
         except sql.IntegrityError:
            flash('Username already exists.','error')
         finally:
            conn.close()
             
             
    return render_template('signup.html')


#patient_home_page
@app.route('/phome')
def phome():
    if 'p_username' not in session:
        return redirect(url_for('plogin'))
    return render_template('phome.html', user_name=session['name'])

#doctor home page
@app.route('/dhome')
def dhome():
    if 'd_username' not in session:
        return redirect(url_for('dlogin'))
    return render_template('dhome.html', user_name=session['doc_name'])

#admin home page
@app.route('/ahome')
def ahome():
    user_name = session.get('username', 'Guest')
    if 'a_username' not in session:
       return redirect(url_for('alogin'))
    return render_template('ahome.html', user_name=session['a_username'])


#registration_details
@app.route("/details",methods=['GET', 'POST'] )
def details():
    #copy from bookdetails
    if request.method=='POST':
         name = request.form['name']
         dob = request.form['dob']
         cn = request.form['cn']
         city = request.form['city']
         conn=sql_connection()
         cursor=conn.cursor(dictionary=True)
         try:
             cursor.execute('INSERT INTO patients (patient_name,patient_dob,patient_cn,patient_city) VALUES (%s,%s,%s,%s)', (name,dob,cn,city))
             conn.commit()
             flash('Registration successful! You can now log in.','success')
             return redirect(url_for('plogin'))
         except :
            flash('Error','error')
         finally:
            conn.close()
    return render_template('details.html')

def get_doctors():
    conn=sql_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT doctor_name,doctor_speciality,doctor_experience,doctor_id FROM doctors')
    doctors = cursor.fetchall()
    conn.close()
    return doctors


#booking
@app.route("/booking")
def booking():
    doctors = get_doctors()  # Retrieve doctor data from the database
    return render_template('booking.html', doctors=doctors)  # Pass data to the template

#booking details
@app.route("/book_details", methods=['GET', 'POST'])
def book_details():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        patient_age = request.form['patient_age']
        appointment_date = request.form['appointment_date']
        appointment_time = request.form['appointment_time']
        mode=request.form['mode']
        payment_option = request.form['payment_option']
        doctor_name=request.form['doctor_name']
        doctor_id=request.form['doctor_id']

        # Database connection
        conn = sql_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # Insert query
            cursor.execute(
                'INSERT INTO appointment (patient_id,doctor_id,patient_name, patient_age, appointment_date, appointment_time,appointment_mode, appointment_payment,doctor_name) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)',
                (session['pat_id'],doctor_id,patient_name, patient_age, appointment_date, appointment_time,mode, payment_option,doctor_name)
            )
            conn.commit()  # Save changes
            return redirect(url_for('phome'))
        
        except Exception as e:
            print("Error:", e)  # Print the error message for debugging
            flash(f"Error: {str(e)}", "error")

        finally:
            cursor.close()
            conn.close()  # Close the connection

    return render_template('book_details.html')

#shows current appointments
@app.route("/pappointment")
def pappointment():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT * FROM appointment WHERE patient_id=%s", (session['pat_id'],))

        appointments = cursor.fetchall()  # Get all rows as a list of dictionaries

    except Exception as e:
        print("Error fetching data:", e)
        appointments = []  # In case of an error, return an empty list
        flash("Error retrieving appointments.", "error")

    finally:
        cursor.close()
        conn.close()

    # Render the appointments.html template and pass the appointments data
    return render_template("pappointment.html", appointments=appointments)

@app.route('/dappointment')
def dappointment():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT * FROM appointment WHERE doctor_id=%s", (session['doc_id'],))

        appointments = cursor.fetchall()  # Get all rows as a list of dictionaries

    except Exception as e:
        print("Error fetching data:", e)
        appointments = []  # In case of an error, return an empty list
        flash("Error retrieving appointments.", "error")

    finally:
        cursor.close()
        conn.close()
    return render_template("dappointment.html",appointments=appointments)

@app.route("/aappointments")
def aappointments():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT * FROM appointment")

        appointments = cursor.fetchall()  # Get all rows as a list of dictionaries

    except Exception as e:
        print("Error fetching data:", e)
        appointments = []  # In case of an error, return an empty list
        flash("Error retrieving appointments.", "error")

    finally:
        cursor.close()
        conn.close()
    return render_template('aapointments.html',appointments=appointments)



#logout
@app.route('/plogout')
def plogout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('plogin'))

@app.route('/dlogout')
def dlogout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('dlogin'))

@app.route('/alogout')
def alogout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('alogin'))


#acknowlegement form
@app.route("/acknow")
def acknow():
    
    return render_template('acknow.html')


#tips
@app.route("/tips")
def tips():
    return render_template('tips.html')

#profile pages
@app.route("/pprofile")
def pprofile():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT patient_name, patient_email, patients_username, patient_dob, patient_cn, patient_city FROM patients WHERE patient_id = %s", (session['pat_id'],))

        profile = cursor.fetchone()
    except Exception as e:
        print("Error fetching data:", e)
        profile = []  # In case of an error, return an empty list
        flash("Error retrieving appointments.", "error")

    finally:
        cursor.close()
        conn.close()
    return render_template('pprofile.html',profile=profile)

@app.route("/dprofile")
def dprofile():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT doctor_name,doctor_username,doctor_speciality,doctor_experience,doctor_city FROM doctor where doctor_id=%s",(session[('doc_id')],))

        profile = cursor.fetchone()
    except Exception as e:
        print("Error fetching data:", e)
        profile = []  # In case of an error, return an empty list
        flash("Error retrieving appointments.", "error")

    finally:
        cursor.close()
        conn.close()
    return render_template('dprofile.html',profile=profile)

@app.route("/editprofile",methods=['GET', 'POST'])
def editprofile():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        # Update user details from the form submission
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        dob = request.form['dob']
        phone = request.form['phone']
        city = request.form['city']

        # SQL query to update the user's profile
        cursor.execute("UPDATE patients SET patient_name=%s, patient_email=%s, patients_username=%s, patient_dob=%s, patient_cn=%s, patient_city=%s WHERE patient_id=%s", 
                       (name, email, username, dob, phone, city, session['pat_id']))
        conn.commit()  # Commit the changes to the database
        return redirect(url_for('pprofile'))
        
    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT patient_name,patient_email,patients_username,patient_dob,patient_cn,patient_city FROM patients where patient_id=%s",(session['pat_id'],))

        profile = cursor.fetchone()
    except Exception as e:
        print("Error fetching data:", e)
        profile = []  # In case of an error, return an empty list
        flash("Error retrieving appointments.", "error")

    finally:
        cursor.close()
        conn.close()
    
    return render_template('editprofile.html',profile=profile)


@app.route("/users")
def users():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT * FROM patients")

        patients = cursor.fetchall()  # Get all rows as a list of dictionaries

    except Exception as e:
        print("Error fetching data:", e)
        patients = []  # In case of an error, return an empty list
        flash("Error retrieving appointments.", "error")

    finally:
        cursor.close()
        conn.close()

    # Render the appointments.html template and pass the appointments data
    return render_template("users.html", patients=patients)

@app.route("/doctor")
def doctor():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT * FROM doctors")

        doctors = cursor.fetchall()  # Get all rows as a list of dictionaries

    except Exception as e:
        print("Error fetching data:", e)
        doctors = []  # In case of an error, return an empty list
        flash("Error retrieving appointments.", "error")

    finally:
        cursor.close()
        conn.close()

    # Render the appointments.html template and pass the appointments data
    return render_template("doctor.html", doctors=doctors)
    

@app.route("/edit_doctor/<int:doctor_id>", methods=['GET', 'POST'])
def edit_doctor(doctor_id):
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        # Get updated data from the form
        name = request.form['doctor_name']
        speciality = request.form['doctor_speciality']
        experience = request.form['doctor_experience']
        username = request.form['doctor_username']
        city = request.form['doctor_city']
        
        # Update the doctor’s information in the database
        cursor.execute("UPDATE doctors SET doctor_name=%s, doctor_speciality=%s, doctor_experience=%s, doctor_username=%s, doctor_city=%s WHERE doctor_id=%s", 
                       (name, speciality, experience, username, city, doctor_id))
        conn.commit()
        flash("Doctor information updated successfully.", "success")
        return redirect(url_for('doctor'))
    
    # Fetch current doctor data to pre-fill the form
    cursor.execute("SELECT * FROM doctors WHERE doctor_id = %s", (doctor_id,))
    doctor = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit_doctor.html', doctor=doctor)

@app.route("/delete_doctor/<int:doctor_id>", methods=['POST'])
def delete_doctor(doctor_id):
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM doctors WHERE doctor_id = %s", (doctor_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Doctor deleted successfully.", "success")
    return redirect(url_for('doctor'))


@app.route("/add",methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        doctor_name = request.form['doctor_name']
        doctor_speciality = request.form['doctor_speciality']
        doctor_experience = request.form['doctor_experience']
        doctor_username = request.form['doctor_username']
        doctor_password=bcrypt.generate_password_hash(request.form['doctor_password']).decode('utf-8')
        doctor_city = request.form['doctor_city']

        try:
            conn = sql_connection()
            cursor = conn.cursor()
            # Insert the new doctor into the database
            cursor.execute("""
                INSERT INTO doctors (doctor_name, doctor_speciality, doctor_experience, doctor_username,doctor_password,doctor_city)
                VALUES (%s, %s, %s, %s, %s,%s)
            """, (doctor_name, doctor_speciality, doctor_experience, doctor_username, doctor_password,doctor_city))
            conn.commit()
            flash("Doctor added successfully!", "success")
            return redirect(url_for('ahome'))  # Redirect to admin home or another page

        except  :
            flash("Failed to add doctor. Please try again.", "error")

        finally:
            cursor.close()
            conn.close()

    # For GET requests, render the 'Add Doctor' form
    return render_template('add.html')





if __name__=="__main__":
    app.run(debug=True)