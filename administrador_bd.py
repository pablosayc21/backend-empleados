import sqlite3
from flask import g

DATABASE = 'empleados_departamentos.db'

def obtener_bd():
    """
    Crea una nueva conexión si no existe dentro del contexto de la aplicación. 
    Se espera que el archivo .db ya este creado.
    """
    if 'db' not in g:

        g.db = sqlite3.connect(DATABASE)

        g.db.row_factory = sqlite3.Row  

    return g.db

def close_db(e=None):
    """
    Cierra la conexión a la base de datos.
    """
    db = g.pop('db', None)

    if db is not None:

        db.close()

def inicializar_app(app):
    """
    Registra las funciones de la base de datos en la aplicación.
    """
    app.teardown_appcontext(close_db)
    with app.app_context():
        obtener_bd()