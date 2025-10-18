while True:
    x = input("Insira um número para classificá-lo entre par ou ímpar: ")

    try:
        num = int(x)
    except ValueError:
        print("Erro: o valor inserido não é um número.\n")
    else:
        if num == 0:
            print("Encerrando...")
            break

        if num % 2 == 0:
            print("É par.\n")
        else:
            print("É ímpar.\n")