def sum (x, y):
    try:
        num1 = float(x)
        num2 = float(y)
    except ValueError:
        print("Erro: pelo menos um dos valores inseridos não é um número.")
        return None
    else:
        soma = num1 + num2

        return soma
    
x = input("Insira um número: ")
print(f"Número inserido: {x}.\n")

y = input("Insira outro número: ")
print(f"Número inserido: {y}.\n")

resultado = sum(x, y)

if resultado is not None:
    print(f"Soma dos números inseridos: {sum(x, y)}.")