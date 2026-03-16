#Escreva um programa que leia um numero e, em seguida, informe se este numero  ́e divisivel por 3 ou  ́e m ́ultiplo de 5.

number = int(input())

divisivel3 = number % 3
multiplo5 = number % 5

if(divisivel3 == 0 and multiplo5 == 0):
    print("é divisivel por 3 e multiplo de 5")

elif(multiplo5 == 0):
    print("é apenas multiplo de 5")

elif(divisivel3 == 0):
    print("é divisivel somente por 3")

else:
    print("não é mulitiplo!")