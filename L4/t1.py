from sys import argv

def check_value(value: str, name: str):
    if not value.replace('.', '').isdigit():
        print(f'Value {name} is not a number: {value}')
        exit(1)
    return float(value)


if len(argv) < 4:
    print('not enough parameters: expected time, rate, bonus')
    exit(1)

work_time, rate, bonus = argv[1:4]
work_time = check_value(work_time, 'work_time')
rate = check_value(rate, 'rate')
bonus = check_value(bonus, 'bonus')

salary = work_time * rate + bonus

print(f'Salary: {salary}')

