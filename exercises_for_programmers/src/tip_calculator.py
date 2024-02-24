

def tip_calculator():
    bill_amount = float(input("What is the bill amount? "))
    tip_rate = int(input("What is the tip rate? "))
    tip = bill_amount * (tip_rate/100)
    total_amount = bill_amount + tip

    print(f'Tip: {tip}')
    print(f'Total amount: ${total_amount}')


if __name__ == '__main__':
    tip_calculator()
