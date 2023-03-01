# -*- coding: utf-8 -*-

def main():
    dados = [{"Estado": "SP", "Faturamento": 67836.43},
             {"Estado": "RJ", "Faturamento": 36678.66},
             {"Estado": "MG", "Faturamento": 29229.88},
             {"Estado": "ES", "Faturamento": 27165.48},
             {"Estado": "Outros", "Faturamento": 19849.53}]

    faturamento_total = 0

    for dado in dados:
        faturamento = dado["Faturamento"]
        faturamento_total += faturamento

    for dado in dados:
        estado = dado["Estado"]
        faturamento = dado["Faturamento"]

        percentual = round((100 * faturamento) / faturamento_total, 2)
        print(f"Percentual de representação de {estado} no valor total: {percentual}%")

if __name__ == "__main__":
    main()
