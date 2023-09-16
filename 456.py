from functools import reduce

my_list = [20, -3, 15, 2, -1, -21]

product = reduce(lambda x, y: x * y, my_list)
print(product)
