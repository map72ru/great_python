num = int(input('Typed int number: '))
max_digit = 0

while True:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num = num // 10
    if num == 0:
        break
print(f'Max digit: {max_digit}')