# Sistema de controle da biblioteca

def saudacao():
    print("1- oiiiiii!")
    print("2- como vai?")
    print("3- nooooossa!")
    print("4- tchau")

def passa_teu_contato(sim_nao):
    if sim_nao == "sim":
        return "Contato salvo: (67) 67676767"
    else:
        return "Contato não fornecido."

# Como usar:
saudacao()

resultado = passa_teu_contato("sim")
print(resultado)
def passa_teu_contato():
    resposta = input("Deseja passar seu contato? (sim/nao): ")
    
    if resposta == "sim":
        num = input("Digite seu telefone: ")
        return f"Contato {num} cadastrado com sucesso!"
    else:
        return "Operação cancelada."

# Como usar:
resultado = passa_teu_contato()
print(resultado)