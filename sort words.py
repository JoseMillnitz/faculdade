#organizando as coisas em ordem alfabética partindo de uma string
textoexperimento = "isso aqui é para ficar em ordem alfabetica, Ele eh case insensitive, mas, ainda não solucionei os acentos"

def sort_texto(texto):
    texto = texto.casefold()
    list_sort = texto.split()
    list_sort.sort()
    texto = ""
    for i in list_sort:
        texto = f"{texto} {i}"
    return texto

print(sort_texto(textoexperimento))
