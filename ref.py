from flask import Flask, render_template, request, redirect, session, url_for, flash
import mysql.connector
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
bcrypt = Bcrypt(app)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='your_user',
        password='your_password',
        database='doctor_consultation'
    )
    return connection

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            session['user_id'] = user['id']
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            connection.commit()
            flash('Registration successful! You can now log in.')
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError:
            flash('Username already exists.')
        finally:
            cursor.close()
            connection.close()

    return render_template('register.html')

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'])

@app.route('/doctors')
def doctors():
    if 'username' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM doctors')
    doctors = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return render_template('doctors.html', doctors=doctors)

@app.route('/schedule/<int:doctor_id>', methods=['GET', 'POST'])
def schedule(doctor_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    if request.method == 'POST':
        appointment_time = request.form['appointment_time']
        user_id = session['user_id']
        
        cursor.execute('INSERT INTO consultations (user_id, doctor_id, appointment_time) VALUES (%s, %s, %s)', 
                       (user_id, doctor_id, appointment_time))
        connection.commit()
        cursor.close()
        connection.close()
        flash('Consultation scheduled successfully!')
        return redirect(url_for('doctors'))
    
    cursor.execute('SELECT * FROM doctors WHERE id = %s', (doctor_id,))
    doctor = cursor.fetchone()
    cursor.close()
    connection.close()

    return render_template('schedule.html', doctor=doctor)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '_main_':
    app.run(debug=True)