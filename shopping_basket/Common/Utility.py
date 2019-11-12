import math

def round_up(num, decimals=0):
    decimal_multiplier = 10 ** decimals
    rounded_value = math.ceil(num * decimal_multiplier)/decimal_multiplier
    return rounded_value