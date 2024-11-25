import argparse
from .config_manager import ConfigManager
from .node import Node

def main():
    parser = argparse.ArgumentParser(description="Distributed Configuration System")
    parser.add_argument('config_file', type=str, help="Path to the configuration file")
    args = parser.parse_args()

    # Simulate a cluster of nodes
    nodes = [Node(i, is_active=(i % 2 == 0)) for i in range(1, 6)]

    manager = ConfigManager(nodes)
    config = manager.load_config(args.config_file)

    if manager.validate_config(config):
        manager.propagate_config(config)
