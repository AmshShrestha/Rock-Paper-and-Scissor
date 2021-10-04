import pytest

@pytest.mark.parametrize("username, password", [("admin", "admin"), ("admin", "ram")])
def test_method(username, password):
    assert username==password
