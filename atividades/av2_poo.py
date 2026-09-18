class Veiculo:
    def __init__(self, modelo: str, placa: str, valor_diaria: float):
        self.__modelo = modelo
        self.__placa = placa
        self.valor_diaria = valor_diaria  

    @property
    def modelo(self) -> str:
        return self.__modelo

    @property
    def placa(self) -> str:
        return self.__placa

    @property
    def valor_diaria(self) -> float:
        return self.__valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    def calcular_aluguel(self, dias: int) -> float:
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")
        return self.__valor_diaria * dias


class Carro(Veiculo):
    def __init__(self, modelo: str, placa: str, valor_diaria: float, portas: int):
        super().__init__(modelo, placa, valor_diaria)
        self.portas = portas

    @property
    def portas(self) -> int:
        return self.__portas

    @portas.setter
    def portas(self, quantidade: int):
        if quantidade <= 0:
            raise ValueError("O carro deve ter pelo menos 1 porta.")
        self.__portas = quantidade

    def calcular_aluguel(self, dias: int) -> float:
        valor_base = super().calcular_aluguel(dias)
        taxa_limpeza = 50.0
        return valor_base + taxa_limpeza


class Moto(Veiculo):
    def __init__(self, modelo: str, placa: str, valor_diaria: float, cilindradas: int):
        super().__init__(modelo, placa, valor_diaria)
        self.cilindradas = cilindradas

    @property
    def cilindradas(self) -> int:
        return self.__cilindradas

    @cilindradas.setter
    def cilindradas(self, cc: int):
        if cc <= 0:
            raise ValueError("A cilindrada deve ser maior que zero.")
        self.__cilindradas = cc

    def calcular_aluguel(self, dias: int) -> float:
        valor_base = super().calcular_aluguel(dias)
        desconto = 0.10
        return valor_base * (1 - desconto)

class SistemaGestaoFrota:
    def __init__(self):
        self.frota = []

    def cadastrar_veiculo(self):
        print("\n--- CADASTRO DE VEÍCULO ---")
        print("1 - Carro")
        print("2 - Moto")
        
        tipo = input("Escolha o tipo de veículo (1/2): ").strip()
        if tipo not in ["1", "2"]:
            raise ValueError("Tipo de veículo inválido! Selecione 1 ou 2.")

        modelo = input("Modelo: ").strip()
        if not modelo:
            raise ValueError("O modelo não pode ser vazio.")

        placa = input("Placa: ").strip().upper()
        if not placa:
            raise ValueError("A placa não pode ser vazia.")

        # Validação se a placa já existe na frota
        for v in self.frota:
            if v.placa == placa:
                raise ValueError("Já existe um veículo cadastrado com esta placa!")

        valor_diaria = float(input("Valor da Diária (R$): "))

        if tipo == "1":
            portas = int(input("Quantidade de Portas: "))
            veiculo = Carro(modelo, placa, valor_diaria, portas)
        else:
            cilindradas = int(input("Cilindradas (cc): "))
            veiculo = Moto(modelo, placa, valor_diaria, cilindradas)

        self.frota.append(veiculo)
        print(f"\n✅ {veiculo.modelo} ({veiculo.placa}) cadastrado com sucesso!")

    def listar_frota(self):
        print("\n--- VEÍCULOS CADASTRADOS ---")
        if not self.frota:
            print("Nenhum veículo cadastrado na frota.")
            return

        for idx, veiculo in enumerate(self.frota, start=1):
            tipo = "Carro" if isinstance(veiculo, Carro) else "Moto"
            detalhe = f"{veiculo.portas} portas" if isinstance(veiculo, Carro) else f"{veiculo.cilindradas} cc"
            print(f"{idx}. [{tipo}] {veiculo.modelo} | Placa: {veiculo.placa} | Diária: R$ {veiculo.valor_diaria:.2f} | Detalhes: {detalhe}")

    def simular_aluguel(self):
        print("\n--- SIMULAÇÃO DE ALUGUEL ---")
        if not self.frota:
            print("A frota está vazia. Cadastre veículos primeiro.")
            return

        self.listar_frota()
        placa_busca = input("\nDigite a placa do veículo desejado: ").strip().upper()

        veiculo_encontrado = None
        for v in self.frota:
            if v.placa == placa_busca:
                veiculo_encontrado = v
                break

        if not veiculo_encontrado:
            raise KeyError(f"Veículo com placa '{placa_busca}' não foi encontrado.")

        dias = int(input("Quantidade de dias de aluguel: "))
        
        total = veiculo_encontrado.calcular_aluguel(dias)

        print("\n--- RESUMO DA LOCAÇÃO ---")
        print(f"Veículo: {veiculo_encontrado.modelo} ({veiculo_encontrado.placa})")
        print(f"Dias de locação: {dias}")
        print(f"Valor Total: R$ {total:.2f}")

    def executar(self):
        while True:
            try:
                print("\n==================================")
                print("   SISTEMA DE GESTÃO DE FROTA    ")
                print("==================================")
                print("1 - Cadastrar Veículo")
                print("2 - Listar Frota")
                print("3 - Simular Aluguel")
                print("4 - Sair")

                opcao = input("Escolha uma opção (1-4): ").strip()

                if opcao == "1":
                    self.cadastrar_veiculo()
                elif opcao == "2":
                    self.listar_frota()
                elif opcao == "3":
                    self.simular_aluguel()
                elif opcao == "4":
                    print("\nEncerrando o sistema... Até logo!")
                    break
                else:
                    raise ValueError("Opção inválida! Escolha um número entre 1 e 4.")

            except ValueError as e:
                print(f"\n❌ Erro de Entrada/Validação: {e}")
            except KeyError as e:
                print(f"\n❌ Erro de Busca: {e}")
            except Exception as e:
                print(f"\n❌ Ocorreu um erro inesperado: {e}")
            else:
                pass
            finally:
                print("-" * 34)

if __name__ == "__main__":
    sistema = SistemaGestaoFrota()
    sistema.executar()