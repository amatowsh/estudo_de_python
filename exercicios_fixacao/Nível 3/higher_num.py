raw1 = input("Entre com um número: ")
raw2 = input("Entre com mais outro número: ")
raw3 = input("Entre com um último número: ")

try: 
    num1 = int(raw1)
    num2 = int(raw2)
    num3 = int(raw3)
except ValueError:
    print("Erro: o valor inserido não é um número.")
else:
    if num1 > num2 and num1 > num3:
        print(f"{num1} é o maior entre os números inseridos.")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} é o maior entre os números inseridos.")
    else:
        print(f"{num3} é o maior entre os números inseridos.")

# se o 'else' não for usado no tratamento de exceções,
# o código tentará fazer as comparações mesmo após uma falha,
# o que resultará em um erro NameError, pois as variáveis podem
# não ter sido definidas durante o bloco 'try' (só existem após o try)
