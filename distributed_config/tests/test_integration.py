import pytest
from src.config_manager import ConfigManager
from src.node import Node

@pytest.fixture
def nodes():
    return [Node(i, is_active=i % 2 == 0) for i in range(5)]

@pytest.fixture
def config_manager(nodes):
    return ConfigManager(nodes)

def test_integration_flow(config_manager, tmp_path, caplog):
    config_file = tmp_path / "config.json"
    config_file.write_text('{"memory_limit": 1024, "cpu_limit": 2.0}')
    config = config_manager.load_config(str(config_file))

    assert config_manager.validate_config(config) is True

    with caplog.at_level("INFO"):
        config_manager.propagate_config(config)

    assert "Configuration applied successfully." in caplog.text
    assert any("Node" in message for message in caplog.messages)
