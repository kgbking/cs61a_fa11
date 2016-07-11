def isnumber(thing):
   try:
       int(thing)
   except:
       return False
   return True

def type_check(fun,isnumber,datum):
    k=isnumber(datum)
    if k:
        return fun(datum)
    else:
        return k

def make_safe(sqrt, isnumber):
    """Return a funtion that takes one numerical argument and excutes safely

    >>> make_safe(lambda x: x*x, isnumber)(2)
    4
    >>> make_safe(lambda x: x*x, isnumber)(5)
    25
    >>> make_safe(lambda x: x*x, isnumber)(0)
    0
    """
    def h(x):
        return type_check(sqrt,isnumber,x)
    return h
    

def average_value(fn, num_samples):
   """Compute the average value returned by fn over num_samples trials.
   
   >>> d = make_test_die(1, 3, 5, 7)
   >>> average_value(d, 100)
   4.0
   """
   "*** YOUR CODE HERE ***"
   total,k=0,1
   while k<=num_samples:
       total,k=total+fn(),k+1
   return total/num_samples    
   
def averaged1(fn, num_samples=100):
   """Return a function that returns the average_value of fn when called.

   >>> die = make_test_die(3, 1, 5, 7)
   >>> avg_die = averaged1(die)
   >>> avg_die()
   4.0
   """
   "*** YOUR CODE HERE ***"
   def h():
       return average_value(fn, num_samples)
   return h
