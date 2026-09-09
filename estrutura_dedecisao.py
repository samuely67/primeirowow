#entrada1
usuario=str(input("digite o nome do usuario:"))
tempo_problema=int(input("por quanto tempo esta com o problema:"))

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


#entrada3
cliente=str(input("digite o nome do cliente"))
contrato=float(input("velocidade de banda larga contratada"))

#nivel3 do problema

velocidade_solicitada=int(input("quantidade de banda larga?)(1 plano ultra, 2 plano avançado ,3 plano intermediario, 4 plano basico)"))

saidas
print(f"a internet{internet}contratada{banda larga}mbps.")
if(plano ultra>=500 mbps):
   print("plano ultra")
if(plano avançado<=500 mbps):
   print("plano avançado")
if(plano intermediario<=198 mbps):
   print("plano intermediario")
if(plano_basico<=50 mbps):
    print("plano basico")


#entrada4entrada
aluno= str(input("digite o nome do/a aluno:"))
idade=int(input("qual a idade dele/a"))
cadastro=str(input("o/a aluno esta cadastrada/o? S/N"))

#saidas
if()
