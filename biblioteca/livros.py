# Lista onde os livros ficarão armazenados



def adicionar_livro(biblioteca):
    print("\n===== ADICIONAR LIVRO =====")

    codigo = input("Insira o código do livro: ")

    if codigo == "":
        print("Código inválido.")
        return

    # Verifica se o código já existe
    for livro in biblioteca:
        if livro[0] == codigo:
            print("Já existe um livro com esse código.")
            return

    titulo = input("Digite o título do livro: ")

    if titulo == "":
        print("Título inválido.")
        return

    autor = input("Digite o nome do autor: ")

    if autor == "":
        print("Autor inválido.")
        return

    ano = int(input("Digite o ano de publicação: "))

    if ano > 2026:
        print("Ano de publicação inválido.")
        return

    quantidade = int(input("Quantos exemplares estão disponíveis? "))

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    livro = [codigo, titulo, autor, ano, quantidade]

    biblioteca.append(livro)

    print("\nLivro adicionado com sucesso!")


def excluir_livro():
    print("\n===== EXCLUIR LIVRO =====")

    if len(livros) == 0:
        print("Não existem livros cadastrados.")
        return

    codigo = input("Digite o código do livro que deseja excluir: ")

    for livro in livros:
        if livro["codigo"] == codigo:
            livros.remove(livro)
            print("Livro excluído com sucesso!")
            return

    print("Livro não encontrado.")


def listar_livros():
    print("\n===== LIVROS CADASTRADOS =====")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print("-----------------------------")
        print("Código:", livro["codigo"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Quantidade:", livro["quantidade"])

    print("-----------------------------")


def cadastro_livros():
    while True:
        print("\n================================")
        print("         MENU DE LIVROS")
        print("================================")
        print("1 - Adicionar livro")
        print("2 - Excluir livro")
        print("3 - Listar livros")
        print("4 - Voltar ao menu principal")
        print("5- listar livros")
        print("6- excluir livros")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()

        elif opcao == "2":
            excluir_livro()

        elif opcao == "3":
            listar_livros()

        elif opcao == "4":
            print("Voltando ao menu principal...")
        elif opcao == "5":
            print("listar livros")
        elif opcao=="6":
            print=("excluir livros")
            break

        else:
            print("Opção inválida.")
