import math


def round_up(num, decimals=0):
    """
    rounds up a number upto the decimal point provided e.g. round_up(1.345, 2) = 1.35
    ---
    Params:
        num: a number
        decimals: decimal point to apply rounding.
    ---
    Returns:
        rounded number
    """
    decimal_multiplier = 10 ** decimals
    rounded_value = math.ceil(num * decimal_multiplier)/decimal_multiplier
    return rounded_value

