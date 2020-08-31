from extramath.sqrt import sqrt
from pytest import approx

def test_sqrt():
	assert sqrt(4.0) == approx(2.0)
