def myPow(x,n):
    if x == 0.0:
        return 0.0
    
    res = 1
    
    while n:
        if n & 1:
            res *= x
        
        x *= x
        n >>= 1
        
    return res