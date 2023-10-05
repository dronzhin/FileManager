def add_money(account):
    money = int(input("Введите сумму, которую хотите положить на счет: "))
    account += money
    print(f'На вашем счету {account} рублей')
    return account


def buy_product(account, purchase_history):
    product = input('Введите товар: ')
    price = int(input('Введите цену за которую покупаете: '))
    if price <= account:
        print('Покупка совершена')
        account -= price
        print(f'На счету осталось {account} рублей')
        purchase_history.append(f"{product} {price}")
    else:
        print("Денег не достаточно на счету")
        print(f'На счету {account} рублей')
    return account


def print_product(purchase_history):
    print('Историй покупок:')
    for i in purchase_history:
        print(i)
def banking(account, purchase_history):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            account = add_money(account)
        elif choice == '2':
            account = buy_product(account, purchase_history)
        elif choice == '3':
            print_product(purchase_history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
    return account