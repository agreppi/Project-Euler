from math import sqrt
from isPrime import is_prime
n = 600851475143
result = 1
if n % 2 == 0: result = 2
for divisor in range(3, int(sqrt(n)),2):
    if n % divisor == 0:
        if is_prime(divisor):
            result = divisor
print(result)
