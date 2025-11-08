your_balance = int(0)
db_history_transactions = list()

def inicilization_program():
    while True:
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход из банка')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            make_deposit()
        elif choice == '2':
            make_transactions()
        elif choice == '3':
            # history_of_transaction()
            print('История покупок: ', db_history_transactions)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

def make_deposit():
    global your_balance
    print('Текущий баланс: ', your_balance)
    your_balance = your_balance + int(input('Пожалуйста, введите сумму, которую вы вносите на счёт: '))
    print('Баланс после пополнения: ', your_balance)
    # return your_balance

def make_transactions():
    global your_balance
    price_transactions = int(input('Пожалуйста, введите сумму списания: '))
    # if price_transactions.isdigit():
    if price_transactions <= your_balance:
        your_balance = your_balance - price_transactions
        name_transactions = str(input('Пожалуйста, введите наименование покупки: '))
        db_history_transactions.append(name_transactions)
        db_history_transactions.append(price_transactions)
    elif price_transactions > your_balance:
        print('Недостаточно средств на счёте: ', your_balance)
    #else:
    #    print("Необходимо ввести сумму цмфрами")

#inicilization_program()