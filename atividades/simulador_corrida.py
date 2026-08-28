from abc import ABC, abstractmethod


# Classe Abstrata / Interface
class Veiculo(ABC):

  def __init__(self, modelo: str):
    self.modelo = modelo

  @abstractmethod
  def acelerar(self):
    pass


# Subclasses
class Carro(Veiculo):

  def acelerar(self):
    print(f"O carro {self.modelo} acelerou: Vrum vrum! Chegando a 120 km/h.")


class Moto(Veiculo):

  def acelerar(self):
    print(
        f"A moto {self.modelo} acelerou: Randandandan! Ultrapassando pelo"
        " corredor."
    )


class Caminhao(Veiculo):

  def acelerar(self):
    print(
        f"O caminhão {self.modelo} acelerou: BRRRRRR! Ganhando velocidade"
        " lentamente com peso."
    )


# Desafio Bônus: Nova classe adicionada sem alterar a estrutura da simulação
class CarroEletrico(Veiculo):

  def acelerar(self):
    print(
        f"O carro elétrico {self.modelo} acelerou em silêncio: SSShhhh!"
        " Torque instantâneo de 0 a 100 km/h!"
    )


# Execução Polimórfica (Simulação de Corrida)
pista_de_corrida = [
    Carro("Sedan Sport"),
    Moto("Ninja 600"),
    Caminhao("Volvo FH"),
    CarroEletrico("Tesla Model S"),  # Adicionado pelo Desafio Bônus
]

print("--- INÍCIO DA CORRIDA ---")
for veiculo in pista_de_corrida:
  veiculo.acelerar()
print("--- FIM DA CORRIDA ---")