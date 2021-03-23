MENU = {
    'sandwich': 10,
    'soup': 8,
    'tea': 3,
}


def restaurant():
    total = 0
    while True:
        order = input('What is your order? ').strip()
        price = MENU.get(order)

        if not order:
            print(f'Your total is {total}')
            break
        elif price is None:
            print(f'Sorry, {order} is not on the menu')
        else:
            total += price
            print(f'{order} costs {price}, your total is {total}')
