import math
def is_prime(n):
    #import pdb; pdb.set_trace()
    for divisor in range(2,int(math.sqrt(n))+1):
        if n % divisor == 0: return False
    return True
    
