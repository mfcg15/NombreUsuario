from flask import render_template, request,jsonify
from _app.config.connection import connectToMySQL
from _app.models.usuario import Usuario
from _app import app
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
    all_usuarios = Usuario.get_all()
    return render_template('index.html', all_usuarios = all_usuarios)

@app.route('/create_usuario', methods=["POST"])
def create_user():
    if len(request.form['username'])<2:
        return jsonify(message="User name must be at least 2 characters")

    if len(request.form['email'])==0:
         return jsonify(message="Enter an email")

    if not EMAIL_REGEX.match(request.form['email']):
         return jsonify(message="Invalid Email")
    
    data = {
        "username": request.form["username"],
        "email" : request.form["email"]
        }
    
    query = "SELECT * FROM usuarios WHERE email = %(email)s;"
    results = connectToMySQL('esquema_nombre_usuario').query_db(query,data)
    if len(results) >= 1:
        return jsonify(message="Email already exists!")

    Usuario.save(data)
    return jsonify(message="Add a user!!!")
