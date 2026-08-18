from src.math_operations import add, subtract

def test_add():
    assert add(2,3) == 5
    assert add(4,5) == 9
    assert add(6,24) == 30
    
def test_sub():
    assert subtract(5,4) == 1
    assert subtract(10,3) == 7
    assert subtract(20,5) == 15


