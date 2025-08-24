from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user
from models import User

def register_routes(app, db, bcrypt):
    @app.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            user = User.query.filter(User.username == username).first()

            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return "login succesful"

            else:
                flash("Incorrect Username or Password", "failed")
                return redirect(url_for('login'))


    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            hashed_password = bcrypt.generate_password_hash(password)

            user = User(username=username, password=hashed_password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))

        else:
            flash("Signup Failed")
            return redirect(url_for('signup'))

