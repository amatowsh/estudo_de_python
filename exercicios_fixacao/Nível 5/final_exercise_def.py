def menu():
    def somar_numeros():
        x = ler_float("\nInsira um número: ")
        if x is None:
            return
        y = ler_float("Insira outro número: ")
        if y is None:
            return
        print(f"\nResultado da soma: {x + y}.")
        print("\n------------------------------")

    def tabuada():
        num = ler_int("\nInsira um número para que a tabuada seja criada: ")
        if num is None:
            return
        print(f"\nTabuada do {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
        print("\n------------------------------")

    def converter_temperatura():
        c = ler_float("\nInsira um valor para ser convertido de Celsius para Fahrenheit: ")
        if c is None:
            return
        f = (c * 9 / 5) + 32
        print(f"\n{c}ºC são {f}ºF.")
        print("\n------------------------------")

    def ler_float(msg):
        valor = input(msg)
        if not valor.strip():
            print("\nErro: não houve valor inserido.")
            return None
        try:
            return float(valor.replace(",", "."))
        except ValueError:
            print("\nErro: o valor inserido não é um número.")
            return None

    def ler_int(msg):
        valor = input(msg)
        if not valor.strip():
            print("\nErro: não houve valor inserido.")
            return None
        try:
            return int(valor)
        except ValueError:
            print("\nErro: o valor inserido não é um número inteiro.")
            return None

    while True:
        print("\n[1] Somar números\n[2] Tabuada\n[3] Conversão de temperatura\n[4] Sair")
        escolha = input("\nEscolha uma das opções acima: ")

        if not escolha.strip():
            print("\nErro: não houve valor inserido.")
            print("\n------------------------------")
            continue

        if escolha == "1":
            print("\nOpção escolhida: Somar números")
            somar_numeros()

        elif escolha == "2":
            print("\nOpção escolhida: Tabuada")
            tabuada()

        elif escolha == "3":
            print("\nOpção escolhida: Conversão de temperatura")
            converter_temperatura()

        elif escolha == "4":
            print("\nEncerrando...\n")
            break

        else:
            print("\nErro: opção inválida. Escolha uma das opções válidas ([1], [2], [3] ou [4]).")
            print("\n------------------------------")

menu()