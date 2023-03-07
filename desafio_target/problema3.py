import json


def analise_dados(tabela_json):

    """
    Recebe uma tabela no formato json como parâmetro e retorna o menor valor faturado num dia, maior valor faturado num
    dia, e média de faturamento, desconsiderando os dias sem faturamento.

    Entradas:
    tabela_json -- Tabela a ser verificada

    Saídas:
    menor -- Menor faturamento dentre os dias válidos
    maior -- Maior faturamento dentre os dias válidos
    dias_acima_media -- Quantidade de dias com faturamento acima da média diária
    """

    # Carrega os dados da tabela
    dados = json.load(tabela_json)

    # Inicialização das variáveis a serem utilizadas
    tot_dias = 0
    tot_valor = 0
    menor = 0
    maior = 0
    dias_acima_media = 0

    for dia in dados:

        # Se o valor de faturamento de um dia for 0, pular a iteração
        if dia['valor'] == 0:
            continue

        # Caso contrário, adiciona 1 ao total de dias de faturamento e o valor do dia ao total do faturamento
        tot_dias += 1
        tot_valor += dia['valor']

        # Checa se o valor do dia é o menor até então
        if dia['dia'] == 1 or dia['valor'] < menor:
            menor = dia['valor']

        # Checa se o valor do dia é o maior até então
        if dia['valor'] > maior:
            maior = dia['valor']

    # Calcula a média de faturamento diário
    media = tot_valor / tot_dias

    # Checa quantos dias estiveram acima da média
    for dia in dados:

        if dia['valor'] > media:
            dias_acima_media += 1

    return menor, maior, dias_acima_media


f = open('dados.json')
menor, maior, dias_acima_media = analise_dados(f)
print(f'O menor valor de faturamento ocorrido em um dia do mês: R${menor:.2f}')
print(f'O maior valor de faturamento ocorrido em um dia do mês: R${maior:.2f}')
print(f'Quantidade de dias com o faturamento acima da média diária: {dias_acima_media}')
