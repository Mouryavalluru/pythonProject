from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI'] = 'your-mongodb-uri'
app.secret_key = 'your-secret-key'

mongo = PyMongo(app)

# Define user roles (you can extend this as needed)
USER_ROLES = {'farmer', 'administrator', 'staff'}

@app.route('/')
def home():
    if 'username' in session:
        return f'Hello {session["username"]}! You are logged in as {session["role"]}'
    return 'Welcome to the Agricultural Products Rural Entrepreneurship Management System'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        # Check if the username is already taken
        if mongo.db.users.find_one({'username': username}):
            return 'Username already exists. Please choose another one.'

        hashed_password = generate_password_hash(password, method='sha256')

        # Insert the new user into the database
        mongo.db.users.insert({'username': username, 'password': hashed_password, 'role': role})

        return 'Registration successful!'

    return render_template('register.html', roles=USER_ROLES)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = mongo.db.users.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('home'))

        return 'Invalid username or password'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
