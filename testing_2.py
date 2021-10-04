import pytest

@pytest.fixture
def tester():
    name="Amsh"
    contact=9801254332
    return[name,contact]

def testing_1(tester):
    first_name="amsh"
    assert tester[0]==first_name

def testing_2(tester):
    contact_num=9801254332
    assert tester[1]==contact_num
