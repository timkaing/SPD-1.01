def dec_to_bin(number):
    """Compute the binary representation of a positive decimal integer."""
    rep = ""
    while number >= 1:
        rep = str(number % 2) + rep
        number = number // 2
    return rep