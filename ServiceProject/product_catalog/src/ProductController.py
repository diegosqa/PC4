from flask import Flask, request, jsonify
from product_catalog.src.ProductService import ProductService
from product_catalog.logger_config import setup_logger



app = Flask(__name__)
logger = setup_logger('product_catalog')

@app.route('/products', methods=['GET'])
def get_products():
    try:
        logger.debug("Solicitud para obtener todos los productos recibida.")
        products = ProductService().get_all_products()
        logger.info(f"Se obtuvieron {len(products)} productos exitosamente.")
        return jsonify(products), 200
    except Exception as e:
        logger.error(f"Error al obtener productos: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/products', methods=['POST'])
def add_product():
    try:
        product_data = request.get_json()
        logger.debug(f"Solicitud para agregar producto con datos: {product_data}")
        product_id = ProductService().add_product(product_data)
        logger.info(f"Producto agregado exitosamente con ID: {product_id}")
        return jsonify({"message": "Producto agregado", "product_id": product_id}), 201
    except Exception as e:
        logger.error(f"Error al agregar producto: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        logger.debug(f"Solicitud para obtener producto con ID: {product_id}")
        product = ProductService().get_product_by_id(product_id)
        if product:
            logger.info(f"Producto con ID {product_id} encontrado.")
            return jsonify(product), 200
        else:
            logger.warning(f"Producto con ID {product_id} no encontrado.")
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as e:
        logger.error(f"Error al obtener producto: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        product_data = request.get_json()
        logger.debug(f"Solicitud para actualizar producto con ID {product_id} con datos: {product_data}")
        updated = ProductService().update_product(product_id, product_data)
        if updated:
            logger.info(f"Producto con ID {product_id} actualizado exitosamente.")
            return jsonify({"message": "Producto actualizado"}), 200
        else:
            logger.warning(f"Producto con ID {product_id} no encontrado para actualización.")
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as e:
        logger.error(f"Error al actualizar producto: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        logger.debug(f"Solicitud para eliminar producto con ID {product_id}")
        deleted = ProductService().delete_product(product_id)
        if deleted:
            logger.info(f"Producto con ID {product_id} eliminado exitosamente.")
            return jsonify({"message": "Producto eliminado"}), 200
        else:
            logger.warning(f"Producto con ID {product_id} no encontrado para eliminación.")
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as e:
        logger.error(f"Error al eliminar producto: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)