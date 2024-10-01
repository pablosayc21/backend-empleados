from flask import Flask, request, jsonify
from flask_restx import Api, Resource
import administrador_bd
from datetime import datetime
import logging
logging.basicConfig(level=logging.ERROR)

app = Flask(__name__)
api = Api(app)
administrador_bd.inicializar_app(app)

def validar_fecha(fecha_str):

    try:

        datetime.strptime(fecha_str, '%d-%m-%Y')

        return True
    
    except ValueError:

        return False

#Ruta extra para la administracion de los deparamentos. 
@api.route('/api/departamentos')
class RecursoDepartamento(Resource):

    def get(self):

        """Obtiene todos los departamentos"""

        try:

            db = administrador_bd.obtener_bd()

            if db is None:

                return {"message": "Error al conectar a la base de datos."}, 500

            departamentos = db.execute('SELECT * FROM departamentos').fetchall()

            diccionario_departamentos = [dict(dep) for dep in departamentos]

            return jsonify({'departamentos':diccionario_departamentos})
            
        except Exception as e:

            logging.error(f"Error en el servidor: {e}")
            
            return {"message": "Error interno del servidor."}, 500

    def post(self):

        if not request.is_json:

            return {"message": "El contenido del request no es JSON"}, 400
        
        datos = request.json

        if 'nombre' not in datos :

            return {"message": "Todos los campos son obligatorios: nombre de departamento"}, 400
        
        try:

            db = administrador_bd.obtener_bd()

            if db is None:
                
                return {"message": "Error al conectar a la base de datos."}, 50

            db.execute( 'INSERT INTO departamentos (nombre) VALUES (?)', (datos['nombre'],))

            db.commit()

            return {"message": "Departamento agregado"}, 201

        except Exception as e:

            logging.error(f"Error en el servidor: {e}")
            
            return {"message": "Error interno del servidor."}, 500
        
@api.route('/api/empleados')
class RecursoEmpleado(Resource):

    def get(self):

        """Obtiene todos los empleados."""

        try:

            db = administrador_bd.obtener_bd()

            if db is None:
                
                return {"message": "Error al conectar a la base de datos."}, 50

            empleados = db.execute('SELECT * FROM empleados').fetchall()

            diccionario_empleados = [dict(emp) for emp in empleados]

            return jsonify({"empleados": diccionario_empleados})

        except Exception as e:

            logging.error(f"Error en el servidor: {e}")

            return {"message": "Error interno del servidor."}, 500

    def post(self):

        """Agrega un nuevo empleado."""

        if not request.is_json:

            return {"message": "El contenido del request no es JSON"}, 400

        datos = request.json

        campos_obligatorios = ['nombre', 'departamento_id', 'apellido', 'fecha_contratacion', 'cargo']

        if not all(campo in datos for campo in campos_obligatorios):

            return {"message": "Todos los campos son obligatorios: " + ", ".join(campos_obligatorios)}, 400

        try:

            db = administrador_bd.obtener_bd()

            if db is None:
                
                return {"message": "Error al conectar a la base de datos."}, 50

            departamento = db.execute('SELECT * FROM departamentos WHERE id = ?',(datos['departamento_id'],)).fetchone()

            if departamento is None:

                return {"message": "El departamento_id especificado no existe."}, 404
            
            if not validar_fecha(datos['fecha_contratacion']):

                return {"message": "El campo fecha_contratacion debe estar en formato YYYY-MM-DD."}, 400


            db.execute(
                'INSERT INTO empleados (nombre, apellido, departamento_id, fecha_contratacion, cargo) VALUES (?, ?, ?, ?, ?)',
                (datos['nombre'], datos['apellido'], datos['departamento_id'], datos['fecha_contratacion'], datos['cargo'])
            )

            db.commit()
            
            return {"message": "Empleado agregado"}, 201
    
        except Exception as e:

            logging.error(f"Error en el servidor: {e}")
            
            return {"message": "Error interno del servidor."}, 500

@api.route('/api/empleados/<int:id>')
class RecursoEmpleadoPorId(Resource):

    def put(self, id):
        """Actualiza la información de un empleado."""

        if not request.is_json:

            return {"message": "El contenido del request no es JSON"}, 400
        
        datos = request.json

        campos_obligatorios = ['nombre', 'departamento_id', 'apellido', 'fecha_contratacion', 'cargo']

        if not all(campo in datos for campo in campos_obligatorios):

            return {"message": "Todos los campos son obligatorios: " + ", ".join(campos_obligatorios)}, 400
        
        try:

            db = administrador_bd.obtener_bd()

            if db is None:
                
                return {"message": "Error al conectar a la base de datos."}, 50

            empleado = db.execute('SELECT * FROM empleados WHERE id = ?', (id,)).fetchone()

            if empleado is None:

                return {"message": "Empleado no encontrado."}, 404
            
            departamento = db.execute('SELECT * FROM departamentos WHERE id = ?',(datos['departamento_id'],)).fetchone()

            if departamento is None:

                return {"message": "El departamento_id especificado no existe."}, 404
            
            db.execute(
                'UPDATE empleados SET nombre = ?, apellido = ?, departamento_id = ?, fecha_contratacion = ?, cargo = ? WHERE id = ?',
                (datos['nombre'], datos['apellido'], datos['departamento_id'], datos['fecha_contratacion'], datos['cargo'], id)
            )

            db.commit()

            return {"message": "Empleado actualizado"}, 200

        except Exception as e:

            logging.error(f"Error en el servidor: {e}")
            
            return {"message": "Error interno del servidor."}, 500

    def delete(self, id):

        """Elimina un empleado por su id"""

        try:


            db = administrador_bd.obtener_bd()

            if db is None:
                
                return {"message": "Error al conectar a la base de datos."}, 50

            empleado = db.execute('SELECT * FROM empleados WHERE id = ?', (id,)).fetchone()

            if empleado is None:

                return {"message": "Empleado no encontrado."}, 404
            
            db.execute('DELETE FROM empleados WHERE id = ?', (id,))

            db.commit()

            return {"message": "Empleado eliminado."}, 200

        except Exception as e:

            logging.error(f"Error en el servidor: {e}")
            
            return {"message": "Error interno del servidor."}, 500

if __name__ == '__main__':
    app.run(debug=True)