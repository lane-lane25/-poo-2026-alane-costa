class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_bonus(self) -> float:
        """Retorna 5% do salario_base como bônus padrão."""
        return self.salario_base * 0.05


class Gerente(Funcionario):
    def __init__(self, nome: str, salario_base: float):
        super().__init__(nome, salario_base)

    def calcular_bonus(self) -> float:
        """Calcula o bônus padrão via super() e adiciona R$ 1.000,00 fixos."""
        bonus_padrao = super().calcular_bonus()
        return bonus_padrao + 1000.00


class Vendedor(Funcionario):
    def __init__(self, nome: str, salario_base: float, total_vendas: float):
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas

    def calcular_bonus(self) -> float:
        """Ignora o bônus padrão e retorna 10% do total de vendas."""
        return self.total_vendas * 0.10


# --- Exemplo prático de uso ---
if __name__ == "__main__":
    f1 = Funcionario("Carlos", 3000.00)
    g1 = Gerente("Ana", 5000.00)
    v1 = Vendedor("Beatriz", 2500.00, total_vendas=20000.00)

    print(f"Bônus de {f1.nome} (Funcionário): R$ {f1.calcular_bonus():.2f}")
    # Cálculo: 5% de 3000 = R$ 150.00

    print(f"Bônus de {g1.nome} (Gerente): R$ {g1.calcular_bonus():.2f}")
    # Cálculo: (5% de 5000) + 1000 = 250 + 1000 = R$ 1250.00

    print(f"Bônus de {v1.nome} (Vendedor): R$ {v1.calcular_bonus():.2f}")
    # Cálculo: 10% de 20000 = R$ 2000.00