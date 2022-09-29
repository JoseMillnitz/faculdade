from Banco import Banco
import datetime
from Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.dataabertura = datetime.datetime.today()
        self.extrato = Extrato()
        self.banco = Banco()
        self.banco.bancodedados.append(["numero", self.numero, "clientes", self.clientes])
    def depositar(self, valor):
        print(f"depositado {valor}")
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO: ", valor, "Data: ", datetime.datetime.today()])
    def sacar(self, valor):
        if valor > self.saldo:
            print("sem saldo suficiente suficiente")
        else:
            self.saldo -= valor
            print(f"sacado {valor} com sucesso")
            self.extrato.transacoes.append(["SAQUE: ", valor, "Data: ", datetime.datetime.today()])
    def gerarextrato(self):
        print(f"numero da conta: {self.numero}\nsaldo atual: {self.saldo}")
    def transferir(self, destino, valor):
        if valor > self.saldo:
            print("sem saldo suficiente")
        else:
            destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA: ", valor, "Data: ", datetime.datetime.today()])
            print("transferencia realizada")
