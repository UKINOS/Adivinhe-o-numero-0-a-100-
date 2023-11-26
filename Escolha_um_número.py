import random
import Filtro_de_números as F

print("Vamos jogar um jogo de adivinhe o número")
print("Escolha um número entre 1 e 100")

tentativas = 3

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

numeros_possíveis = list(range(1, 101))

print("Escolha a dificuldade:")
print("--------------------------------")
print("1. Fácil             10. Dificíl")
dificuldade = F.numeros(1,10,1)
if dificuldade == 10:
    numerose = 10
else:
    numerose = 1

#INTELIGÊNCIA ARTIFICIAL?
while tentativas != 0:
    if (random.randint(numerose,dificuldade)%2) == 1:
        if tentativas == 3:
            print("Quantas casas tem o número?")
            casas = F.numeros(1,3,1)
            if casas == 3:
                numeros_possíveis.clear()
                numeros_possíveis.append(100)
            if casas == 2:
                for n in range(1,10):
                    numeros_possíveis.remove(n)
                numeros_possíveis.remove(100)
            if casas == 1:
                numeros_possíveis.clear()
                for n in range(1,10):
                    numeros_possíveis.append(n)
        elif tentativas == 2:
            print("Possuí algum zero na casa da unidade?\n1. Sim\n2. Não")
            temp = [0]
            if F.numeros(1,2,1) == 1:
                for n in numeros_possíveis:
                    if n % 10 != 0:
                        temp.append(n)
                for n in temp:
                    if n in numeros_possíveis:
                        numeros_possíveis.remove(n)
            else:
                for n in numeros_possíveis:
                    if n % 10 == 0:
                        temp.append(n)
                for n in temp:
                    if n in numeros_possíveis:
                        numeros_possíveis.remove(n)
        elif tentativas == 1:
            print("Esse número é primo?\n1. Sim\n2. Não")
            temp = [0]
            if F.numeros(1,2,1) == 1:
                for n in numeros_possíveis:
                    if n not in primos:
                        temp.append(n)
                for n in temp:
                    if n in numeros_possíveis:
                        numeros_possíveis.remove(n)
            else:
                for n in numeros_possíveis:
                    if n in primos:
                         temp.append(n) #69 :)
                for n in temp:
                    if n in numeros_possíveis:
                        numeros_possíveis.remove(n)
    else:
        if tentativas == 3:
            print("Este número é maior que 50?\n1. É maior que 50\n2. É menor ou igual a 50")
            if F.numeros(1,2,1) == 1:
                for n in range(1,51):
                    if n in numeros_possíveis:
                        numeros_possíveis.remove(n)
            else:
                for n in range(51,101):
                    if n in numeros_possíveis:
                        numeros_possíveis.remove(n)
        elif tentativas == 2:
            print("É impar ou par?\n1. Impar\n2. Par")
            temp = [0]
            if F.numeros(1,2,1) == 1:
                for n in numeros_possíveis:
                    if n % 2 == 0:
                        temp.append(n)
                for n in temp:
                    if n in numeros_possíveis:
                        numeros_possíveis.remove(n)
            else:
                for n in numeros_possíveis:
                    if n % 2 == 1:
                        temp.append(n)
                for n in temp:
                    if n in numeros_possíveis:
                        numeros_possíveis.remove(n)
        elif tentativas == 1:
            print("Quanto é a soma dos números?")
            temp = [0]
            soma = F.numeros(1,18,1)
            for n in numeros_possíveis:
                z = str(n)
                if len(z) > 1:
                    b = z[1]
                    a = z[0]
                    if (int(a) + int(b)) != soma:
                        temp.append(n)
                elif n != soma and len(z) == 1:
                    temp.append(n)
            for n in temp:
                if n in numeros_possíveis:
                    numeros_possíveis.remove(n)

    if len(numeros_possíveis) < 2:
        tentativas = 0
    else:
        tentativas -= 1

#HORA DE VER SE ELE SABE OU NÃO
if len(numeros_possíveis) == 0:
    print("Vc provavelmente respondeu algo errado, já que não há nenhum número que se encaixe nessa descrição }:(")
elif len(numeros_possíveis) == 1:
    print(f"O seu número é {numeros_possíveis[0]}?\n1. Sim\n2. Não")
    if F.numeros(1,2,1) == 1:
        print("Oba, mais uma vitória pra mim!")
        print("Depois de pensar um pouco, eu soube qual era a resposta :)")
    else:
        print("Mentiroso! Cai fora }=(")
else:
    max = ((len(numeros_possíveis)) - 1)
    Chute = random.randint(0,max)
    print(f"O seu número é {numeros_possíveis[Chute]}?\n1. Sim\n2. Não")
    if F.numeros(1,2,1) == 1:
        print("Oba, mais uma vitória pra mim!")
    else:
        print("Ops, qual era seu número?")
        resposta_correta = F.numeros(1,100,1)
        if resposta_correta == numeros_possíveis[Chute]:
            print("Mas... esse é o número q eu chutei...")
        elif resposta_correta in numeros_possíveis:
            print("Meu chute foi errado, eu estava com dificuldade de descobrir qual era o número :(")
        else:
            print("Você provavelmente respondeu algo errado, pois eu não estou achando na minha lista o número mencionado :(")    
    print(f"Segue abaixo a lista de números que eu tinha em mente:\n{numeros_possíveis}")
input("Aperte enter para fechar o programa...")
