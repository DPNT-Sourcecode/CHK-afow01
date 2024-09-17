from .checkout_solution import checkout


def test_checkout_basic():
    num = checkout("A,A,B,C,D")
    expected = 50 + 50 + 30 + 20 + 15
    assert num == expected


def test_checkout_one_offer():
    num = checkout("A,A,B,A,D")
    expected = 130 + 30 + 15
    assert num == expected

