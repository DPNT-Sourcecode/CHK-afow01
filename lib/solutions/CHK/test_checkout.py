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


def test_checkout_with_E():
    num = checkout("AABCDE")
    expected = 50 + 50 + 30 + 20 + 15 + 40
    assert num == expected


def test_E_offer():
    num = checkout("AABADEE")
    expected = 130 + 15 + 80
    assert num == expected


def test_As():
    num = checkout("AAAAEAAAE")
    expected = 380
    assert num == expected


def test_EEEB():
    num = checkout("EEEB")
    expected = 120
    assert num == expected


def test_ABCDEABCDE():
    import pdb;pdb.set_trace()  # fmt: skip
    num = checkout("ABCDEABCDE")
    expected = 280
    assert num == expected


