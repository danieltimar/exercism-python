def square_of_sum(count):
    sum = 0
    for i in range(1,count+1):
        sum += i
    return sum ** 2

def sum_of_squares(count):
    sum_of_sq = 0
    for i in range(1,count+1):
        sum_of_sq += i ** 2
    return sum_of_sq


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
