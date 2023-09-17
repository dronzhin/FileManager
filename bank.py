account = 0
purchase_history = []

def add_money():
    money = int(input("Введите сумму, которую хотите положить на счет: "))
    global account
    account += money
    print(f'На вашем счету {account} рублей')


def buy_product():
    global account
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


def print_product():
    print('Историй покупок:')
    for i in purchase_history:
        print(i)
def banking():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            add_money()
        elif choice == '2':
            buy_product()
        elif choice == '3':
            print_product()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')