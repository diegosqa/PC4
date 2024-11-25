import logging

def setup_logger(name):
    """
    Configura un logger con el nombre del módulo, niveles de logging y formato estándar.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Handler para la consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Formato para los logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Añadir handler al logger
    if not logger.handlers:
        logger.addHandler(console_handler)
    
    # Evitar duplicados en los logs
    logger.propagate = False

    return logger

