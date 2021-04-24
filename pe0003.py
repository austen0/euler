# Largest prime factor
# Problem 3
#
# What is the largest prime factor of the number 600851475143?


import pefn

p = pefn.math()


def largest_prime_factor(x=None):
    if not x:
        x = 600851475143
    for i in range(2, x):
        if x % i == 0:
            val = int(x / i)
            print("checking val: ", val)
            if p.is_prime(val):
                return val


if __name__ == "__main__":
    print("largest prime factor found: ", largest_prime_factor())
