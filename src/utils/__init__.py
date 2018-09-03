"""
This package contains all the util functions like printing list or preloading the datasets etc.
"""
def populate_list(ran):
    """
    Returns a list of random integers
    :param random number range:
    :return list:
    """
    import random as r
    my_randoms = []
    for i in range(ran):
        my_randoms.append(r.randrange(1, 10000, 1))
    return my_randoms
