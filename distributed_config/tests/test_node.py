from src.node import Node

def test_node_active():
    node = Node(1, is_active=True)
    config = {"memory_limit": 1024, "cpu_limit": 2.0}

    assert node.is_active is True
    node.apply_config(config)

def test_node_inactive(caplog):
    node = Node(2, is_active=False)
    config = {"memory_limit": 1024, "cpu_limit": 2.0}

    with caplog.at_level("WARNING"):
        node.apply_config(config)

    assert f"Node {node.id}: Configuration applied successfully." not in caplog.text
