from random import randint
from datetime import datetime

def gerador():
    lista_numeros=[]
    for n in range(0,7):
        lista_numeros.append(str(randint(1,45)))
    return {'numeros':lista_numeros[0:5], 'estrelas':lista_numeros[5:]}

def escrever_lista_append(dic):
    data_hora=datetime.now()
    data_formatada=data_hora.strftime('%d/%m/%Y %H:%M:%S')
    texto=data_formatada + ','.join(dic['numeros']) + ',' +','.join(dic['estrelas']) + '\n'
    fic=open('chaves_euromilhoes.txt','a')
    fic.write(texto)
    fic.close()
    
def escrever_lista_write(dic):
    data_hora=datetime.now()
    data_formatada=data_hora.strftime('%d/%m/%Y %H:%M:%S')
    texto=data_formatada + ','.join(dic['numeros']) + ',' +','.join(dic['estrelas']) + '\n'
    fic=open('chaves_euromilhoes.txt','w')
    fic.write(texto)
    fic.close()
