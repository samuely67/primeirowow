#lista vazia
produtos=[]

#leitura dos produtos
for i in range(4):
    nome=input(f"digite o nome do produto por favor:")
    produtos.append(nome)

#mostra os produtos numerados
print("-lista de produtos-")
for indice, produto in enumerate(produtos):
    print(f"{indice},{produto}")

#pesquisa de um produto
termo_busca=input("digite o nome de um produto para pesquisar:")
if termo_busca in produtos:
    print(f"o produto nao foi encontradi na lista!:")
else:
    print(f"o produto NAOO foi encontrado.")

#quantidade total de produtos cadastrados
print(f"total de produtos cadastrados:")

#remoçao do produto
produto_remover=input("digite o nome do produto que quer remover:")
if produto_remover in produtos:
    produtos.remove(produto_remover)
    print("produto removido com sucesso!!!")
    print(f"nova quantidade de produtos cadastrados")

    #lista atualizada 
    print("lista atualizda")

    for indice, produto in enumerate(produtos, start=1):
        print(f"indice, produto")
    else:
        print(f"nao foi possivel remover:nao pertence a lista.")




