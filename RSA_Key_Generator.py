import random

'''
Miller-Rabin Primality Test

Input:
    p: prime candidate
    s: security parameter

Output:
    True if p is likely prime
    False is p is composite
'''
def miller_rabin(p, s = 40):
    
    # Preliminary tests:
    if p == 2 or p == 3:
        return True
    if p % 2 == 0:
        return False
    
    # Setting variable values
    r, u = 0, p - 1
    while r % 2 == 0:
        u += 1
        r //= 2
        print('here1')
    # Miller-Rabin implementation:
    print('here3')
    for _ in range(s):
        a = random.randint(2, p - 1)
        z = pow(a, r, p)
        if z == 1 or z == p - 1:
            continue
        for _ in range(u - 1):
            z = pow(z, 2, p)
            if z == p - 1:
                break
        else:
            return False
            
    return True

# Generate a prime number
def gen_prime(min_val, max_val):
    prime = random.randint(min_val, max_val)
    print(prime)
    while not miller_rabin(prime):
        prime = random.randint(min_val, max_val)
        print(prime)
    return prime

def totient_function(p, q):
    return (p - 1)(q - 1)

def select_public_exponent(phi_n):
    return random.randint(1, phi_n - 1)

def compute_private_key():
    return

def generate_keys():
    p = gen_prime(10,100)
    q = gen_prime(10,100)
    print(p, q)
