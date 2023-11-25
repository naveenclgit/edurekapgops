from flask import Flask, render_template, request, redirect, session, flash, jsonify
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from helpers import apology, login_required, lookup, usd, adlogin_required

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MySQL Configuration
app.config['MYSQL_HOST'] = '10.0.1.46'
app.config['MYSQL_USER'] = 'tbtbappuser'
app.config['MYSQL_PASSWORD'] = 'tbtbapppwd'
app.config['MYSQL_DB'] = 'cs50db'
mysql = MySQL(app)

# Custom filter
app.jinja_env.filters["usd"] = usd


# Home Page

@app.route('/')
def home():
    return render_template('index.html')


# Register User
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = sha256_crypt.encrypt(request.form['password'])

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO appuser(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
        mysql.connection.commit()
        cur.close()

        flash('You are now registered and can log in', 'success')
        return redirect('/login')

    return render_template('register.html')


# Register Admin

@app.route('/adregister', methods=['GET', 'POST'])
@adlogin_required
def adregister():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = sha256_crypt.encrypt(request.form['password'])

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO adminuser(name, password,email) VALUES(%s, %s, %s)", (name, password, email))
        mysql.connection.commit()
        cur.close()

        flash('You are now registered a new admin and can log in', 'success')
        return redirect('/admin_login')

    return render_template('admin_register.html')


# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password_candidate = request.form['password']

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT id,name,email,password FROM appuser WHERE email = %s", [email])

        if result > 0:
            data = cur.fetchone()
            # print(data)
            password = data[3]
            # print(password)

            if sha256_crypt.verify(password_candidate, password):
                session['user_id'] = True
                session['email'] = email
                session['id'] = data[0]

                flash('You are now logged in', 'success')
                return redirect('/dashboard')
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            cur.close()
        else:
            error = 'Email not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


# Admin Login

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        name = request.form['username']
        password_candidate = request.form['password']

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT id,name,password FROM adminuser WHERE name = %s", [name])

        if result > 0:
            data = cur.fetchone()
            password = data[2]

            if sha256_crypt.verify(password_candidate, password):
                session['admin_id'] = True
                session['name'] = name
                session['id'] = data[0]

                flash('You are now logged in', 'success')
                return redirect('/dashboard')
            else:
                error = 'Invalid login'
                return render_template('admin_login.html', error=error)
            cur.close()
        else:
            error = 'User not found'
            return render_template('admin_login.html', error=error)

    return render_template('admin_login.html')


# User Logout

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect('/')


# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# Add Routes (Admin Page)
@app.route('/add_routes', methods=['GET', 'POST'])
@adlogin_required
def add_routes():
    if request.method == 'POST':
        busid = request.form['brand']
        fromloc = request.form['fromloc']
        toloc = request.form['toloc']
        datet = request.form['date']
        price = request.form['price']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO routes(buses_id,fromloc,toloc,dateoft,price,adminuser_id) VALUES(%s,%s,%s,%s,%s,%s)",
                    (busid, fromloc, toloc, datet, price, session['id']))
        mysql.connection.commit()
        cur.close()

        flash('Route added successfully', 'success')
        return redirect('/add_routes')

    cur = mysql.connection.cursor()
    result = cur.execute("SELECT id, brand from buses")
    if result > 1:
        print(result)
        cur.execute("SELECT id, brand from buses")
        records = cur.fetchall()
        print(records[1][1])
        cur.close()

        return render_template('add_routes.html', result=records)
    else:
        error = "There are no Buses"
        return render_template('add_routes.html', error=error)


# Add Buses (Admin Page)
@app.route('/add_buses', methods=['GET', 'POST'])
@adlogin_required
def add_buses():
    if request.method == 'POST':
        brand = request.form['brand']
        seats = request.form['seats']
        image = request.files['photo']
        file_contents = image.read()
        seats = int(seats)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO buses(brand,seats,photo,adminuser_id) VALUES(%s,%s,%s,%s)",
                    (brand, seats, file_contents, session['id']))
        mysql.connection.commit()
        cur.close()

        flash('Bus added successfully', 'success')
        return redirect('/add_buses')

    return render_template('add_buses.html')


# Admin Reports

@app.route('/reports')
@adlogin_required
def reports():
    # Code for booking tickets
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand,seats,photo FROM buses")
    buses = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT brand,fromloc,toloc,dateoft,price FROM routes, buses where routes.buses_id=buses.id")
    routes = cur.fetchall()
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT name,dateofbk,seatsbk,dateoft,fromloc,toloc,payment, brand FROM bookingsdet")
    bookings = cur.fetchall()
    cur.close()

    return render_template('reports.html', buses=buses, routes=routes, bookings=bookings)


@app.route('/updates')
@adlogin_required
def updates():
    # TODO
    flash('To be added successfully :) ', 'success')
    return redirect('/reports')


# Book Ticket
@app.route('/book_ticket', methods=['GET', 'POST'])
@login_required
def book_ticket():
    # Code for booking tickets
    if request.method == 'POST':
        routeid = request.form['trip']
        seats = request.form['seats']
        seatsbk = int(seats)
        payment = "NOTPAID"
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO booking(appuser_id,routes_id,seatsbk,payment,updatedby) VALUES(%s,%s,%s,%s,%s)",
                    (session['id'], routeid, seatsbk, payment, 1))
        mysql.connection.commit()
        flash('Ticket Booked, Check your email for payment details via Crypto')
        return redirect('/dashboard')

    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT routeid,fromloc,toloc,dateoft,brand,price FROM trips")
        trips = cur.fetchall()
        cur.close()
        return render_template('book_tickets.html', trips=trips)


# Cancel Ticket
@app.route('/cancel_ticket', methods=['GET', 'POST'])
@login_required
def cancel_ticket():
    # Code for canceling tickets
    if request.method == 'POST':
        tripid = request.form['tripid']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM booking WHERE id = %s", [tripid])
        booking = cur.fetchone()
        cur.close
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO bkinghistory(appuser_id,routes_id,seatsbk,payment,dateofbk,status,updatedby) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                    (session['id'], booking[2], booking[3], booking[5], booking[4], "Cancelled", 1))
        mysql.connection.commit()
        cur.close
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM booking WHERE id = %s", [tripid])
        mysql.connection.commit()
        flash('Ticket Canelled')
        return redirect('/dashboard')

    else:
        userid = session['id']
        cur = mysql.connection.cursor()
        cur.execute("SELECT bkid,fromloc,toloc,dateoft,dateofbk,seatsbk FROM bookingsdet WHERE appuid = %s", [userid])
        bookings = cur.fetchall()
        print(bookings)
        cur.close()
        return render_template('cancel_tickets.html', mybookings=bookings)


# Cancel Ticket

@app.route('/history')
@login_required
def history():
    # Code for canceling tickets
    userid = session['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT bkid,fromloc,toloc,dateoft,dateofbk,seatsbk FROM bookingsdet WHERE appuid = %s", [userid])
    bookings = cur.fetchall()
    print(bookings)
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT fromloc,toloc,dateofbk,seatsbk,payment,status,dateofupd FROM bkhistoryview WHERE appuid = %s", [userid])
    myhistory = cur.fetchall()
    print(bookings)
    cur.close()
    return render_template('history.html', mybookings=bookings, mybookingshist=myhistory)


if __name__ == '__main__':
    app.run(debug=True)

