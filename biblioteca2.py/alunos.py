def cadastro_alunos():
    print("Opção #2: Cadastro de alunos")
    print()

    qtd_alunos = int(input("Quantos alunos deseja cadastrar? "))

    for numero in range(1, qtd_alunos + 1):
        print(f"\n## Aluno #{numero} ##")

        matricula = input("Insira a matrícula do aluno: ")

        if matricula == "":
            print("Matrícula inválida. Reinicie a operação.")
            continue

        print("Matrícula:", matricula)

        nome_aluno = input("Digite o nome completo do(a) aluno(a): ")

        if nome_aluno == "":
            print("Aluno desconhecido. Reinicie a operação.")
            continue

        print("Nome:", nome_aluno)

        curso = input("Digite o nome do curso em que ele(a) está matriculado(a): ")

        if curso == "":
            print("Curso não identificado. Reinicie a operação.")
            continue

        print("Curso:", curso)
        print("Aluno cadastrado!")

    print("Operação concluída!")