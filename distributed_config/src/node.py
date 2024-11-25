from .logger import Logger

class Node:
    def __init__(self, node_id, is_active=True):
        self.id = node_id
        self.is_active = is_active
        self.logger = Logger()

    def apply_config(self, config):
        try:
            # Simulate applying configuration
            self.logger.info(f"Node {self.id}: Configuration applied successfully.")
        except Exception as e:
            self.logger.error(f"Node {self.id}: Failed to apply configuration - {e}")
