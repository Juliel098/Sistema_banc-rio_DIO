loop = True

operacoes = []

limite_saque = 0
limite_valor_saque = 500

saldo = 0

while loop != 0:
    print('''SISTEMA BANCÁRIO
                1 - DEPÓSITO
                2 - SAQUE
                3 - EXTRATO
                0 - SAIR
    ''')

    resultado_menu = int(input(':'))

    if resultado_menu == 1:
        print('INFORME O VALOR')
        deposito = float(input(':'))
        if deposito > 0:
            saldo += deposito
            operacoes.append('DEPÓSITO - R$ {}'.format(deposito))
        else:
            print('VALOR INCORRETO')


    elif resultado_menu == 2:
        if limite_saque >= 3:
            print('OPERAÇÃO NEGADA')
        else:
            print('INFORME O VALOR')
            saque = float(input(':'))
            if saque > limite_valor_saque:
                print('VALOR SUPERIOR AO PERMITIDO -> R$ {}'.format(limite_valor_saque))
            else:
                saldo -= saque
                operacoes.append('SAQUE - R$ {}'.format(saque))
                limite_saque += 1

    
    elif resultado_menu == 3:
        for operecao in operacoes:
            print(operecao)
        print('SALDO - R$ {}'.format(saldo))

    elif resultado_menu == 0:
        loop = 0

    else:
        print('SELEÇÃO INVÁLIDA')