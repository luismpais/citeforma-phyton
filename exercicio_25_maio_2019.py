'''
Resolução de exercicio para casa
na sessão 4 (25 Maio 2019)
'''

dic_lucro={2017:{2:967.95, 5:1678.48, 7:647.5, 11:792.83},
           2018:{3:838.6, 7:168.4, 0:278.23}} #Dicionario dado para exercicio


totais_dic = {} #Inicialização do dicionário para totais anuais
maximos_dic={} #Inicialização do dicionário para máximos de cada ano

for ano_key in dic_lucro: #Para cada ano ...
    meses_dic=dic_lucro[ano_key] #variável 'meses_dic' é um dicionário referente aos meses do ano em questão 'dic_lucro[ano_key]'
    total_anual=sum(list(meses_dic.values())) #Conversão dos valores do dicionário 'meses_dic' em lista e respetiva soma desse ano, guardada em 'total_anual'
    maximo_anual=max(list(meses_dic.values())) #Conversão dos valores do dicionário 'meses_dic' em lista e respetivo máximo desse ano, guardada em 'maximo_anual'

    for mes_key in meses_dic: #Para cada mes...
        if meses_dic[mes_key] == maximo_anual: maximo_mes_key=mes_key #Se o valor deste mês é igual ao valor  guardado em 'maximo_anual', guarda a key deste mês em 'maximo_mes_key'

    totais_dic.update({ano_key: total_anual}) #Atualiza dicionário'totais_dic' com o total para este ano
    maximos_dic.update({ano_key: (maximo_mes_key,maximo_anual)}) #Atualiza dicionário 'maximos_dic' com o máximo {ano: (mes,valor)} para este ano

print('Dicionário de Totais por ano:\n',totais_dic)
print('Dicionário do Melhor Mês de cada Ano:\n',maximos_dic)
