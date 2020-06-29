import json

def iff(a, b):
    if a > b:
        return a
    return -b

firms = {}
avg_profit = 0
n = 0

with open('task_7.txt', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        name, other = line.split(':')
        form, profit, loss = other.split()
        profit = float(profit)
        loss = float(loss)
        if profit > loss:
            avg_profit += profit
            n += 1
        firms.update({name: iff(profit, loss)})

if n > 0:
    avg_profit /= n

with open('task_7.out', 'w', encoding='utf-8') as out_file:
    jsn = json.dumps([firms, {'average_profit': avg_profit}], ensure_ascii=False)
    out_file.write(jsn)
