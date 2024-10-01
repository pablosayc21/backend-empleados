import sqlite3


conn = sqlite3.connect('empleados_departamentos.db')


cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS empleados")

cursor.execute("DROP TABLE IF EXISTS departamentos")

cursor.execute("""
               
    CREATE TABLE departamentos 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre TEXT NOT NULL)
               
""")

cursor.execute("""
               
    CREATE TABLE empleados 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    departamento_id INTEGER NOT NULL,
    fecha_contratacion DATE NOT NULL,
    cargo TEXT NOT NULL,
    FOREIGN KEY (departamento_id) REFERENCES departamentos (id))
               
""")

conn.commit()

conn.close()

print("Creación de base de datos exitosa.")