## Avaliação 1: Sistema de controle de uma biblioteca
# Parte 0: Intro
print("     SISTEMA PARA BIBLIOTECA     ")

print("Opção 1: Cadastro de livros")
print("Opção 2: Cadastro de alunos")
print("Opção 3: Realizar Empréstimo")
print("Opção 4: Sair")

opcao_menu = int(input("Escolha uma opção: "))
print()

# Parte 1: Cadastro de livros
if(opcao_menu == 1):
    print("Opção #1: Cadastro de livros")

    qtd_livros = int(input("Quantos livros deseja cadastrar? "))
    for numero in range(1, qtd_livros + 1):
        print(f"### Livro #{numero} ###")

        codigo = str(input("Insira o código de cadastro: "))
        if(codigo == ""):
            print("Código inválido. Reinicie a operação.")
        else:
            print("Código:", codigo)

            titulo = str(input("Digite o título do livro: "))
            if(titulo == ""):
                print("Título vazio, reinicie a operação")
            else:
                print("Título: ", titulo)

                autor = str(input("Digite o nome do(s) autor(es): "))
                if(autor == ""):
                    print("Autor não identificado, reinicie a operação")
                else:
                    print("Autor(es): ", autor)

                    ano_publicacao = int(input("Digite o ano de publicação: "))
                    if(ano_publicacao > 2026):
                        print("Reinicie a operação, data errada!!")
                    else:
                        print("Ano de publicação: ", ano_publicacao)

                        qtd_cadastro = int(input("Quantos exemplares estão disponíveis? "))
                        if(qtd_cadastro > 0):
                            print("Quantidade: ", qtd_cadastro)
                            print("Livro cadastrado com sucesso!")
                        else:
                            print("Não consigo cadastrar zero livros. Reinicie a operação.")
    print("Operação concluída! Reinicie para outras operações.")

# Parte 2: Cadastro de alunos
elif(opcao_menu == 2):
    print("Opção #2: Cadastro de alunos")

    qtd_alunos = int(input("Quantos alunos deseja cadastrar? "))
    for numero in range(1, qtd_alunos + 1):
        print(f"### Aluno #{numero} ###")
        matricula = str(input("Insira a matrícula do aluno: "))
        if(matricula == ""):
            print("Matrícula inválida. Reinicie a operação.")
        else:
            print("Matricula:", matricula)

            nome_aluno = str(input("Digite o nome completo do(a) aluno(a): "))
            if(nome_aluno == ""):
                print("Aluno desconhecido, reinicie a operação")
            else:
                print("Nome: ", nome_aluno)
            
                curso = str(input("Digite o nome do curso em que ele(a) está matruculado(a): "))
                if(curso == ""):
                    print("Curso não identificado, reinicie a operação")
                else:
                    print("Curso: ", curso)
                    print("Aluno cadastrado!")
    print("Operação concluída! Reinicie para outras operações.")

# Parte 3: Empréstimo de livro
elif(opcao_menu == 3):
    print("Opção #3: Empréstimo de livros")

    codigo = str(input("Insira o código de cadastro: "))
    if(codigo == ""):
        print("Código inválido, reinicie a operação.")
    else:
        print("Código do livro: ", codigo)

        matricula = str(input("Insira o número de matrícula: "))
        if(matricula == ""):
            print("Matrícula inválida. Reinicie a operação.")
        else:
            print("Matrícula: ", matricula)
            qtd_cadastro = int(input("Quantos livros estão disponíveis? "))
            if(qtd_cadastro > 0):
                print("Empréstimo realizado com sucesso!")
            else:
                print("Não é possível realizar o empréstimo. Não há livros disponíveis.")
    print("Operação concluída! Reinicie para outras operações.")

# Parte 4: Sair + Opções erradas:
elif(opcao_menu == 4):
    print("Você saiu da operação. Reinicie para outras operações.")
else:
    print("Número inválido. Reinicie a operação.")

    