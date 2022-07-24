from .gaussian_elimination_3 import echelon

def test_echelon_form():
    a = [
        [2, 4, 0],
        [-3, 6, 2]
    ]
    res = echelon(a)
    assert res[1] == [0, 12, 2] 
    