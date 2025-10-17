while True:

    num1 = input("Insira um número: ")
    num2 = input("Insira outro número: ")

    if "pronto" in (num1.lower(), num2.lower()): #lower pra deixar em lower case
        break

    print(num1)
    print(num2)

    try:
        x = float(num1)
        y = float(num2)
    except ValueError:
        print("Erro: um dos valores não é um número.\n")
        continue

    soma = x + y
    print(f"Números a serem somados: {x} e {y}")
    print(f"Soma: {soma}\n")

print("Encerrando...")