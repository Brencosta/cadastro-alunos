from operacoes import soma
from operacoes import subtracao

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 1
    assert soma(0, 0) == 0