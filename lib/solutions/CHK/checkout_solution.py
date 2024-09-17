# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # presumably deliminated by commas
    skus = skus.split(",")

    # I guess this would be a DB in the real world
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    special_offers = {"A": (3, 130), "B": (2, 45)}

