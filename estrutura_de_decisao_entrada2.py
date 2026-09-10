#entrada2 nivel do problema

tipo_do_problema=int(input("qual o tipo de problema?(1 indisponibilidade total, 2 lentidao, 3 problema que nao impede o trabalho, 4 outros)"))

saidas
 print(f"o usuario {usuario}reporta o prblema em seu pc ha{tempo_problema}dias.")
if(tipo_do_problema==4):
    print("problema:indisponibilidade total // prioridade:critico")
elif(tipo_do_problema==3):
    print("problema:lentidao //prioridade:alta")
elif(tipo_do_problema==2):
   print("problema:simples,que nao dificulta o trabalho // prioridade:media")
else:
   print("outros problemas // prioridade:baixa")

#entrada2 estoque
nome=str(input("digite o nome do produto:"))
quantidade=int(input("digite a quantidade disponivel"))

#saida
print(f"o produto{produto}esta com o estoque de{quantidade}unidades.")
if(quantidade>=20):
print("normal")
if(quantidade<=20):
   print("estoque baixo")
if(quantidade<=4):
   print("estoque critico")