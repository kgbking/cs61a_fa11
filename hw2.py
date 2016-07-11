def product(n, term):
    """Return the product of the first n terms in a sequence.
    
    term -- a function that takes one argument
    """
    total, k = 1, 1
    while k <= n:
        total, k = total*term(k), k+1
    return total

def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    """
    def term(x):
        return x
    return product(n, term)


    
def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence.
    
    *** For Summation, start=0
    *** For Production, start=1

    """
    total, k = start, 1
    while k <= n:
        total, k = combiner(total,term(k)), k+1
    return total

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate."""
    "*** YOUR CODE HERE ***"
    def combiner(total,term):
        return total+term
    return accumulate(combiner, 0, n, term)
        

def product_using_accumulate(n, term):
    """An implementation of product using accumulate."""
    "*** YOUR CODE HERE ***"
    def combiner(total,term):
        return total*term
    return accumulate(combiner, 1, n, term)

def double(f):
    """Return a function that applies f twice."""
    def h(x):
        return f(f(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of f.
    
    f -- a function that takes one argument
    n -- a positive integer
    1st repetition is function f itself
    >>> repeated(square, 2)(5)
    625
    """
    def compose(f, g):
        def h(x):
            return f(g(x))
        return h
    k,opf=1,f
    if n>1:
        while k<n:
            opf,k=compose(f,opf),k+1
    return opf
        
    
    
def zero(f):
    """Church numeral 0."""
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1."""
    "*** YOUR CODE HERE ***"
    return lambda x: f(x)

def two(f):
    """Church numeral 2."""
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n."""
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(f)(n(f)(x))

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.
    
    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(add_church(two, two))
    4
    """
    "*** YOUR CODE HERE ***"
    return n(lambda x: x+1)(0)

