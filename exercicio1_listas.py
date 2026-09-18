#criaçao de lista vazia
notas=[]

#2 ler 5 notas e adiçao com append()
for i in range(5):
    nota=float(input(f"digite a nota:"))
    notas.append(nota)

#3 exibiçao de todas as notas cadastradas
print("notas cadastradas:")
for nota in notas:
    print(f"nota")

#4 quantidade de notas armazenadas
quantidade=len(notas)
print(f"quantidade de notas armazenadas:quantidade")

#5 maior e menor nota
maior_nota=max(notas)
menor_nota=min(notas)

print(f"maior nota:maior_nota")
print(f"menor nota:menor_nota")

