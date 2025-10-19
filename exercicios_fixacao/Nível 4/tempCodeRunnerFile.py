def converter(x):

    try:
        num = float(x)
    except ValueError:
        print("\nErro: o valor inserido não pode ser convertido.")
        return None
    
    return num
    
raw = input("Entre com um número inteiro para ser convertido para ponto flutuante: ")

resultado = converter(raw)

if resultado is not None:
    print(f"\nInteiro: {raw}.\nPonto flutuante: {resultado}.")

print("\nEncerrando...")