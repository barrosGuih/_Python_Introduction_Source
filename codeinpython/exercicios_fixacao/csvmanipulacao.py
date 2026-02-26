import csv



# Especificando delimitador
with open("dados.tsv", "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.reader(arquivo, delimiter="\t")  # Tabulação como delimitador
    for linha in leitor:
        print(linha)