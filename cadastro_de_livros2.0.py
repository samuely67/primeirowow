# Lista para armazenar os livros cadastrados
biblioteca = []

while True:
    print("--sistema de biblioteca--")
    print("1 -cadastrar livros")
    print("2 - listar livros")
    print("3 - pesquisar livros")
    print("4 - alterar livro")
    print("5 - excluir livros")
    print("6 - sessao finalizada")

    opcao = input("escolha uma opçao:")

    # 1 - cadastro de livros
    if opcao == "1":
        print("\n--- Cadastro de Novo Livro ---")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação: ")

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano
        }
        biblioteca.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!\n")

    # 2 - LISTAR LIVROS (Read)
    elif opcao == "2":
        print("\n--- Lista de Livros ---")
        if not biblioteca:
            print("Nenhum livro cadastrado na biblioteca.\n")
        else:
            for i, livro in enumerate(biblioteca):
                print(f"[{i}] Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")
            print()

    # 3 - PESQUISAR LIVROS (Read por título)
    elif opcao == "3":
        print("\n--- Pesquisar Livro ---")
        termo = input("Digite o título (ou parte dele) para buscar: ")
        encontrados = [l for l in biblioteca if termo in l["titulo"]]

        if not encontrados:
            print("Nenhum livro encontrado com esse termo.\n")
        else:
            print(f"\nEncontrados {len(encontrados)} resultado(s):")
            for livro in encontrados:
                print(f"- Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")
            print()

    # 4 - ALTERAR LIVRO (Update)
    elif opcao == "4":
        print("\n--- Alterar Livro ---")
        if not biblioteca:
            print("Nenhum livro cadastrado para alterar.\n")
        else:
            for i, livro in enumerate(biblioteca):
                print(f"[{i}] {livro['titulo']}")
            
            try:
                indice = int(input("Digite o número (índice) do livro que deseja alterar: "))
                if 0 <= indice < len(biblioteca):
                    print(f"Alterando o livro: {biblioteca[indice]['titulo']}")
                    novo_titulo = input("Novo título (deixe em branco para manter): ")
                    novo_autor = input("Novo autor (deixe em branco para manter): ")
                    novo_ano = input("Novo ano (deixe em branco para manter): ")

                    if novo_titulo != "":
                        biblioteca[indice]["titulo"] = novo_titulo
                    if novo_autor != "":
                        biblioteca[indice]["autor"] = novo_autor
                    if novo_ano != "":
                        biblioteca[indice]["ano"] = novo_ano

                    print("Livro atualizado com sucesso!\n")
                else:
                    print("Índice inválido!\n")
            except ValueError:
                print("Por favor, digite um número válido.\n")

    # 5 - EXCLUIR LIVROS (Delete)
    elif opcao == "5":
        print("\n--- Excluir Livro ---")
        if not biblioteca:
            print("Nenhum livro cadastrado para excluir.\n")
        else:
            for i, livro in enumerate(biblioteca):
                print(f"[{i}] {livro['titulo']}")
            
            try:
                indice = int(input("Digite o número (índice) do livro que deseja excluir: "))
                if 0 <= indice < len(biblioteca):
                    removido = biblioteca.pop(indice)
                    print(f"Livro '{removido['titulo']}' excluído com sucesso!\n")
                else:
                    print("Índice inválido!\n")
            except ValueError:
                print("Por favor, digite um número válido.\n")

    # 6 - SESSÃO FINALIZADA
    elif opcao == "6":
        print("\nSessão finalizada. Até logo!")
        break

    else:
        print("\nOpção inválida! Escolha um número entre 1 e 6.\n")