
#entrada4entrada
aluno= str(input("digite o nome do/a aluno:"))
idade=int(input("qual a idade dele/a"))
cadastro=str(input("o/a aluno esta cadastrada/o? S/N"))
 
#saida
if(cadastro=="n"):
    print(f"o/a aluno/a{aluno}nao possui cadastro no laboratorio. Assim, acesso nao negado.")
elif(cadastro=="s"):
    if(idade>=18):
        print(f"o/a aluno{aluno} tem acesso permitido a esse laboratorio.")
elif(idade>=14):
    print(f"o/a aluno {aluno} tem acesso a esse laboratorio.")
else:
    print(f"o/a aluno/a {aluno} tem acesso a esse laboratorio, apenas com a presença de uma pessoa.")
print("dados do cadastro errado. Tente novamente.")

