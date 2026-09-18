quantidade = int(input("Quantos livros deseja cadastrar? "))
contador = 0

while contador < quantidade:
    print(f"\n--- Cadastro do Livro {contador + 1} ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")

    print("\nDados do livro cadastrado:")
    print(f"• Título: {titulo}")
    print(f"• Autor: {autor}")
    print(f"• Ano: {ano}")

    contador += 1

print("\nCadastro finalizado!")