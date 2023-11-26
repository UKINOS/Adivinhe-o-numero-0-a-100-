import random
import Filtro_de_números as F

print("Vamos jogar um jogo de adivinhe o número")
print("Eu escolhi um número entre 1 e 100")

número = random.randint(0, 100)

tentativas = 3

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,67, 71, 73, 79, 83, 89, 97]

def primo(número):
    for p in primos:
        if número == p:
            print("O número é primo")
            return
    print("O número não é primo")
    return

while tentativas != 0:
    print("\n\nO que vc vai perguntar?\n1. Quantas casas tem o número?\n2. Quanto é a soma dos números?\n3. Este número é maior que 50?\n4. Possuí algum zero na casa da unidade?\n5. Esse número não é primo?\n6. É impar ou par?\n7. \"JÁ SEI A RESPOSTA!\"")
    resposta = F.numeros(1,7,1)
    print("\n")
    if resposta == 1:
        print("O número possuí", len(str(número)), "casas")
        tentativas -= 1
    elif resposta == 2:
        numero_str = str(número)
        a = int(numero_str[0])
        b = int(numero_str[1])
        print("A soma dos números é de", a + b)
    elif resposta == 3:
        if número > 50:
            print("Esse número é maior que 50")
        else:
            print("Esse número é menor ou igual a 50")
    elif resposta == 4:
        if número % 10 == 0:
            print("O número possuí um 0 na casa da unidade")
        else:
            print("Nope, a casa da unidade não possuí um zero")
    elif resposta == 5:
        primo(número)
    elif resposta == 6:
        if número % 2 == 0:
            print("É par")
        else:
            print("É impar")
    
    if resposta == 7 or tentativas == 1:
        print("Então, nos diga qual é a resposta final!")
        resposta_final = F.numeros(1,100,1)
        if resposta_final == número:
            print("Parabéns, vc acertou!")
        else:
            print(f"Vc errou, a resposta correta era {número}")

    tentativas -= 1

input("Aperte enter para fechar o programa")