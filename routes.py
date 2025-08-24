from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required, login_user, current_user
import sqlalchemy
from models import User
from models import Task

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
                return redirect(url_for('tasks'))

            else:
                flash("Incorrect Username or Password", "flash")
                return redirect(url_for('login'))


    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        if request.method == 'POST':

            username = request.form.get('username')
            password = request.form.get('password')

            try:

                hashed_password = bcrypt.generate_password_hash(password)

                user = User(username=username, password=hashed_password)

                db.session.add(user)
                db.session.commit()

                flash("Account Created Succesfully", "flash")
                return redirect(url_for('login'))
            
            except sqlalchemy.exc.IntegrityError:
                flash("Username Already Taken")
                return redirect((url_for('signup')))

        else:
            flash("Signup Failed", "flash")
            return redirect(url_for('signup'))

    @app.route('/addtask', methods=['GET', 'POST'])
    @login_required
    def addtask():
        if request.method == 'GET':
            return render_template('add.html')
        
        if request.method == 'POST':

            task_content = request.form.get('task')

            new_task = Task(content=task_content, user_id=current_user.id)

            db.session.add(new_task)
            db.session.commit()

            flash("Task Added Successfully", "flash")
            return redirect(url_for('tasks'))
        
        else:
            flash("Failed To Add Task", 'flash')
            return redirect(url_for('tasks'))

    @app.route('/tasks')
    @login_required
    def tasks():
        tasks = Task.query.filter_by(user_id=current_user.id).all()
        return render_template('index.html', tasks=tasks)
    
    @app.route('/delete/<int:task_id>', methods=['POST'])
    @login_required
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)

        db.session.delete(task)
        db.session.commit()
        flash("Task Deleted Successfully", 'flash')
        return redirect(url_for('tasks'))