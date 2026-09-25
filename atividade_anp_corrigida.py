#CADASTRO DE LIVROS!#
livros = []
import datetime
x= datetime.datetime.now()
print(x)
ano_max = x.year

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        
        # Correção da condição
        if titulo == "" or autor == "":
            print("erro: titulo e autor nao podem estar vazios!!!!")
        else:
            livros.append({"titulo": titulo, "autor": autor})
            print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- Livros Cadastrados ---")
        if len(livros) == 0:
            print("Nenhum livro cadastrado ainda.")
        else:
            for i, livro in enumerate(livros, 1):
                # Correção: livro['titulo'] no lugar de livro['livro']
                print(f"{i}. Título: {livro['titulo']} | Autor: {livro['autor']}")

    elif opcao == "3":
        pesquisa = input("Digite o título que deseja pesquisar: ")
        encontrado = False

        for livro in livros:
            if livro["titulo"] == pesquisa:
                print("\nLivro encontrado!")
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                encontrado = True
                break  # O break precisa estar recuado DENTRO do if

        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "4":
        pesquisa = input("Digite o título que deseja excluir: ")
        encontrado = False

        for livro in livros:
            if livro["titulo"] == pesquisa:
                livros.remove(livro)
                print("livro excluído com sucesso!!!!!!")
                encontrado = True
                break
        
        if not encontrado:
            print("Livro não encontrado para exclusão.")

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida! Escolha um número de 1 a 5.")