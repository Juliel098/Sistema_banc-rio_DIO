loop = 1
operacoes = []
limite_saque = 0
limite_valor_saque = 500
saldo = 0

usuario = []
conta = []

def menu():
    print('''SISTEMA BANCÁRIO
                1 - DEPÓSITO
                2 - SAQUE
                3 - EXTRATO
                0 - SAIR
    ''')
    resultado_menu = int(input(':'))
    return resultado_menu

def deposito(valor_deposito, saldo, operacoes):
    
    if valor_deposito > 0:
        saldo += valor_deposito
        operacoes.append('DEPÓSITO - R$ {}'.format(valor_deposito))
    else:
        print('VALOR INCORRETO')
    
    return saldo, operacoes


def saque(*,valor_saque, limite_valor_saque, saldo, operacoes, limite_saque):
    if valor_saque > limite_valor_saque:
        print('VALOR SUPERIOR AO PERMITIDO -> R$ {}'.format(limite_valor_saque))
    else:
        saldo -= valor_saque
        operacoes.append('SAQUE - R$ {}'.format(valor_saque))
        limite_saque += 1
    return saldo, operacoes, limite_saque

def cadastro_cliente():
    nome = str(input('Nome: '))
    data_de_nascimento = str(input('Data de Nascimento: '))
    print('SOMENTE NÚMERO')
    cpf = int(input('CPF: '))

    logradouro = str(input('Logradouro: '))
    numero = str(input('Número: '))
    Bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    sigla_estado = str(input('Sigla do Estado: '))
    endereco = str([logradouro,',',numero,' - ',Bairro,' - ',cidade,'/',sigla_estado])

    usuario.append({'Nome':nome,'Data de Nascimento':data_de_nascimento,'CPF':cpf,'Endereço':endereco})
    cadastrar_conta_bancaria(agencia = '0001', usuario=cpf)

def cadastrar_conta_bancaria(agencia, usuario):
    conta.append({'Agencia':agencia,'Numero da Conta':len(conta)+1,'Usuario':usuario})

'''Ajustar o controle de contas'''
    
    

print('''SISTEMA BANCÁRIO - DIO''')

cadastro_cliente()

while loop != 0:
    resultado_menu = menu()

    if resultado_menu == 1:
        print('INFORME O VALOR')
        valor_deposito = float(input(':'))
        saldo, operacoes = deposito(valor_deposito, saldo, operacoes)
            


    elif resultado_menu == 2:
        if limite_saque >= 3:
            print('OPERAÇÃO NEGADA')
        else:
            print('INFORME O VALOR')
            valor_saque = float(input(':'))
            saldo, operacoes, limite_saque = saque(valor_saque=valor_saque,limite_valor_saque=limite_valor_saque , saldo=saldo, operacoes=operacoes, limite_saque=limite_saque)
                

        
    elif resultado_menu == 3:
        for operecao in operacoes:
            print(operecao)
        print('SALDO - R$ {}'.format(saldo))

    elif resultado_menu == 0:
        loop = 0

    else:
        print('SELEÇÃO INVÁLIDA')

