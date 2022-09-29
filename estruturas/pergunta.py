# Para aprender mais sobre estruturas em programação, mais especificamente em python

def recome():
    global nome
    global invnome
    salve = "oi"
    print(salve)
    nome = input("qual seria o nome de vossa senhoria, é que minha faculdade estã solicitando sabe, e eles estão apontando uma arma para a minha cabeça: ")
    invnome = nome[::-1]
    print(f"prazer em te conhecer {invnome}, é {invnome} né? espero que seja, sou meio ruim de memória")
    temp = input("...")
    print("ahn?")
    perguntar()

def perguntar():
    global temp
    print(f"então não é {invnome}?")
    temp = input("1-sim, 2-não: ")
    resposta()
    
def resposta():
    global temp
    global nome
    global invnome
    if temp == "1":
        print("ufa, viu só, não to ficando louco :D")
        print(f"só por garantia, vamos começar nos reintroduzindo denovo então, {invnome}")
        recome()
    elif temp == "2":
        print(f"desculpe, é um erro meu sempre inverter, acho que você já deve ter conhecido alguem que falasse assim, né {nome}?")
        print(f"vamos começar denovo então, {nome}")
        recome()
    else:
        print("desculpe, não compreendi, to meio surdo esses dias")
        print("vou repetir a pergunta")
        perguntar()

recome()
