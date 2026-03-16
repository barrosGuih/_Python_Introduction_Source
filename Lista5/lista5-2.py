#Escreva um programa que leia um numero e, em seguida, informe se este numero  ́e ou nao e divisivel por 2 e por 3 ao mesmo tempo.

number = int(input("Digite um numero para descobrir se um numero e divisivel por 2 e por 3: "))
div2 = number % 2
div3 = number % 3

if(div2 == 0 and div3 == 0):
    print("Ambos sao divisiveis por 2 e por 3")

elif(div2 != 0 or div3 == 0):
    print("Apenas divisivel por 3")

elif(div2 == 0 or div3 != 0):
    print("Apenas divisivel por 2")