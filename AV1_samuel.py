print("SISTEMA DE CONTROLE DE BIBLIOTECA")
print("opçao 1- cadastrar livros")
print("opçao 2- cadastrar alunos")
print("opçao 3- realizar emprestimo")
print("opçao 4- sair")

opcao_menu= int(input("escolha_uma_opcao:"))
print("escolha uma opçao")

if opcao_menu == 1:
    quant_de_livros = int(input("Quantos livros deseja cadastrar?"))

    if opcao == "1":
        qtd = int(input("Quantos livros deseja cadastrar? "))
        for i in range(qtd):
            print(f"livro")
            codigo = input("codigo: ")
            titulo = input("titulo: ")
            autor = input("autor: ")
            ano = int(input("ano: "))
            quantidade = int(input("quantidade: "))
            
            if titulo == "":
                print("erro: titulo vazio.")
            elif autor == "":
                print("erro:autor vazio.")
            elif ano <= 0:
                print("erro:ano invalido.")
            elif quantidade <= 0:
                print("erro: quantidade deve ser maior que zero.")
            else:
                print("livro cadastrado com sucesso!")

    elif opcao == "2":
        qtd = int(input("quantos alunos deseja cadastrar? "))
        for i in range(qtd):
            print(f"ALUNO")
            matricula = input("matricula: ")
            nome = input("nome: ")
            turma = input("turma: ")
            
            if matricula == "":
                print("erro:matricula vazia.")
            elif nome == "":
                print("erro:nome vazio.")
            elif turma == "":
                print("erro:turma vazia.")
            else:
                print("aluno cadastrado com sucesso!")

    elif opcao == "3":
        print("emprestimo")
        codigo = input("codigo do livro: ")
        matricula = input("matricula do aluno: ")
        quantidade = int(input("quantidade disponivel: "))
        
        if codigo == "":
            print("erro:codigo nao informado.")
        elif matricula == "":
            print("erro:matricula nao informada.")
        elif quantidade > 0:
            print("emprestimo realizado com sucesso!")
        else:
            print("nao é preciso realizar o emprestimo.")
            print("nao há exemplares disponiveis.")

    elif opcao == "4":
        print("cabou meu nobre.")

    else:
        print("opçao invalida!")



