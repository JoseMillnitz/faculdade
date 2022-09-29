# calculo IMC basico

print ("seja bem vindo, iremos calcular seu IMC")
print("para maior precisão, use gramas e centimetros")
print("para numeros decimais coloque o ponto '.'")
peso = float(input("por favor, coloque seu peso: "))
altura = float(input("por favor, coloque sua altura: "))
IMC = format((peso/(altura**2)), ".2f")
print(f"seu IMC é: {IMC}")
