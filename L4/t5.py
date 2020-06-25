from functools import reduce

numbers = [n for n in range(100, 1001) if n % 2 == 0]
print(list(numbers))

print(reduce(lambda x, y: x*y, numbers))