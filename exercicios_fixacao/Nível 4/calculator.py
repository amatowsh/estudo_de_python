def calculator(x, y, operator):

    try: 
        num1 = float(x)
        num2 = float(y)
    except ValueError:
        print("\nErro: o valor inserido não é um número.")
    else:

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("\nErro: divisão por zero não é permitido.")
                return None
        else:
            print("\nErro: operador inválido. Use +, -, * ou /.")
            return None
        
        return result
    
raw1 = input("Insira um número: ")
raw2 = input("Insira um segundo número: ")
oper = input("Agora insira um operador (+, -, *, /): ")

resultado = calculator(raw1, raw2, oper)

if resultado is not None:
    print(f"\nO resultado da operação desejada é: {resultado}.")

print("\nEncerrando...")