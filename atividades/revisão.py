# 1. abstração e encapsulamento
class Veiculo:
    def __init__(self, marca, modelo, valor_diaria):
        self.marca = marca
        self.modelo = modelo
        #TODO: torne o atributo valor_diaria privado
        self.__valor_diaria = valor_diaria

    def get_valor_diaria(self):
        return self.__valor_diaria

    def calcular_valor_aluguel(self, dias):
        return self.__valor_diaria * dias

#2. herança e reuso de código
class Carro(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, portas):
        super().__init__(marca, modelo, valor_diaria)
        self.portas = portas

    def calcular_valor_aluguel(self, dias):
        valor_base = super().calcular_valor_aluguel(dias)
        return valor_base + self.taxa_de_limpeza

    def __init__(self, marca, modelo, valor_diaria, portas):
        super().__init__(marca, modelo, valor_diaria)
        self.portas = portas
        self.taxa_de_limpeza = 50