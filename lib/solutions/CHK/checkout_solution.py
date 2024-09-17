from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # presumably deliminated by commas
    skus = Counter(list(skus))

    # I guess this would be a DB in the real world
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    special_offers = {"A": [(5, 200), (3, 130)], "B": [(2, 45)], "E": [(2, 40)]}

    total = 0

    for sku, number in skus.items():
        rrp = prices.get(sku)

        # no illegal characters allowed
        if not rrp:
            return -1

        # create as a separate function
        if offers := special_offers.get(sku):
            for offer in offers:
                required_for_offer, special_price = offer
                while number >= required_for_offer:
                    number -= required_for_offer
                    total += special_price

        if number > 0:
            total += number * rrp

    return total


