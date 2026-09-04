#declaracao de variaveis, conversao e entrada  de dados pelo usuario#

nome= input("informe seu nome")
idade=int(input("informe sua idade:"))
altura=float(input("informe sua altura:"))

#implementaçao 1
print("o nome informado foi:", nome)
print("a idade informada foi:", idade)
print("a altura informada foi:", altura)

#implementaçao 2
print(f"o nome informado foi:{nome}")
print(f"a idade informada foi: {idade}")
print(f"a altura informada foi: {altura}")

##condicional
if idade >=18:
    print("voto obrigatorio")
else:
    print("voto nao obrigatorio")
    