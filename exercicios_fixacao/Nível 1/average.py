while True:
    a = input("Insira a primeira nota (ou 'pronto' para sair): ")
    b = input("Insira a segunda nota: ")
    c = input("Insira a terceira nota: ")

    if "pronto" in (a.lower(), b.lower(), c.lower()):
        break

    try:
        n1, n2, n3 = float(a), float(b), float(c)

    except ValueError:

        print("Erro: o valor inserido não é um número.\n")
        continue

    media = (n1 + n2 + n3) / 3

    print(f"Média: {media:.2f}")
    print("Aluno aprovado!\n" if media >= 6 else "Aluno reprovado!\n")

print("Encerrando...")
