#metodo tradicional leitura
#arquivo = open("arquivo.txt", "r")
#conteudo = arquivo.read()
#arquivo.close

#metodo convencional leitura
#with open("arquivo.txt", "r") as arq:
  #  conteu = arq.read()

#metodo convencional escrita e leitura
"""msg = "aprovado seu lindao"
with open("text.txt", "w") as document:
    mostra = document.write(msg)
    
with open("text.txt", "r") as document:
    conteu = document.read()
    print(conteu)"""
    
# Lendo arquivo inteiro
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Lendo linha por linha
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove espaços e quebras de linha extras

# Lendo todas as linhas em uma lista
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print(f"O arquivo tem {len(linhas)} linhas")
    for i, linha in enumerate(linhas):
        print(f"Linha {i+1}: {linha.strip()}")