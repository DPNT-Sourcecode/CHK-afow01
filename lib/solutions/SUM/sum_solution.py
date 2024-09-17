# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x < 0 or x > 100:
        raise ValueError("x should be between 0 and 100")
    if y < 0 or y > 100:
        raise ValueError("y should be between 0 and 100")
    return x + y
