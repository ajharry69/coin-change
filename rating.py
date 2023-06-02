import math


def get_ratings(rating):
    ratings = ["empty", "empty", "empty", "empty", "empty"]

    rating_as_float = float(rating)
    if rating_as_float <= 0:
        return " ".join(ratings)

    number_of_full_ratings = math.floor(rating_as_float)
    for index in range(0, number_of_full_ratings):
        ratings[index] = "full"

    unclassified_rating = rating_as_float - number_of_full_ratings
    if unclassified_rating <= 0.5:
        ratings[number_of_full_ratings] = "half"
    elif unclassified_rating > 0.5:
        ratings[number_of_full_ratings] = "full"

    return " ".join(ratings)


assert get_ratings("4.45") == "full full full full half"
assert get_ratings("4.5") == "full full full full half"
assert get_ratings("4.6") == "full full full full full"
assert get_ratings("0.38") == "half empty empty empty empty"
assert get_ratings("3.5") == "full full full half empty"
assert get_ratings("3.51") == "full full full full empty"
assert get_ratings("3.49") == "full full full half empty"
assert get_ratings("-1") == "empty empty empty empty empty"
assert get_ratings("0") == "empty empty empty empty empty"
