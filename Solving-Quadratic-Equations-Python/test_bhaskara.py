import pytest

def solve_equation(a,b,c):
    import math
    delta=(b**2)-4*a*c
    if delta<0:
        return 0
    elif delta==0:
        x=-b/2*a
        return 1, x
    elif delta>0:
        x1=(-b+(math.sqrt(delta)))/(2*a)
        x2=(-b-(math.sqrt(delta)))/(2*a)
        if x1<=x2:
            return 2, x1, x2
        else:
            return 2, x2, x1

def test_solve_equation():
    assert solve_equation(2,2,4) == 0

@pytest.mark.parametrize("a,b,c,num_roots,root1,root2", [
    (1, 2, -15, 2, -5, 3),
    (1, -1, -1, 2, -0.6180339887498949, 1.618033988749895),
    (9, -5, 0, 2, 0, 0.5555555555555556),
    (4, 0, -16, 2, -2, 2)
    ])

def test_solve_equation(a,b,c,num_roots,root1,root2):
    assert solve_equation(a,b,c) == (num_roots, root1, root2)
