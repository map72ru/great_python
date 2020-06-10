cost = float(input('Firm cost: '))
revenue = float(input('Firm revenue: '))
profit = revenue - cost

if profit > 0:
    print('Very fine')

    profitability = profit / cost

    strength = int(input('Typed firm strength: '))

    print(f'Profit on worker: {profit / strength:0.2f}')
else:
    print('I\'ll tell Donald everything')

