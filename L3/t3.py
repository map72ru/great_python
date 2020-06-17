def my_func(arg1, arg2, arg3):
    return sum([arg1, arg2, arg3]) - min(arg1, arg2, arg3)

print(f'Sum1 {my_func(3, 7, 5)}')
print(f'Sum2 {my_func(9, 7, 4)}')

