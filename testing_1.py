import pytest

@pytest.mark.parametrize("username, password", [("user", "user"), ("user", "Amsh")])
def test_method(username, password):
    assert username==password
