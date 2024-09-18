# Target Sistemas
Todas resoluções da tarefa estão nesse repositório, incluindo os dados da questão 3. 


## Primeira tarefa: Cálculo da Soma


Considere o seguinte trecho de código:

```plaintext
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);  
```

### Resolução:
#### Saída:
```
91
``` 

A resposta é 91 




## 2) Verificação na Sequência de Fibonacci

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

### Resolução em Python:

```python
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
```



## 3) Análise de Faturamento Diário

Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

**IMPORTANTE:**
a) Usar o JSON ou XML disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

### Resolução em python, observação, deverá ser utilizada os dados "dados.json".

```python
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
``` 


## 4) Cálculo do Percentual de Representação

Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

### Resolução em python, observação, foi utilizado os dados disponiblizados.

```python 
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
``` 

## 5) Inversão de String

Escreva um programa que inverta os caracteres de uma string.

*IMPORTANTE:*
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse.

### Resolução em python 
```python 
string = input("Digite alguma palavra e ela será invertida: ")
string_invertida = string[::-1]
print(string_invertida)
``` 


