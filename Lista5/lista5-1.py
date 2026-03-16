#Escreva um programa que leia um n umero e, em seguida, informe se este numero e ou nao e multiplo de 3.

numero = int(input("Digite um numero: "))
multiplo = numero % 3

if (multiplo == 0):
    print("E multiplo de 3")

else:
    print("Nao eh multiplo de 3")