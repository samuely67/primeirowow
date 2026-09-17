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

#para eremover se usa o remove(), e pop() para trabalhar em uma posiçao
nomes.remove("pedro")
nomes.pop(0)

