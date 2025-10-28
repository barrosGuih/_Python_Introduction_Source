import time

print("Você entrou no banco!")

fila = ["1","2","3","4"]

fila.append("5")
_ficha = fila[-1]
print("sua ficha é: ", _ficha)


while fila[0] != _ficha:
    print("ficha atual: ", fila[0])
    print("aguardando atendimento...\n")
    time.sleep(3)
    fila.pop(0)

print("\n sua vez chegou Ficha: ", _ficha)