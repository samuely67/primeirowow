def adicionar_livro(biblioteca):
    print("\n===== ADICIONAR LIVRO =====")

    codigo = input("Insira o código do livro: ")

    if codigo == "":
        print("Código inválido.")
        return

    # Verifica se o código já existe na lista
    for livro in biblioteca:
        if livro["codigo"] == codigo:
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

    # Salva o livro como dicionário
    livro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "quantidade": quantidade
    }

    biblioteca.append(livro)
    print("\nLivro adicionado com sucesso!")


def excluir_livro(biblioteca):
    print("\n===== EXCLUIR LIVRO =====")

    if len(biblioteca) == 0:
        print("Não existem livros cadastrados.")
        return

    codigo = input("Digite o código do livro que deseja excluir: ")

    for livro in biblioteca:
        if livro["codigo"] == codigo:
            biblioteca.remove(livro)
            print("Livro excluído com sucesso!")
            return

    print("Livro não encontrado.")


def listar_livros(biblioteca):
    print("\n===== LIVROS CADASTRADOS =====")

    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in biblioteca:
        print("-----------------------------")
        print("Código:", livro["codigo"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Quantidade:", livro["quantidade"])

    print("-----------------------------")