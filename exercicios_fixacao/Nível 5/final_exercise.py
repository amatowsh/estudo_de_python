while True:

    print("\n[1] Somar números\n[2] Tabuada\n[3] Conversão de temperatura\n[4] Sair")
    numChoosen = input("\nEscolha uma das opções acima: ")

    if not numChoosen.strip():
        print("\nErro: não houve valor inserido.")
        print("\n------------------------------")
        continue

    if numChoosen == "1":
        print("\nOpção escolhida: Somar números")

        x = input("\nInsira um número: ")
        y = input("Insira outro número: ")

        try:
            num1 = float(x)
            num2 = float(y)
        except ValueError:
            print("\nErro: o valor inserido não é um número.")
            print("\n------------------------------")
            continue
        else:
            result = num1 + num2

            print(f"\nResultado da soma: {result}.")
            print("\n------------------------------")

    elif numChoosen == "2":
        print("\nOpção escolhida: Tabuada")

        x = input("\nInsira um número para que a tabuada seja criada: ")

        try:
            num = int(x)
        except ValueError:
            print("\nErro: o valor inserido não é um número.")
            print("\n------------------------------")
            continue
        else:
            print(f"\nTabuada do {num}:")

            for i in range(1, 11):

                result = num * i

                print(f"\n{num} x {i} = {result}")

            print("\n------------------------------")

    elif numChoosen == "3":
        print("\nOpção escolhida: Conversão de temperatura")

        x = input("\nInsira um valor para ser convertido de Celsius para Fahrenheit: ")

        try:
            c = float(x)
        except ValueError:
            print("\nErro: o valor inserido não é um número.")
            print("\n------------------------------")
            continue
        else:
            f = (c * 9 / 5) + 32

            print(f"\n{c}ºC são {f}ºF.")
            print("\n------------------------------")

    elif numChoosen == "4":
        print("\nEncerrando...\n")
        break

    else:
        print(
            "\nErro: opção inválida. Escolha uma das opções válidas ([1], [2], [3] ou [4])."
        )
        print("\n------------------------------")