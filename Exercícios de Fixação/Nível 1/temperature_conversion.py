while True:
    temp = input("Insira uma temperatura (Cº) ou digite 'pronto' para finalizar o programa: ")

    if temp.lower() == "pronto":
        break

    try:
        c = float(temp)
    except ValueError:
        print("Erro: o valor inserido não é um número.\n")
        continue

    f = (c * 9/5) + 32

    print(f"{c:.1f}ºC equivalem {f:.1f}ºF.\n")

print("Encerrando...")