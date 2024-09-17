import json
with open('dados.json', 'r') as file:
    faturamentos = json.load(file)
 
dias_faturamento = [dia['valor'] for dia in faturamentos if dia['valor'] > 0]

menor_val = min(dias_faturamento)

maior_val = max(dias_faturamento)

media_mensal = sum(dias_faturamento) / len(dias_faturamento)


valor_acima_media = len([valor for valor in dias_faturamento if valor > media_mensal])

# Exibir resultados
print(f"Menor valor de faturamento: {menor_val}")
print(f"Maior valor de faturamento: {maior_val}")
print(f"Número de dias com faturamento acima da média mensal: {valor_acima_media}")