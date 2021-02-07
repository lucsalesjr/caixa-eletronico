class Conta:

    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular


    def saque(self, valor_saque):
        if (valor_saque <= self.saldo):
            self.saldo -= valor_saque
            print("Seu saldo é de {}".format(self.saldo))
        else:
            print("Você nao tem saldo suficiente para realizar o saque")


    def deposita(self, valor):
        self.saldo += valor
        print("Seu saldo é de {}".format(self.saldo))


    def extrato(self):
        print("Titular e número: {}; {} -- Saldo: {}".format(self.titular, self.numero, self.saldo))


    def transferir(valor_transferir, conta1, conta2, conta_logada):

        numero_de_transferencia = int(input("Digite o número da conta que deseja transferir: "))

        if (numero_de_transferencia == conta1.numero or numero_de_transferencia == conta2.numero):

            if (conta_logada == 1):
                if (conta1.numero == numero_de_transferencia):
                    print("Você não pode transferir para sua própria conta!")

                else:
                    if (conta1.saldo >= valor_transferir):
                        conta1.saldo -= valor_transferir
                        conta2.saldo += valor_transferir
                        Conta.extrato(conta1)
                        Conta.extrato(conta2)

                    else:
                        print("Você não tem saldo suficiente para realizar a transferência")

            else:
                if (conta2.numero == numero_de_transferencia):
                    print("Você não pode transferir para sua própria conta!")

                else:
                    if (conta1.numero == numero_de_transferencia):
                        if (conta2.saldo >= valor_transferir):
                            conta2.saldo -= valor_transferir
                            conta1.saldo += valor_transferir
                            Conta.extrato(conta1)
                            Conta.extrato(conta2)
                        else:
                            print("Você não tem saldo suficiente para realizar a transferência")

        else:
            print("Conta inexistente")