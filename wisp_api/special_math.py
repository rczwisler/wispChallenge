'''
Module to computer special math:
    f(n) = n + f(n-1) + f(n-2)
and provide a Blueprint for a Flask app with endpoint(s):
    /specialMath/<int>

Functions:
    special_math_get(str)
    special_math_memoize(int)
    special_math_iterative(int)
'''
from flask import Blueprint

bp = Blueprint("specialMath", __name__)

@bp.route("/specialMath/<value>", methods=["Get"])
def special_math_get(value):
    '''
    Take input from endpoint, convert to int and pass to special math solver

    Parameters:
        value(str): input from HTTP endpoint

    Returns:
        result(str): result of special math solver
    '''
    try:
        result = special_math_iterative(int(value))
        return str(result)
    except (ValueError, TypeError):
        return "Invalid input value. Must be a positive whole integer", 400

def special_math_memoize(value, memoize = None):
    '''
    Recursive special math solver with memoization

    Parameters:
        value(int): Input value to evaluate
        memoize(dict): Dictionary of previously calculated values

    Returns:
        result(int): Result of special math f(n) = n + f(n-1) + f(n-2)
    '''
    if memoize is None:
        memoize = {}
    if value in memoize:
        return memoize[value]
    if value == 0:
        return value
    if value == 1:
        return value
    result = value + special_math_memoize(value-1, memoize) + special_math_memoize(value-2, memoize)
    memoize[value] = result
    return result

def special_math_iterative(value):
    '''
    Iterative special math solver.
    f(n) = n + f(n-1) + f(n-2) = fibonacci(n+4) - (3+n)
    credit/source of formula at https://oeis.org/A001924

    Parameters:
        value(int): Input value to evaluate

    Returns:
        result(int): Result of special math fibonacci(n+4) - (3+n)
    '''
    if value < 0:
        raise ValueError
    result = _fibonacci(value+4) - (3+value)
    return result

def _fibonacci(value):
    '''
    Return the Nth fibonacci value

    Parameters:
        value(int): N to look up

    Returns:
        fib_a(int): the Nth fibonacci value
    '''
    fib_a,fib_b = 0,1
    for _ in range(value):
        fib_a,fib_b = fib_b,fib_a + fib_b
    return fib_a
