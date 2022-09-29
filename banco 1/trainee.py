from conta import Conta

c1 = Conta(1,123,"joao",1000)
c2 = Conta(2,123,"maria",1000)

c1.transferir(c2, 500)
c1.gerarextrato()
c2.gerarextrato()