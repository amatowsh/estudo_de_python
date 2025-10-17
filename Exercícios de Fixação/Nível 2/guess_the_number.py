resposta = 7
while True:
    temp = input("Tente adivinhar o número: ")

    try:
        num = int(temp)
    except ValueError:
        print("Erro: insira um número inteiro.")
        continue

    if num > resposta:
        print("O número é maior.\n")
    elif num < resposta:
        print("O número é menor.\n")
    else:
        print("Você acertou!\n")
        break

print("Encerrando...")