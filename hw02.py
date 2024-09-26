from operator import add, mul

square = lambda x: x * x        # def square(x): return x * x

identity = lambda x: x      # def identity(x): return x

triple = lambda x: 3 * x        # def triple(x): return 3 * x

increment = lambda x: x + 1     # def increment(x): return x + 1


HW_SOURCE_FILE=__file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    total, x = 0, 1
    while x <= n:
        total, x = total * term(x), x + 1
    return total

def product_identity(n):
    """Product the first N natural numbers
    >>> product_identity(5)
    120
    """
    return product(n, identity)
        
def product_square(n):
    """Product the first N squares of natural numbers
    >>> product_square(3)
    36
    """
    return product(n, square) 
    
def product_triple(n):
    """Product the first N triples of natural numbers
    >>> product_triple(3)
    162"""
    return product(n, triple)
    
def product_increment(n):
    """Product the first N increment of natual numbers
    >>>product_increment(3)
    24"""
    return product(n, increment)


def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)        # def increment(x, y): return x + y + 1
    19
    """
    # fuse(total, term(x)) == add(total, term(x)) or mul(total, term(x))        This line doesn’t serve a purpose here. The actual fusion happens inside the while loop via the fuse function.
    total, x = start, 1 
    while x <= n:
        total, x = fuse(total, term(x)), x + 1
    return total

# def fuse(total, term(x)):
#     return add(total, term(x)), mul(total, term(x))

def accu_identity(fuse, start, n):
    """accumulate the first N natural numbers.
    >>>accu_identity(add, 0, 5)
    15"""
    # total, x = start, 1
    # while x <= n:
    #     total, x = fuse(total, x), x + 1
    return accumulate(fuse, start, n, identity)

def accu_square(fuse, start, n):
    """accumulate the first N squares of natural numbers
    >>>accu_square(mul, 2, 3)
    72"""
    # total, x = start, 1
    # while x <= n:
    #     total, x = fuse(total, x * x), x + 1
    return accumulate(fuse, start, n, square)

def accu_triple(fuse, start, n):
    """accumulate the first N triples of natural numbers
    """
    # total, x = start, 1
    # while x <= n:
    #     total, x = fuse(total, 3 * x), x + 1
    return accumulate(fuse, start, n, triple)

def accu_increment(fuse, start, n):
    """accumulate the first N increment of natural numbers
    """
    # total, x = start, 1
    # while x <= n:
    #     total, x = fuse(total, x + 1), x + 1 
    return accumulate(fuse, start, n, increment)


def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square) # square(1) + square(2) + ... + square(4) + square(5)
    55
    >>> summation_using_accumulate(5, triple) # triple(1) + triple(2) + ... + triple(4) + triple(5)
    45
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square) # square(1) * square(2) * square(3) * square()
    576
    >>> product_using_accumulate(6, triple) # triple(1) * triple(2) * ... * triple(5) * triple(6)
    524880
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n, term)


def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    "*** YOUR CODE HERE ***"

