from .checkout_solution import checkout


def test_checkout_basic():
    num = checkout("AABCD")
    expected = 50 + 50 + 30 + 20 + 15
    assert num == expected


def test_checkout_one_offer():
    num = checkout("AABAD")
    expected = 130 + 30 + 15
    assert num == expected


def test_checkout_all_offers():
    num = checkout("BDBAACA")
    expected = 45 + 15 + 130 + 20
    assert num == expected


def test_illegal():
    num = checkout("BBXA")
    assert num == -1



