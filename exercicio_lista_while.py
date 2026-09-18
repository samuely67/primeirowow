#exercicio 1
contador = 1
while contador <=10:
    print(contador)
    contador=contador+1

#exercicio 2
contador = 2
while contador <= 20:
    print(contador)
    contador += 2

#exercicio 3
total_alunos=int(input("quantos alunos serao cadastrados?"))
contador=0
while contador<=2:
    print(contador)
    contador+= 2

#exercicio 4 menu simples#
opcao = ""

while opcao != "3":
    print("==MENU==")
    print("1 — Cadastrar livro")
    print("2 — Listar livros")
    print("3 — Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Opção selecionada: Cadastrar livro")
    elif opcao == "2":
        print("Opção selecionada: Listar livros")
    elif opcao == "3":
        print("Saindo do sistema...")
    else:
        print("Opção inválida! Tente novamente.")
    
#exercicio 5 validaçao
idade = int(input("Digite a sua idade: "))

while idade < 0 or idade > 90:
    print("Idade inválida! O valor deve estar entre 0 e 90.")
    idade = int(input("Digite a sua idade novamente: "))

print(f"idade válida cadastrada: {idade}")

#exercicio 6
senha_correta = "1234" 
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta! Tente novamente.")
    senha = input("Digite a senha: ")
print("Acesso permitido!")

