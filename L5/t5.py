import random
import math

file_name = 'task_5.out'
with open(file_name, 'w') as out_file:

    ln = random.randint(1, 100)
    while ln > 0:
        out_file.write(str(random.random()) + ' ')
        ln -= 1

with open(file_name) as file:
    print('Sum=', math.fsum(map(float, file.read().split())))