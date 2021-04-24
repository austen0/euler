# Special Pythagorean triplet
# Problem 9
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
#
# Answer: 31875000

a = 1
go = True
while go and a < 1000:
    b = a + 1
    while go and b < 1000:
        c = b + 1
        while go and c < 1000:
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                print(a ** 2 + b ** 2, c ** 2)
                print(a + b + c)
                print(a * b * c)
                go = False
            c += 1
        b += 1
    a += 1
