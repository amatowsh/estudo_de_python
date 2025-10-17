num = input("Insira um número: ")

try:
    x = int(num)
except ValueError:
    print("Erro: insira um número inteiro.")
else:
    for i in range (1, 11):
        
        mult = x * i

        if i == 5:
            continue

        print(f"{x} x {i} = {mult}")

# Curiosidade: dá pra usar a seguinte estrutura

# try -> tenta executar o código que pode falhar.
# except -> captura e trata os erros.
# else -> executa apenas se nenhum erro ocorreu.
# finally -> executa sempre, aconteça erro ou não.