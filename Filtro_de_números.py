#Função roubada de outro código meu :)
def numeros(x, y, z):
    resposta = input(f"Escolha um número: ")
    while True:
        resposta2 = resposta.strip("-")
        resposta3 = resposta2.strip(" ")
        if resposta3.isdigit() == True:
            if x <= int(resposta3) <= y and z == 1:
                return int(resposta)
            elif z == 0:
                return int(resposta)
            else:
                resposta = input(f"Sua resposta tem que ser entre {x} e {y}: ")
        else:
            resposta = input(f"Sua resposta precisa ser em números naturais (sem espaços, letras, ou números inteiros): ")