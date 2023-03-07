# Inicialização das variáveis
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

# Cálculo da média por estado
sp_per = (sp / total) * 100
rj_per = (rj / total) * 100
mg_per = (mg / total) * 100
es_per = (es / total) * 100
outros_per = (outros / total) * 100

print('Percentual de participação de cada estado: ')
print(f'SP: {sp_per:.2f}')
print(f'RJ: {rj_per:.2f}')
print(f'MG: {mg_per:.2f}')
print(f'ES: {es_per:.2f}')
print(f'Outros estados: {outros_per:.2f}')
