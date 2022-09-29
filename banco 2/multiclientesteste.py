from Contas import Conta
from Banco import Banco
from Clientes import Cliente

banco = Banco()

cliente1 = Cliente(123, "joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")
conta1 = Conta([cliente1,cliente2], 1,0)

cliente4 = Cliente(6789, "Varia", "Rua 4")
cliente3 = Cliente(1234, "jose", "Rua 3")
conta2 = Conta([cliente4,cliente3], 2,0)

conta1.gerarextrato()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarextrato()

conta2.gerarextrato()
conta1.transferir(conta2, 500)
conta2.sacar(250)
conta1.gerarextrato()
conta2.gerarextrato()

print("aqui é pra vim algo diferente")
conta1.extrato.extrato(conta1.numero)

conta2.extrato.extrato(conta2.numero)

print(banco.bancodedados)