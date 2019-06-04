from datetime import datetime as datahora
import os, sys


try:
    os.mkdir('output')      # Tenta criar uma pasta para saída dos ficheiros chamada 'output'
except:                     #Se esta pasta existir, apanha o erro...
    pass                    #... e ignora o erro e segue


try:
    fic_1 = open('input/nomes.txt','r')                                                                                 # Verifica se existe o ficheiro 'nomes.txt'
except:
    print('Houve um erro a abrir o ficheiro nomes.txt. Verifique se a pasta "input" e o ficheiro "nomes.txt" existem')  # Se o ficheiro ou pasta não existirem gera erro...
    sys.exit()                                                                                                          # ...e termina o programa
else:                                                                                                                   #...senão segue lendo o ficheiro
    lista_1 = fic_1.read().splitlines()
    fic_1.close() 

try:
    lista_templates = os.listdir('templates')                                           #tenta criar lista com os nomes dos templates disponiveis dentro da pasta 'templates'
except:                                                                                 # se a pasta não existir apanha o erro
     print('Houve um erro a abrir o ficheiro nomes.txt')                                #Imprime msg erro...
     sys.exit()                                                                         #... e termina programa
else:                                                                                   #...senão prossegue para a criação da lista com o nome dos ficheiro na pasta template
    if len(lista_templates) == 0:                                                       #Se a pasta template estiver vazi
        print('A pasta dos Templates está vazia. Não é possível continuar o programa!') #imprime mensagen de erro...
        sys.exit()                                                                      #.. e termina programa


#Bloco para mostrar lista de templates disponíveis para escolha do utilizador
        
contador=1
for templates in lista_templates:
    print(contador,' - ',templates)
    contador+=1
templates_escolha = len(lista_templates) + 1
while templates_escolha > len(lista_templates):
    templates_escolha = int(input('Escolha um template de 1 a %d: ' % len(lista_templates)))

template_escolhido = lista_templates[templates_escolha-1]                                   #Template escolhido é guardado aqui em template_escolhido

    
#Bloco de leitura do template (já verificamos anteriormente que a pasta e ficheiro existem...)

fic_2 = open('templates/%s' % (template_escolhido),'r')
texto_padrao = fic_2.read()
fic_2.close()

#Leitura da data e respetivo guardar da mesma formatada na variável data

data_hora = datahora.now()
data = data_hora.strftime('%d/%m/%y')
print('Data hoje: ',data)

for n in lista_1:
    lista = n.split(',')
    numero = lista[0]
    nome = lista[1]
    

    #NOTA: para ser mais fácil escrever os templates, a data é substituida por <<data>> e o nome por <<nome>> em cada template.

    texto = texto_padrao.replace('<<data>>', data).replace('<<nome>>', nome) 
                                                                                
    output = open('output/' + numero + '.txt','w')
    output.write(texto)
    output.close()
    print ('Ficheiro /output/%s.txt processado!' % numero)




