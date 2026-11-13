
class Livro:
    def __init__(self, titulo: str, preco_aluguel: float):
        self.set_titulo(titulo)
        self.set_preco_aluguel(preco_aluguel)

    def get_titulo(self) -> str:
        return self.__titulo

    def set_titulo(self, titulo: str):
        if not isinstance(titulo, str) or len(titulo.strip()) < 3:
            # Dispara ValueError para ser capturado pela interface sem quebrar o sistema
            raise ValueError("O título do livro deve conter pelo menos 3 caracteres.")
        self.__titulo = titulo.strip()

    def get_preco_aluguel(self) -> float:
        return self.__preco_aluguel

    def set_preco_aluguel(self, preco: float):
        if not isinstance(preco, (int, float)) or preco < 0:
            raise ValueError("O valor do aluguel não pode ser negativo.")
        self.__preco_aluguel = float(preco)


class Usuario:
    def __init__(self, nome: str, email: str):
        self._nome = nome
        self._email = email

    def exibir_perfil(self) -> str:
        return f"Usuário: {self._nome} | E-mail: {self._email}"


class Leitor(Usuario):
    def __init__(self, nome: str, email: str, matricula: str):
        super().__init__(nome, email)
        self._matricula = matricula

    def exibir_perfil(self) -> str:
        return f"[LEITOR] {self._nome} (Matrícula: {self._matricula})"


class SistemaBiblioteca:
    def __init__(self):
        self.__acervo = []

    # --------------------------------------------------------------------------
    # 1. TRATAMENTO DE ValueError (Conversão numérica e regras dos Setters)
    # --------------------------------------------------------------------------
    def cadastrar_livro(self):
        print("\n--- CADASTRO DE NOVO LIVRO ---")
        while True:
            try:
                titulo = input("Título do livro: ")
                preco_texto = input("Preço do aluguel (R$): ").replace(",", ".")
                preco = float(preco_texto)  # Pode gerar ValueError se digitar letras

                # O construtor aciona os setters, que também podem lançar ValueError
                novo_livro = Livro(titulo, preco)
                self.__acervo.append(novo_livro)

            except ValueError as erro:
                # Verifica se o erro veio da conversão float() ou da regra do setter
                if "could not convert string to float" in str(erro):
                    print("[AVISO] Valor inválido! Digite apenas números para o preço (ex: 12.50).\n")
                else:
                    print(f"[AVISO] Dado inválido: {erro} Tente novamente.\n")
            else:
                print(f"[SUCESSO] Livro '{novo_livro.get_titulo()}' cadastrado no acervo!")
                break

    # --------------------------------------------------------------------------
    # 2. TRATAMENTO DE IndexError e ValueError (Busca em lista do acervo)
    # --------------------------------------------------------------------------
    def consultar_livro_por_posicao(self):
        print("\n--- CONSULTA DE LIVRO POR POSIÇÃO ---")
        if not self.__acervo:
            print("[AVISO] O acervo está vazio. Cadastre um livro primeiro.")
            return

        for i, livro in enumerate(self.__acervo):
            print(f"[{i}] {livro.get_titulo()} - R$ {livro.get_preco_aluguel():.2f}")

        while True:
            try:
                indice = int(input("\nDigite o número da posição do livro desejado: "))
                if indice < 0:
                    raise IndexError("Índice negativo não permitido.")
                livro_escolhido = self.__acervo[indice]  # Pode gerar IndexError

            except ValueError:
                print("[AVISO] Entrada inválida! Digite apenas o número inteiro da posição.")
            except IndexError:
                print(f"[AVISO] Posição inexistente! Escolha um número entre 0 e {len(self.__acervo) - 1}.")
            else:
                print(f"[SELECIONADO] {livro_escolhido.get_titulo()} | Aluguel: R$ {livro_escolhido.get_preco_aluguel():.2f}")
                break

    # --------------------------------------------------------------------------
    # 3. TRATAMENTO DE ZeroDivisionError (Cálculo de média sem livros no acervo)
    # --------------------------------------------------------------------------
    def relatorio_media_aluguel(self):
        print("\n--- RELATÓRIO FINANCEIRO DO ACERVO ---")
        try:
            soma_valores = sum(livro.get_preco_aluguel() for livro in self.__acervo)
            quantidade = len(self.__acervo)
            media = soma_valores / quantidade  # Gera ZeroDivisionError se quantidade == 0

        except ZeroDivisionError:
            print("[AVISO] Não é possível calcular a média pois não há livros cadastrados no acervo.")
        else:
            print(f"Total de livros: {quantidade} | Preço médio de aluguel: R$ {media:.2f}")
        finally:
            print("Processo de emissão de relatório finalizado.")


# ==============================================================================
# BLINDAGEM DO MENU PRINCIPAL (while True + try / except ValueError)
# ==============================================================================
def iniciar_sistema():
    biblioteca = SistemaBiblioteca()
    leitor_ativo = Leitor("Alane", "alane@bibliotech.com", "MAT-2026")
    print(f"Bem-vinda ao BiblioTech! Sessão iniciada por: {leitor_ativo.exibir_perfil()}")

    while True:
        print("\n================ MENU PRINCIPAL ================")
        print("1 - Cadastrar novo livro")
        print("2 - Consultar livro por posição (Teste IndexError)")
        print("3 - Relatório de média de preços (Teste ZeroDivisionError)")
        print("0 - Sair do sistema")
        print("================================================")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n[AVISO] Entrada inválida! Digite apenas o número da opção desejada (0 a 3).")
            continue

        if opcao == 1:
            biblioteca.cadastrar_livro()
        elif opcao == 2:
            biblioteca.consultar_livro_por_posicao()
        elif opcao == 3:
            biblioteca.relatorio_media_aluguel()
        elif opcao == 0:
            print("\nEncerrando o sistema BiblioTech com segurança. Até logo!")
            break
        else:
            print("\n[AVISO] Opção inexistente! Escolha um número entre 0 e 3.")


if __name__ == "__main__":
    iniciar_sistema()