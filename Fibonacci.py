def verifica_fibo(numero):
    if numero < 0:
        print("Não é um número válido")
        return

    a, b = 0, 1
    while a <= numero:
        if a == numero:
            print(f"Sim. {numero} é um número de fibonacci.")
            return
        a, b = b, a + b

    print(f"Não. {numero} não é um número de fibonacci.")

try:
    numero = int(input("Digite um número inteiro para saber se é de fibonacci: "))
    verifica_fibo(numero)
except ValueError:
    print("Por favor, digite um número inteiro válido.")