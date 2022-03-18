from _app.config.connection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( username , email , created_at, updated_at ) VALUES ( %(username)s, %(email)s , NOW() , NOW() );"
        return connectToMySQL('esquema_nombre_usuario').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('esquema_nombre_usuario').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append(usuario)
        return usuarios