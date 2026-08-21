class Funcionario:
    def __init__(self, nome: str, matricula: str, salario_base: float):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self) -> float:
        return self.__salario_base

    def set_salario_base(self, novo_salario: float):
        if novo_salario > 0:
            self.__salario_base = novo_salario
        else:
            print(f"Erro: O novo salário para {self.nome} deve ser maior que zero.")

    def calcular_salario_final(self) -> float:
        return self.__salario_base


class Gerente(Funcionario):
    def __init__(self, nome: str, matricula: str, salario_base: float, bonus_gestao: float):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self) -> float:
        return self.get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, matricula: str, salario_base: float, nivel: str):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self) -> float:
        salario = self.get_salario_base()
        if self.nivel == "Senior":
            salario += 1500.00
        return salario

if __name__ == "__main__":
    print("--- SISTEMA DE GESTÃO TECHCORP ---")
    
    gerente_1 = Gerente(nome="Ana Silva", matricula="G001", salario_base=8000.00, bonus_gestao=2000.00)
    
    dev_senior = Desenvolvedor(nome="Carlos Souza", matricula="D005", salario_base=6000.00, nivel="Senior")
    
    print("\n[Teste de Encapsulamento]")
    print(f"Salário base original (Carlos): R$ {dev_senior.get_salario_base():.2f}")
    
    dev_senior._Funcionario__salario_base = -100
    
    print(f"Tentativa de modificação direta. Salário base lido pelo getter: R$ {dev_senior.get_salario_base():.2f}")
    
    dev_senior.set_salario_base(-500)
    dev_senior.set_salario_base(6500.00) 
    print(f"Salário base após uso correto do setter: R$ {dev_senior.get_salario_base():.2f}")

    print("\n[Relatório de Salários Finais - TechCorp]")
    print(f"Funcionário: {gerente_1.nome} (Gerente) | Matrícula: {gerente_1.matricula} | Salário Final: R$ {gerente_1.calcular_salario_final():.2f}")
    print(f"Funcionário: {dev_senior.nome} (Desenvolvedor {dev_senior.nivel}) | Matrícula: {dev_senior.matricula} | Salário Final: R$ {dev_senior.calcular_salario_final():.2f}")