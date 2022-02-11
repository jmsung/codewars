

def sign(n):
    """ Return sign 1 (n >= 0) or -1 (n < 0) """

    if not (isinstance(n, float) or isinstance(n, int)):
        raise ValueError("Input must be real number.")

    import math
    return math.copysign(1, n)


def num2lst(n):
    """ Convert from a multiple digit number to a list of single digit """
    return [int(i) if n > 0 else -int(i) for i in str(abs(n))]


def lst2num(lst):
    """ Convert from a list of single digits to a multiple digit number """

    # check all the element have the same sign
    if not all(sign(element) == sign(lst[0])
               for element in lst if element != 0):
        raise ValueError("All the element in lst must have the same sign.")

    num = int("".join([str(abs(i)) for i in lst]))
    return num if sign(lst[0]) > 0 else -num


def list_same_digit(n):
    """ Return the sorted list of the same digits from the input number

    Parameters
    ----------
    n (int): An int number

    Return
    ------
    digits (list of int): combination of digits """
    pass


def sum_squared(x):
    """ Return the sum of the squared elements
    
    Parameters
    ----------
    x (list): List of numbers

    Return
    ------
    ss (float): sum of the squared """    
    
    ss = sum(map(lambda i : i * i, x))
    # ss = sum([i**2 for i in x])
    return ss
    
    
    
    