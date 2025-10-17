while True:
    num = input("Insira ou número ou digite 'pronto' para finalizar o programa: ")

    if num.lower() == "pronto":
        break

    try:
        n = int(num)
    except ValueError:
        print("Erro: insira um número inteiro.")
        continue

#   Caso 1: Estrutura For
#   for i in range(1, n+1):
#       print(i)

#   Caso 2: Estrutura While
#   i = 1
#   while i <= n:
#       print(i)
#       i += 1

print("Encerrando...")