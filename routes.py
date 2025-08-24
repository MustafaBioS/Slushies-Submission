from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

def register_routes(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('index.html')
        if request.method == 'POST':
            pass

    def signUp():
        if request.method == 'GET':
            return render_template('signup.html')
        if request.method == 'POST':
            pass

