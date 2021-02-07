from conta import Conta

count = 1

for contador in range(2):
    numero_conta = int(input("Digite o número da conta {} : ".format(count)))
    titular_conta = input("Digite o número do titular: ")
    saldo_conta = int(input("Digite o saldo da conta: "))

    if (count == 1):
        conta1 = Conta(numero_conta, titular_conta, saldo_conta)
        print("Conta {} criada por {}, com o saldo de {}.".format(numero_conta, titular_conta, saldo_conta))
    else:
        conta2 = Conta(numero_conta, titular_conta, saldo_conta)
        print("Conta {} criada por {}, com o saldo de {}.".format(numero_conta, titular_conta, saldo_conta))
    count += 1


print("Deseja logar em qual conta? 1 ou 2?")
conta_logada = int(input())
print("Você está usando a conta ", conta_logada)
print("O que deseja fazer?")
print(" Extrato [1] -- Sacar [2] -- Depositar [3] -- Transferir [4] ")
operacao = int(input())


if (operacao == 1):
    if (conta_logada == 1):
        conta1.extrato()
    else:
        conta2.extrato()


elif (operacao == 2):
    valor_saque = float(input("Qual valor?\n"))
    if (conta_logada == 1):
        conta1.saque(valor_saque)
    else:
        conta2.saque(valor_saque)


elif (operacao == 3):
    valor_deposita = float(input("Qual valor?\n"))
    if (conta_logada == 1):
        conta1.deposita(valor_deposita)
    else:
        conta2.deposita(valor_deposita)


elif (operacao == 4):
    valor_transferir = float(input("Qual valor?\n"))
    Conta.transferir(valor_transferir, conta1, conta2, conta_logada)


else:
    print("Digite um número(função) válida!")
