def hailstone(n):
    count=0
    while n!=1:
        count=count+1
        print('No. of the steps:', count)
        print('Corresponding term:', n)
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    count=count+1
    print('No. of the steps:', count)
    print('Corresponding term:', n)
    return
        
            
                
