def realizar_emprestimo():
    print("Opção #3: Empréstimo de livros")
    print()

    codigo = input("Insira o código de cadastro: ")

    if codigo == "":
        print("Código inválido. Reinicie a operação.")
        return

    print("Código do livro:", codigo)

    matricula = input("Insira o número de matrícula: ")

    if matricula == "":
        print("Matrícula inválida. Reinicie a operação.")
        return

    print("Matrícula:", matricula)

    qtd_cadastro = int(input("Quantos livros estão disponíveis? "))

    if qtd_cadastro > 0:
        print("Empréstimo realizado com sucesso!")
    else:
        print("Não é possível realizar o empréstimo. Não há livros disponíveis.")

    print("Operação concluída!")