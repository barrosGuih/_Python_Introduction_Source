# ● Tipos de dados 
_nome = "guilherme" #tipo texto
_idade = 10         #tipo numero inteiro
_altura = 1.80      #tipo numero floatoante ou quebrado
_inteligente = True #tipo booleano, verdadeiro ou falso

#============================list(array)===========================================================================
frutas = ["maçã", "banana", "laranja"]  # 
numeros = [1, 2, 3, 4, 5]               # 
misturada = [1, "dois", 3.0, True]      # 

# Acessando elementos
primeira_fruta = frutas[1]  # "banana"

# Modificando elementos
frutas[1] = "morango"  # Agora a lista é ["maçã", "morango", "laranja"]

# Adicionando elementos
frutas.append("uva")  # Adiciona ao final
frutas.insert(1, "pêra")  # Insere na posição 1

# Removendo elementos
frutas.remove(frutas[0])  # Remove pelo valor

ultima_fruta = frutas.pop()  # Remove e retorna o último item


#============================tuplas===============================================================================
coordenadas = (10, 20)           # 
cores_rgb = (255, 0, 0)          # 
singleton = (42,)                # 

# Acessando elementos (semelhante às listas)
x = coordenadas[0]  # 10
y = coordenadas[1]  # 20

# Diferentemente das listas, não podemos modificar elementos:
# coordenadas[0] = 15  # Isso geraria um erro!

# Desempacotamento de tuplas
r, g, b = cores_rgb  # r=255, g=0, b=0


#============================dicionario(dict)========================================================================

pessoa = {"nome": "Ana", "idade": 30, "profissao": "Engenheira"}  # 
config = {"debug": True, "max_connections": 100}                  # 

# Acessando valores
nome = pessoa["nome"]  # "Ana"

# Método seguro para acessar (não gera erro se a chave não existir)
email = pessoa.get("email", "não informado")  # "não informado"

# Adicionando ou modificando valores
pessoa["email"] = "ana@exemplo.com"

# Removendo valores
del pessoa["profissao"]

# Iterando sobre o dicionário
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")

# Obtendo chaves e valores
todas_chaves = pessoa.keys()
todos_valores = pessoa.values()


#============================Conjuntos(set)========================================================================
vogais = {"a", "e", "i", "o", "u"}                # 
numeros_primos = {2, 3, 5, 7, 11, 13}             # 

# Não permite elementos duplicados
letras = {"a", "b", "a", "c"}  # Será {"a", "b", "c"}

# Adicionando elementos
vogais.add("y")  # Em alguns idiomas, y pode ser considerada uma vogal

# Removendo elementos
vogais.remove("y")

# Operações de conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

uniao = conjunto1 | conjunto2        # {1, 2, 3, 4, 5, 6}
intersecao = conjunto1 & conjunto2   # {3, 4}
diferenca = conjunto1 - conjunto2    # {1, 2}

# ● Estruturas de controle (if, while, for)
# ● Vetores e matrizes
# ● Estruturas de dados (fila, pilha, lista)
# ● Manipulação de arquivos
# ● Algoritmos de ordenação (bubble, selection, insertion)