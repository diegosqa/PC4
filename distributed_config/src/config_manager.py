import json
from .logger import Logger
from .node import Node

class ConfigManager:
    REQUIRED_KEYS = ['memory_limit', 'cpu_limit']

    def __init__(self, nodes):
        self.nodes = nodes
        self.logger = Logger()

    def load_config(self, filepath):
        try:
            with open(filepath, 'r') as file:
                config = json.load(file)
                self.logger.info(f"Configuration loaded from {filepath}")
                return config
        except Exception as e:
            self.logger.error(f"Error loading configuration: {e}")
            raise

    def validate_config(self, config):
        for key in self.REQUIRED_KEYS:
            if key not in config:
                self.logger.error(f"Missing required key: {key}")
                return False
        if not (256 <= config['memory_limit'] <= 64000):
            self.logger.error("Invalid memory_limit value")
            return False
        if not (0.5 <= config['cpu_limit'] <= 32):
            self.logger.error("Invalid cpu_limit value")
            return False
        self.logger.info("Configuration is valid")
        return True

    def propagate_config(self, config):
        for node in self.nodes:
            if node.is_active:
                node.apply_config(config)
            else:
                self.logger.warning(f"Node {node.id} is inactive. Skipping.")
