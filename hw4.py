"""Homework 4: Non-local assignment and local state."""

"""1) An accumulator is a procedure that is called repeatedly with a single
numeric argument and accumulates its arguments into a sum. Each time it is
called, it returns the currently accumulated sum. Without using any lists or
dictionaries, write a function make_accumulator that returns accumulators, each
of which maintains an independent sum. The argument of make_accumulator should
specify the initial value of the sum for the returned accumulator.
"""

def make_accumulator(total):
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator(5)
    >>> acc(10)
    15
    >>> acc(10)
    25
    """
    
    def accumulator(val):
        nonlocal total
        total=val+total
        return total
    return accumulator

"""2) When testing software, it can be useful to count the number of times that
a function is called.  Without using any lists or dictionaries, define a
higher-order function count_calls that returns two functions:

  - a counted version of the original function that counts the number of times
    it has been called
  
  - a function of zero arguments that returns the number of times that the
    counted function is called
"""

def count_calls(f):
    """A decorator that returns a version of f that counts calls to f and can
    report that count to how_many_calls.

    
    >>> from operator import add
    >>> counted_add, add_count = count_calls(add)
    >>> add_count()
    0
    >>> counted_add(1, 2)
    3
    >>> add_count()
    1
    >>> add(3, 4)  # Doesn't count
    7
    >>> add_count()
    1
    >>> counted_add(5, 6)
    11
    >>> add_count()
    2
    """
    n=0
    
    def counted_f(*args):
        nonlocal n
        n=n+1
        return f(*args)
    def f_count():
        return n
    return counted_f,f_count

"""3) When we defined the evaluation procedure for call expressions, we said
that the first step in evaluating an expression is to evaluate its operator and
operand subexpressions. We never specified the order in which the operand
subexpressions should be evaluated (e.g., left to right or right to left). In
Python, operands are evaluated from left to right. With non-local assignment,
this order matters.

Define get_f, which returns a function f such that evaluating add(f(0), f(1))
will return 0 if operand expressions are evaluated from left to right, but will
return 1 if they were evaluated right to left.
"""

def get_f():
    """Returns a function that takes and returns one numeric argument.

    >>> from operator import add

    >>> f = get_f()
    >>> add(f(0), f(1))
    0

    >>> f = get_f()
    >>> add(f(1), f(0))
    1
    """
    "*** YOUR CODE HERE ***"
    k=1
    def f(val):
        nonlocal k
        k=k*val
        return k
    return f
        


"""4) Write a version of make_withdraw that returns password-protected account
functions.  That is, make_withdraw should take a password argument (a string) in
addition to an initial balance.  The returned function should take two
arguments: an amount to withdraw and a password.  

A password-protected withdraw function should only process withdrawals that
include a password that matches the original.  Upon receiving an incorrect
password, the function should:

  1) Store that incorrect password in a list, and

  2) Return the string 'Incorrect password'.
  
If a withdraw function has been called three times with incorrect passwords
p1, p2, and p3, then it is locked.  The function should return:

  "Your account is locked. Attempts: [<p1>, <p2>, <p3>]"

All future calls to the function should return this same message.
"""

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"
    pwdlist=[]
    n=0
    def withdraw(amount,pwd):

        nonlocal balance,n,pwdlist
        if n>=3:
            return "Your account is locked. Attempts: ['"+pwdlist[0]+"', '"+pwdlist[1]+"', '"+pwdlist[2]+"']"

        if pwd==password:
            if amount>balance:
                return 'Insufficient funds'
            balance=balance-amount
            return balance
        else:
            n=n+1
            pwdlist=pwdlist+[pwd]
            return 'Incorrect password'

    return withdraw
                
                        
"""5) Suppose that our banking system requires the ability to make joint
accounts.  Define a function make_joint that takes three arguments.  

  - A password-protected withdraw function

  - The password with which that withdraw function was defined 

  - A new password that can also access the original account
  
The make_joint function returns a withdraw function that provides additional
access to the original account using *either* the new or old password.  Both
functions draw down the same balance. Incorrect passwords provided to either
function will be stored and cause the functions to be locked after three wrong
attempts.

Hint: The solution is short (less than 10 lines) and contains no string
literals!  The key is to call withdraw with the right password and interpret the
result.  The following construction may prove useful in detecting errors:

result = 'hello'
if type(result) == str:
    print(result)
""" 

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    
    def joint(amount,pwd):

        if pwd==new_password:
            pwd=old_password
        return withdraw(amount, pwd)
        
    op=withdraw(0, old_password)
    if type(op)!=str:
        return joint
    else:
        return op


