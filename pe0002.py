# Even Fibonacci numbers
# Problem 2
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find
# the sum of the even-valued terms.


def evenfibonaccis(limit=None):
    if not limit:
        limit = 4e6

    def step(answer_sum, x, y):
        if y < limit:
            if y % 2 == 0:
                answer_sum += y
            print(x, y)
            return step(answer_sum, y, x + y)
        return answer_sum

    print(step(0, 1, 2))


if __name__ == "__main__":
    evenfibonaccis()
