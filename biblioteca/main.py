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
    print("4 - excluir livros")
    print("5- listar livros")
    print("6- sair")
    print("====================================")

    opcao_menu = input("Escolha uma opção: ")
    print()

    if opcao_menu == "1":
        livros.adicionar_livro(biblioteca)

    elif opcao_menu == "2":
        cadastro_alunos()

    elif opcao_menu == "3":
        realizar_emprestimo()

    elif opcao_menu == "4":
        print("Você excluiu livros.")
    elif opcao_menu =="5":
        print("listar livros")
    elif opcao_menu =="6":
        print("sair")
        break

    else:
        print("Número inválido. Escolha uma opção de 1 a 4.")
