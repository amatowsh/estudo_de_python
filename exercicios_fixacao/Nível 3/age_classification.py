while True:
    raw = input("Insira uma idade para ser classificada (ou 'ok' para finalizar o programa): ")

    if raw.lower() == "ok":
        break

    try:
        age = int(raw)
    except ValueError:
        print("Erro: o valor inserido não é um número.\n")

    if age >= 0 and age <= 11:
        print("É uma criança.\n")
    elif age >= 12 and age <= 18:
        print("É um adolescente.\n")
    elif age >= 19 and age <= 59:
        print("É um adulto.\n")
    elif age >= 60 and age <= 100:
        print("É um idoso.\n")
    else:
        print("Essa idade é inexistente ou muito difícil de ser alcançada.\n")

print("Encerrando...")