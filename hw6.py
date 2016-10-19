"""Homework 6: Object-oriented programming"""

"""1) Create a class called VendingMachine that represents a vending machine
for some product. A VendingMachine object doesn't actually return anything but
strings describing its interactions.  See the doctest for examples.
    
In Nanjing, there are even vending machines for crabs:
http://www.youtube.com/watch?v=5Mwv90m3N2Y
"""
class VendingMachine(object):
    """A vending machine that vends some product for some price.
    
    >>> v = VendingMachine('iPod', 100)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current iPod stock: 2'
    >>> v.vend()
    'You must deposit $100 more.'
    >>> v.deposit(70)
    'Current balance: $70'
    >>> v.vend()
    'You must deposit $30 more.'
    >>> v.deposit(50)
    'Current balance: $120'
    >>> v.vend()
    'Here is your iPod and $20 change.'
    >>> v.deposit(100)
    'Current balance: $100'
    >>> v.vend()
    'Here is your iPod.'
    >>> v.deposit(150)
    'Machine is out of stock. Here is your $150.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, vending_product, vending_price):
        self.product=vending_product
        self.price=vending_price
        self.stock=0
        self.balance=0
        self.change=0
    def restock(self, stk):
        self.stock+=stk
        print('Current {} stock: {}'.format(self.product,self.stock))
    def deposit(self, bal):
        if self.stock>0:
            self.balance+=bal
            print('Current balance: ${}'.format(self.balance))
        else:
            print('Machine is out of stock. Here is your ${}.'.format(bal))    
    def vend(self):
        if self.stock>0:
            if self.balance>self.price:
                self.change=self.balance-self.price
                self.balance=0
                print('Here is your {} and ${} change.'.format(self.product,self.change))
            elif self.balance==self.price:
                self.balance,self.stock=0,0
                print('Here is your {}.'.format(self.product))
            else:
                print('You must deposit ${} more.'.format(self.price-self.balance))
        else:
            print('Machine is out of stock.')
        

"""2) Create a class called MissManners that promotes politeness among our
objects. A MissManners object takes another object on construction.  It has one
method, called ask.  It responds by calling methods on the object it contains,
but only if the caller said please.  The doctest gives an example.

Hint: Your implementation will need to use the *args notation that allows
functions to take a flexible number of variables.
"""

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please.'
    >>> m.ask('please give up a teaspoon')
    'Thanks for asking, but I know not how to give up a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, se_obj):
        self.obj=se_obj
    def ask(self,*args):
        if type(args[0]) is type('s'):
            text=args[0].split()
            if 'please' in text:
                text.remove('please')
                if len(args)==1 and text[0]=='vend' :
                    self.obj.vend()
                elif len(args)==2 and text[0]=='deposit' :
                    self.obj.deposit(args[1])
                else:
                    print('Thanks for asking, but I know not how to '+' '.join(text))
            else:
                print('You must learn to say please.')
        else:
            print('wrong argument type, the 1st parameter must be a string!')

"""3) Write a class Amount that represents a collection of nickels and pennies.

Include a property method value that computes the value of the amount from the
nickels and pennies.  Do not add a value attribute to each Amount instance.

Finally, write a subclass MinimalAmount with base class Amount that overrides
the constructor so that all amounts are minimal.

An amount is minimal if it has no more than four pennies.
"""

class Amount(object):
    """An amount of nickels and pennies.

    >>> a = Amount(3, 7)
    >>> a.nickels
    3
    >>> a.pennies
    7
    >>> a.value
    22
    """
    "*** YOUR CODE HERE ***"
    
    def __init__(self, nic, pen):
        self.nickels=nic
        self.pennies=pen
    @property    
    def value(self):
        return 5*self.nickels+self.pennies
        

class MinimalAmount(Amount):
    """An amount of nickels and pennies with no more than four pennies.

    >>> a = MinimalAmount(3, 7)
    >>> a.nickels
    4
    >>> a.pennies
    2
    >>> a.value
    22
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, nic, pen):
        self.nickels=nic+(pen//5)
        self.pennies=pen%5
   
    

"""4) Write a class Rlist that implements the recursive list data type from
section 2.3, but works with Python's built-in sequence operations: the len
function and subscript notation.

When len is called on an object with a user-defined class, it calls a method
called __len__ and returns the result

When a subscript operator is applied to an object with a user-defined class, it
calls a method called __getitem__ with a single argument (the index) and
returns the result.

As an example, here is a container class that holds a single value.
"""

class Container(object):
    """A container for a single item.
    
    >>> c = Container(12)
    >>> c
    Container(12)
    >>> len(c)
    1
    >>> c[0]
    12
    """

    def __init__(self, item):
        self._item = item

    def __repr__(self):
        return 'Container({0})'.format(repr(self._item))

    def __len__(self):
        return 1

    def __getitem__(self, index):
        assert index == 0, 'A container holds only one item'
        return self._item

class Rlist(object):
    """A recursive list consisting of a first element and the rest.
    
    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> len(s)
    3
    >>> s[0]
    1
    >>> s[1]
    2
    >>> s[2]
    3
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, rest=None):
        self.list = (item,rest)        
    def __len__(self):        
        length = 0
        s=self
        while s != None:
            s=s.list
            s, length = s[1], length + 1
        return length
    def __getitem__(self, index):
        assert index <= len(self.list)
        s=self.list
        while index > 0:
            s, index = s[1], index - 1
            s=s.list            
        return s[0]


"""Extra for experts: 5) Multiple Inheritance

Add multiple inheritance to the object system that we implemented in class
using dispatch dictionaries.  You will need to make the following changes:

    1) Allow a class to be created with an arbitrary number of base classes

    2) Classes should respond to a message 'mro' that returns the method
    resolution order for the class

    3) Looking up an attribute by name in a class (using the 'get' message)
    should follow the method resolution order

Choose a method resolution order from the three approaches that have been
used in Python since its invention:

http://python-history.blogspot.com/2010/06/method-resolution-order.html
"""
