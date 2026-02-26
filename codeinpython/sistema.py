class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        print("Ligado o carro VRUMMMM")
    
meu_carro = Carro("Fiat", "chevrolet", "2000")
print(meu_carro.marca)
meu_carro.ligar()