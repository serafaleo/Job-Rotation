# -*- coding: utf-8 -*-

import json

def main():
    with open("dados.json") as json_file:
        dados = json.load(json_file)

    menor = float('inf')
    maior = 0
    soma = 0
    n = 0

    for dado in dados:
        valor = float(dado["valor"])

        if valor > 0.0:
            n += 1
            soma += valor

        if valor < menor:
            menor = valor

        if valor > maior:
            maior = valor

    print(f"O menor valor de faturamento é {menor}.")
    print(f"O maior valor de faturamento é {maior}.")

    média = soma/n
    dias_superior = 0

    for dado in dados:
        valor = float(dado["valor"])
        if valor > média:
            dias_superior += 1

    print(f"O valor de faturamento diário foi superior à média mensal em {dias_superior} dias.")


if __name__ == "__main__":
    main()
