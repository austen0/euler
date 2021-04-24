# Sum square difference
# Problem 6
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and
# the square of the sum.


sosq = 0
sqos = 0
for i in range(1, 101):
    sosq += i ** 2
    sqos += i
print(sqos ** 2 - sosq)
