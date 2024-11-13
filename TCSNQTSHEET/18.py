#check if the number prime or not

def is_prime(n):
    # Check if the number is less than 2, which are not prime
    if n <= 1:
        return False
    
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Example usage:
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
