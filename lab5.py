

def reverse(seq):
    """Takes an input tuple, seq, and returns a tuple with the same items in
    reversed order. Does not reverse any items in the tuple and does not modify the
    original tuple.

    Arguments:
    seq -- The tuple for which we return a tuple with the items reversed.

    >>> x = (1, 2, 3, 4, 5)
    >>> reverse(x)
    (5, 4, 3, 2, 1)
    >>> x
    (1, 2, 3, 4, 5)
    >>> y = (1, 2, (3, 4), 5)
    >>> reverse(y)
    (5, (3, 4), 2, 1)
    """
    "*** Your code here. ***"
    l=len(seq)
    op=()
    for k in range(0,l):
        op=op+(seq[l-k-1],)
    return op

def sizes(seq):
    """Takes an input sequence of tuples, seq, and returns a sequence with the
    corresponding lengths of each tuple in seq.

    Arguments:
    seq -- A sequence of tuples.

    >>> sizes(((1,), (2, 3), (4, 5, 6)))
    (1, 2, 3)
    """
    "*** Your code here. ***"
    return tuple(map(len,seq))

def odd_len_only(seq):
    """Takes an input sequence of tuples, seq, and returns a sequence with only
    the tuples which had odd length.
    
    Arguments:
    seq -- A sequence of tuples.

    >>> odd_len_only(((1,), (2, 3), (4, 5, 6)))
    ((1,), (4, 5, 6))
    """
    "*** Your code here. ***"
    return tuple(filter(lambda x: len(x) % 2 != 0, seq))

def tuple_to_rlist(tup):
    """Takes an input tuple, tup, and returns the equivalent representation of
    the sequence using an rlist.
    
    Arguments:
    tup -- A sequence represented as a tuple.

    >>> tuple_to_rlist((1, 2, 3, 4, 5, 6))
    (1, (2, (3, (4, (5, (6, None))))))
    """
    "*** Your code here. ***"
    temp=reverse(tup)
    op=(temp[0],None)
    for i in range(1,len(tup)):
        op=(temp[i],op)
    return op


    
    
    
    
    


    
    
    
