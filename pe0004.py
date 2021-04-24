# Largest palindrome product
# Problem 4
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

import pefn

u = pefn.utility()


def largest_palindrome_product(max_digit, min_digit):
    max_pal = 0
    for x in range(max_digit, min_digit, -1):
        y = max_digit
        while x * y > max_pal and y > min_digit:
            product = x * y
            product_str = str(product)
            if product_str == product_str[::-1] and product > max_pal:
                max_pal = product
                print(f"{x} * {y} = {product_str}")
            y -= 1
    return max_pal


if __name__ == "__main__":
    u.tstart()
    print(largest_palindrome_product(999, 100))
    u.tstop()
