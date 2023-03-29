import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# a) Leitura do arquivo
dados = pd.read_csv('C:/Users/muril/Desktop/Dados_Clima/ArquivoDadosProjeto.csv', sep=';')
print('Dados carregados:')
print(dados)

# b) Visualização de dados de precipitação
while True:
    try:
        ano_mes = input('Digite o ano e mês desejados (yyyy-mm): ')
        ano, mes = map(int, ano_mes.split('-'))
        datetime(ano, mes, 1) # Verifica se a data é válida
        break
    except ValueError:
        print('Data inválida. Tente novamente.')

print(f'Precipitação em {mes}/{ano}:')

for _, dado in dados.iterrows():
    data = datetime.strptime(dado['data'], '%d/%m/%Y')
    if data.year == ano and data.month == mes:
        precipitacao = dado['precip']
        print(f'{data.day}/{mes}/{ano}: {precipitacao}')

# c) Visualização de dados de temperatura
while True:
    try:
        ano_str = input('Digite o ano desejado: ')
        ano = int(ano_str)
        datetime(ano, 1, 1) # Verifica se o ano é válido
        break
    except ValueError:
        print('Ano inválido. Tente novamente.')

primeiros_7_dias = dados[dados['data'].str.match(f'0[1-7]/\d{{2}}/{ano_str}')]
temperaturas_max = primeiros_7_dias['maxima'].tolist()
print(f'Temperatura máxima em cada um dos primeiros 7 dias de cada mês de {ano}: {temperaturas_max}')

# d) Análises estatísticas
def mes_chuvoso(dados):
    """
    Retorna o mês mais chuvoso de todo o período, com o nome do mês e o ano correspondente.
    """
    chuvoso = {'mes': None, 'ano': None, 'acumulado': 0}
    meses = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
             '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
             '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
    for _, dado in dados.iterrows():
        data = datetime.strptime(dado['data'], '%d/%m/%Y')
        mes_ano = f"{data.month:02d}-{data.year:04d}"
        if mes_ano in chuvoso:
            chuvoso[mes_ano] += dado['precip']
        else:
            chuvoso[mes_ano] = dado['precip']
        if chuvoso[mes_ano] > chuvoso['acumulado']:
            chuvoso['acumulado'] = chuvoso[mes_ano]
            chuvoso['mes'] = meses[f"{data.month:02d}"]
            chuvoso['ano'] = data.year
    return chuvoso

print(mes_chuvoso(dados))
