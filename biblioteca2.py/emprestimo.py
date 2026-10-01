historico_emprestimos = []

def realizar_emprestimo():
    print("Opção #3: Empréstimo de livros")
    print()

    codigo = input("Insira o código de cadastro do livro: ")

    if codigo == "":
        print("Código inválido. Reinicie a operação.")
        return

    print("Código do livro:", codigo)

    matricula = input("Insira o número de matrícula do aluno: ")

    if matricula == "":
        print("Matrícula inválida. Reinicie a operação.")
        return

    print("Matrícula:", matricula)

    qtd_cadastro = int(input("Quantos livros estão disponíveis? "))

    if qtd_cadastro > 0:
        registro = {
            "codigo_livro": codigo,
            "matricula_aluno": matricula,
            "status": "Emprestado"
        }
        historico_emprestimos.append(registro)
        print("Empréstimo realizado com sucesso!")
    else:
        print("Não é possível realizar o empréstimo. Não há livros disponíveis.")

    print("Operação concluída!")


def devolver_livro():
    print("\n===== DEVOLUÇÃO DE LIVRO =====")

    if not historico_emprestimos:
        print("Não há empréstimos registrados no sistema.")
        return

    matricula = input("Insira a matrícula do aluno: ")
    codigo = input("Insira o código do livro a devolver: ")

    for emprestimo in historico_emprestimos:
        if (emprestimo["matricula_aluno"] == matricula and 
            emprestimo["codigo_livro"] == codigo and 
            emprestimo["status"] == "Emprestado"):
            
            emprestimo["status"] = "Devolvido"
            print("Devolução realizada com sucesso!")
            return

    print("Nenhum empréstimo ativo foi encontrado com esses dados.")


def listar_emprestimos():
    print("\n===== RELATÓRIO DE EMPRÉSTIMOS =====")

    if not historico_emprestimos:
        print("Nenhum registro de empréstimo até o momento.")
        return

    for idx, emp in enumerate(historico_emprestimos, start=1):
        print("-----------------------------")
        print(f"Empréstimo #{idx}")
        print("Código do Livro:", emp["codigo_livro"])
        print("Matrícula do Aluno:", emp["matricula_aluno"])
        print("Status:", emp["status"])

    print("-----------------------------")