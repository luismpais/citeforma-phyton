import modulo1

#Função principal a ser chamada
def main():
    dic=modulo1.gerador() #chama função do modulo com return de um dicionário

    #Imprime chave a partir do dicionário
    print('\nNúmeros gerados: \n',
          'Chave: ', dic['numeros'],'\n',
          'Estrelas: ', dic['estrelas'])

    #Opção para anexar ou apagar ficheiro existente 
    print('\nSelecione uma opção: \n',
          '------------------------\n',
          '1: Anexar resultados ao ficheiros\n',
          '2: Apagar ficheiro e escrever do inicio\n',
          '------------------------')
    #Bloco de control para input
    escolha=3                                                  #Inicialização de escolha para o ciclo correr pelo menos 1 vez
    while escolha <1 or escolha>2:
        escolha=input('Selecione a sua opção: ')
        if escolha.isdigit():                                  #Se string input é composto por digitos...
            escolha=int(escolha)                                #converte em inteiro
            if escolha==1:modulo1.escrever_lista_append(dic)  #Anexa lista 
            else: modulo1.escrever_lista_write(dic)            #Apaga ficheiro e escreve do inicio
        else: escolha=3


    #Opção para terminar programa ou gerar nova chave
    print('\nGerar nova chave?\n',
          '------------------------\n',
          '1: Sim\n',
          '2: Não terminar o progama\n',
          '------------------------')
    #Bloco de control para input
    escolha=3
    while escolha <1 or escolha>2:
        escolha=input('Selecione a sua opção: ')
        if escolha.isdigit():
            escolha=int(escolha)
            if escolha==1:main()               #chama main() recursivamente
            else:break                          #Sai do while e termina programa
        else: escolha=3

main()

