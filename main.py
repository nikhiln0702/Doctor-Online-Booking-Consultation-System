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
            database='doc_consult'
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
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        conn.close()
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            session['user_id'] = user['user_id']
            return redirect(url_for('dhome'))
        else:
            if 'invalid_login' not in session or not session['invalid_login']:
                flash('Invalid username or password','error')
                session['invalid_login'] = False
    else:
        session['invalid_login'] = False
    return render_template('dlogin.html')

#patient login
@app.route("/plogin",methods=['GET', 'POST'] )
def plogin():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        conn=sql_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        conn.close()
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            session['user_id'] = user['user_id']
            return redirect(url_for('phome'))
        else:
                flash('Invalid username or password','error')
                
    
    return render_template('plogin.html')


#signup
@app.route("/signup",methods=['GET', 'POST'] )
def signup():
    if request.method=='POST':
         username = request.form['username']
         email = request.form['email']
         password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
         conn=sql_connection()
         cursor=conn.cursor(dictionary=True)
         try:
             cursor.execute('INSERT INTO users (username,email, password) VALUES (%s, %s,%s)', (username,email, password))
             conn.commit()
             return redirect(url_for('details'))
         except sql.IntegrityError:
            flash('Username already exists.','error')
         finally:
            conn.close()
             
             
    return render_template('signup.html')


#patient_home_page
@app.route('/phome')
def phome():
    user_name = session.get('username', 'Guest')
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('phome.html', user_name=session['username'])


#registration_details
@app.route("/details",methods=['GET', 'POST'] )
def details():
    #copy from bookdetails
    if request.method=='POST':
         name = request.form['name']
         date = request.form['dob']
         tel = request.form['tel']
         address = request.form['address']
         conn=sql_connection()
         cursor=conn.cursor(dictionary=True)
         try:
             cursor.execute('INSERT INTO users (username,email, password) VALUES (%s, %s)', (name,date))
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
    cursor.execute('SELECT name,speciality,experience,qualification FROM doctor')
    doctors = cursor.fetchall()
    conn.close()
    return doctors


#booking
@app.route("/booking")
def booking():
    doctors = get_doctors()  # Retrieve doctor data from the database
    return render_template('booking.html', doctors=doctors)  # Pass data to the template


@app.route("/book_details", methods=['GET', 'POST'])
def book_details():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        patient_age = request.form['patient_age']
        appointment_date = request.form['appointment_date']
        appointment_time = request.form['appointment_time']
        payment_option = request.form['payment_option']

        # Database connection
        conn = sql_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # Insert query
            cursor.execute(
                'INSERT INTO booking (patient_name, patient_age, appointment_date, appointment_time, payment_option) VALUES (%s, %s, %s, %s, %s)',
                (patient_name, patient_age, appointment_date, appointment_time, payment_option)
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


@app.route("/pappointment")
def pappointment():
    # Connect to the database
    conn = sql_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Fetch all appointments from the database
        cursor.execute("SELECT * FROM booking WHERE patient_name=%s", (session['username'],))

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



@app.route("/user")
def user():
    return render_template('user.html')




if __name__=="__main__":
    app.run(debug=True)