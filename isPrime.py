import math
def is_prime2(n):
    #import pdb; pdb.set_trace()
    for divisor in range(2,int(math.sqrt(n))+1):
        if n % divisor == 0: return False
    return True
    
def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9: 
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f += 6
    return True

