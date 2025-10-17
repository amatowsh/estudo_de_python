soma = 0

while True:
    num = input("Insira um número ímpar para ser somado aos ímpares ou um par para finalizar o programa: ")

    try:
        x = int(num)
    except ValueError:
        print("Erro: insira um número inteiro.\n")
        continue

    if x % 2 == 0:
        break

    soma += x

    print(f"\nA soma dos ímpares resultou em {soma}.\n")

print("Encerrando...")