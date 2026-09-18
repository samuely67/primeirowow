nomes=["aju", "caju", "paku"]
#indice 0, 1, 2#
idade=[13, 14, 15]
peso=[34, 43, 21]

print(nomes[0]) #aju
print(nomes[-1]) #paku

#acessar uma posiçao que nao exista provoca um erro.
#para conhecer o tamanho da lista, se usa o len().
print(len(nomes))


nomes =["ana", "carlos", "joao" ]
nomes[1]="pedro"
print(nomes)
#["ana", "pedro", "joao"]

#adicionar elementos
nomes.append("maria")

#adicionar no final da lista insert().
nomes.insert(1, "lucas")

#para remover se usa o remove(), e pop() para trabalhar em uma posiçao
nomes.remove("pedro")
nomes.pop(0)

#o for faz com que o codigo seja executado para cada item da lista
nomes=["ana","carlos", "joao"]
for nome in nomes:
print(nome)

#percorrendo numeros
idades=[15,16,17]
for idade in idade:
    print(idade)

#calculos durante a repetiçao
notas=[5,7]
soma=0
for nota in notas:
    soma=soma+nota
    print(soma)



