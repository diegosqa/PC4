import pytest
from src.config_manager import ConfigManager
from src.node import Node

@pytest.fixture
def nodes():
    return [Node(i, is_active=True) for i in range(3)]

@pytest.fixture
def config_manager(nodes):
    return ConfigManager(nodes)

def test_load_config(config_manager, tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text('{"memory_limit": 1024, "cpu_limit": 2.0}')
    
    config = config_manager.load_config(str(config_file))
    assert config["memory_limit"] == 1024
    assert config["cpu_limit"] == 2.0

def test_validate_config_valid(config_manager):
    config = {"memory_limit": 1024, "cpu_limit": 2.0}
    assert config_manager.validate_config(config) is True

def test_validate_config_invalid_memory(config_manager):
    config = {"memory_limit": 128, "cpu_limit": 2.0}
    assert config_manager.validate_config(config) is False

def test_validate_config_invalid_cpu(config_manager):
    config = {"memory_limit": 1024, "cpu_limit": 40.0}
    assert config_manager.validate_config(config) is False

def test_propagate_config(config_manager, caplog):
    config = {"memory_limit": 1024, "cpu_limit": 2.0}

    with caplog.at_level("INFO"):
        config_manager.propagate_config(config)

    assert "Configuration applied successfully." in caplog.text
