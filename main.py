import getpass
import os
from collections import OrderedDict

accounts = {
    '0001-1': {
        'password': '123456',
        'customer_name': 'John Due',
        'balance_value': 500.13,
        'admin': False
    },
    '0001-2': {
        'password': '654321',
        'customer_name': 'Maria Due',
        'balance_value': 1000,
        'admin': False
    },
    '0000-0': {
        'password': '1234',
        'customer_name': 'Admin',
        'balance_value': 2000,
        'admin': True
    }
}

money_slips = {
    20: 5,
    50: 5,
    100: 5
}

# infinity execution
while True:
    print("***************** BEM VINDO *********************")
    print("*************** CAIXA ELETRÓNICO ****************")
    print("******************* COBRA ***********************")

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts and password_typed == accounts[account_typed]['password'] :
        account = accounts[account_typed]
        print('Olá ' + account['customer_name'])
        print('Seu saldo atual é de: R$ %s' % account['balance_value'])

        bCashOut = input("Deseja efetuar um saque?\n1 - SIM\n2 - NÃO\n")
        if(bCashOut == '1') :
            fCashOutValue_typed = input("Digite o valor que deseja sacar: ")
            fCashOutValue = float(fCashOutValue_typed)
            if(int(fCashOutValue) < account['balance_value']):
                money_slips_user = {}
                value_int = int(fCashOutValue_typed)
                for key, value in sorted(money_slips.items(), reverse=True) :
                    iKey = int(key)
                    if value_int // iKey > 0 and value_int // iKey <= money_slips[key] :
                        money_slips_user[key] = value_int // iKey
                        value_int = value_int - value_int // iKey * iKey
    
                if value_int != 0:
                    print('O caixa não tem cédulas disponíveis para este valor')
                else:
                    for money_bill in money_slips_user:
                        money_slips[money_bill] -= money_slips_user[money_bill]

                    account['balance_value'] -= fCashOutValue

                    print('Valor sacado R$: %s' % fCashOutValue)
                    print('Saldo após o saque R$: %s' % account['balance_value'])
                    print('Pegue as notas:')
                    print(money_slips_user)

            else : 
                print('O valor a ser sacado é maior que seu saldo atual.')

        # only admin - ask if want add bank note
        if(account['admin']) :
            bAddCash = input("Deseja incluir cédulas?\n1 - SIM\n2 - NÃO\n")
            if(bAddCash == '1') :
                amount_typed = input('Digite a quantidade de cédulas: ')
                money_bill_typed = input('Escolha o valor da cédula a ser incluída: ')
                money_slips[money_bill_typed] += int(amount_typed)
                print(money_slips)
    else:
        print('Conta inválida')

    input('Presione <ENTER> para continuar...')

    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)
