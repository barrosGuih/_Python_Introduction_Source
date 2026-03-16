entrada = input("Digite em uma so entrada separados por virgula: ")

valores = entrada.split(",")

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = b**2 - 4*a*c

if(delta < 0):
    print("Nao existem raizes reais")
    
elif(delta == 0):
    x = -b / (2*a)
    print(f"Raiz: {x:.2f}")

else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    
    print(f"Raiz 1: {x1:.2f}")
    print(f"Raiz 2: {x2:.2f}")