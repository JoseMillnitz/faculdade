class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if valor > self.saldo:
            print("sem saldo suficiente suficiente")
        else:
            self.saldo -= valor
            print("sacado com sucesso")
    def gerarextrato(self):
        print(f"numero: {self.numero}, cpf: {self.cpf}, extrato atual: {self.saldo}")
    def transferir(self, destino, valor):
        if valor > self.saldo:
            print("sem saldo suficiente")
        else:
            destino.depositar(valor)
            self.saldo -= valor
            print("transferencia realizada")


