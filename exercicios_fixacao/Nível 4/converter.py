def converter(x):

    if not x.strip():
        print("Erro: não houve valor inserido.") 
        return None

    try:
        num = float(x.replace(",", "."))
    except ValueError:
        print("\nErro: o valor inserido não pode ser convertido.")
        return None
    
    return num
    
raw = input("Entre com um número inteiro para ser convertido para ponto flutuante: ")

resultado = converter(raw)

if resultado is not None:
    print(f"\nInteiro: {raw}.\nPonto flutuante: {resultado}.")

print("\nEncerrando...")

# strip() remove espaços em branco (e quebras de linha) no início e no fim da string
# em Python, strings vazias ("") são avaliadas como False em expressões booleanas
# portanto, se o que o usuário digitou for só espaços ou nada, x.strip() vira "",
# o que faz not x.strip() ser True e acionar o if