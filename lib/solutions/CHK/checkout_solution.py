
from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # presumably deliminated by commas
    skus = Counter(skus.split(","))

    # I guess this would be a DB in the real world
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    special_offers = {"A": (3, 130), "B": (2, 45)}

    total = 0

    for sku, number in skus.items():
        if offer := special_offers.get(sku):
            required_for_offer, special_price = offer
            if number >= required_for_offer:




