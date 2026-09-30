import livros
import alunos
import emprestimo

biblioteca = []

while True:
    print()
    print("====================================")
    print("       SISTEMA PARA BIBLIOTECA")
    print("====================================")
    print("1 - Cadastro de livros")
    print("2 - Cadastro de alunos")
    print("3 - Realizar empréstimo")
    print("4 - Excluir livro")
    print("5 - Listar livros")
    print("6 - Sair")
    print("====================================")

    opcao_menu = input("Escolha uma opção: ")
    print()

    if opcao_menu == "1":
        livros.adicionar_livro(biblioteca)

    elif opcao_menu == "2":
        alunos.cadastro_alunos()

    elif opcao_menu == "3":
        emprestimo.realizar_emprestimo()

    elif opcao_menu == "4":
        livros.excluir_livro(biblioteca)

    elif opcao_menu == "5":
        livros.listar_livros(biblioteca)

    elif opcao_menu == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Número inválido. Escolha uma opção de 1 a 6.")