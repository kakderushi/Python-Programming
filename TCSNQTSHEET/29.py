import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Find and print prime numbers between 1 and 10
primes = [i for i in range(1, 11) if is_prime(i)]
print("Prime numbers between 1 and 10 are:", primes)
