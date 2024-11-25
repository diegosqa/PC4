from flask import Flask, request, jsonify
from user_management.src.UserService import UserService
from user_management.logger_config import setup_logger


app = Flask(__name__)
logger = setup_logger('user_management')

@app.route('/users', methods=['GET'])
def get_users():
    try:
        logger.debug("Solicitud para obtener todos los usuarios recibida.")
        users = UserService().get_all_users()
        logger.info(f"Se obtuvieron {len(users)} usuarios exitosamente.")
        return jsonify(users), 200
    except Exception as e:
        logger.error(f"Error al obtener usuarios: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/users', methods=['POST'])
def add_user():
    try:
        user_data = request.get_json()
        logger.debug(f"Solicitud para agregar usuario con datos: {user_data}")
        user_id = UserService().add_user(user_data)
        logger.info(f"Usuario agregado exitosamente con ID: {user_id}")
        return jsonify({"message": "Usuario agregado", "user_id": user_id}), 201
    except Exception as e:
        logger.error(f"Error al agregar usuario: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        logger.debug(f"Solicitud para obtener usuario con ID: {user_id}")
        user = UserService().get_user_by_id(user_id)
        if user:
            logger.info(f"Usuario con ID {user_id} encontrado.")
            return jsonify(user), 200
        else:
            logger.warning(f"Usuario con ID {user_id} no encontrado.")
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        logger.error(f"Error al obtener usuario: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_data = request.get_json()
        logger.debug(f"Solicitud para actualizar usuario con ID {user_id} con datos: {user_data}")
        updated = UserService().update_user(user_id, user_data)
        if updated:
            logger.info(f"Usuario con ID {user_id} actualizado exitosamente.")
            return jsonify({"message": "Usuario actualizado"}), 200
        else:
            logger.warning(f"Usuario con ID {user_id} no encontrado para actualización.")
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        logger.error(f"Error al actualizar usuario: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        logger.debug(f"Solicitud para eliminar usuario con ID {user_id}")
        deleted = UserService().delete_user(user_id)
        if deleted:
            logger.info(f"Usuario con ID {user_id} eliminado exitosamente.")
            return jsonify({"message": "Usuario eliminado"}), 200
        else:
            logger.warning(f"Usuario con ID {user_id} no encontrado para eliminación.")
            return jsonify({"error": "Usuario no encontrado"}), 404
    except Exception as e:
        logger.error(f"Error al eliminar usuario: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
