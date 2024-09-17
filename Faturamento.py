faturamento = {
    "São Paulo": 67836.43,
    "Rio de Janeiro": 36678.66,
    "Minas Gerais": 29229.88,
    "Espírito Santo": 27165.48,
    "Outros": 19849.5
}

def faturamento_amostra():
    soma = sum(faturamento.values())
    print(f"A soma de todos os valores do faturamento é: {soma:.2f}")

    porcentagem = {estado: (valor / soma) * 100 for estado, valor in faturamento.items()}

    for estado, perc in porcentagem.items():
        print(f"{estado}: {perc:.2f}%")

faturamento_amostra()