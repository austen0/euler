# Multiples of 3 and 5
# Problem 1
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168


def multiples35(limit=None):
    if not limit:
        limit = 1000
    answer_sum = 0
    for x in range(1, limit):
        if x % 3 == 0 or x % 5 == 0:
            answer_sum += x
            print(x, answer_sum)


if __name__ == "__main__":
    multiples35()
