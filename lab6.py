def make_fib():
    a,b=1,1
    n=0 
    def fib():
        nonlocal n,a,b
        n=n+1
        if n==1:
            return a
        if n==2:
            return b
        k=a+b
        a,b=b,k
        return k
    return fib

def build_successors_table(tokens):
    table = {}
    prev = '.'
    for word in tokens:
        if prev in table:
            
            table[prev].append(word)
            
        else:
            table[prev]=[word]
        prev = word    
    return table

def construct_sent(word, table):
    import random
    result = ''
    while word not in ['.', '!', '?']:
        result=result+' '+word
        word=random.choice(table[word])
    return result + word

def shakespeare_tokens(path = 'shakespeare.txt', url = 'http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list"""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()        
    else:
        shakespeare = urlopen(url)          
    return shakespeare.read().decode(encoding='ascii').split()
