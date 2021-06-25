from random import randint #Biblioteca para gerar os números dos dados aleatórios
import operator #Biblioteca para ordenar os dicionarios por ordem de Valor das Chaves
from time import sleep
from tqdm import tqdm #Biblioteca para gerar a barra de progresso
from rich import print #Biblioteca para decorar os textos

def linhas(): #Função para decorar com linhas criando efeito de separação
    print(f'='*30)

def clear(): #Função para limpar o console.
    try:
        import os # import dentro da função
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)
clear()
print(f'''
               
                 :!!!        !!!!!!!###########:.###############.:#########################:    ....##!!:               
                 .!!!!:      !!!!!!!!!!!#####!###!!!#######@###############################.      :##!!!:               
                 .!!!!!!!!!!!!!!!!!!!!!!#!#     :!!########@#########!    . !#########################!!.               
                  :!!!!!!!!!!!!!!!!!!!!!##!       .########@#######........ .#########################!!.               
                  .!!!!!!!!!!!!!!!!!!!!!#!!.        !############# .   .... ##########################!!.               
                   !!!!!!!!!!!!:      !!!!!##       :!############        :###########################!!.               
                   !!!!!!##!!!!!        !!!!!!!!#!!#!#############################################!###!!                
                    !!!    .!!!!!        !!!!!!!!!!##########################################!!... .##!!                
                    .!!       !!!!!:    .!!!!!!!!!!#########################################:.......##!.                
                     .!!       !!!!#!!!!!!!!!!!!!!!######################################## ..   . ##!:                 
                       :!!:    !!!!!!!!!!!!!!!!!!##!!######################################     .!#!!                   
                          .!!!!!!!!!!!!####!!. .:#!!###################!.   .####################!.                     
                              .!!!!!!!!####!       .##!##############.........###############!.                         
                                   :!!#!!#!!#        .!!###########...  .  . ############.                              
                                       .!!!!!!!       !!###########       .########!                                    
                                            :!!!##!#!#########################:                                         
                                                 .!!#!##################!.                                              
                                                       .:!!!!#!!!#: 
''')
print()
print(f'{"VAMOS JOGAR DADOS":^30}')
linhas()

rodadas = int(input('Quantas rodadas você quer jogar? '))
sleep(1)
linhas()
dadosResult = list() # criação das listas para receber os dicionários

vitPlayer1 = vitPlayer2 = vitPlayer3 = vitPlayer4 = 0 # Contadores para os resultados das rodadas
print('ROLANDO OS DADOS...')
print()
for i in tqdm(range(1000)):
    sleep(0.001)
print()
for r in range(rodadas):
    rodada = dict() # Criação de dicionário temporário que receberá as informações de cada rodada
    
    rodada['player1'] = randint(1, 6) # Randint para gerar números aleatórios dos dados
    rodada['player2'] = randint(1, 6)
    rodada['player3'] = randint(1, 6)
    rodada['player4'] = randint(1, 6)
    sleep(1)
    print(rodada)
    sleep(1)
    if (rodada['player3'] < rodada['player1'] > rodada['player2']) and rodada['player1'] > rodada['player4'] :
        vitPlayer1+=1
    elif (rodada['player3'] < rodada['player2'] > rodada['player1']) and rodada['player2'] > rodada['player4'] :
        vitPlayer2+=1
    elif (rodada['player2'] < rodada['player3'] > rodada['player1']) and rodada['player3'] > rodada['player4'] :
        vitPlayer3+=1
    elif (rodada['player3'] < rodada['player4'] > rodada['player2']) and rodada['player4'] > rodada['player1'] :
        vitPlayer4+=1
    empates = rodadas - (vitPlayer1+vitPlayer2+vitPlayer3+vitPlayer4)
    sortedResult = sorted(rodada.items(), key=operator.itemgetter(1), reverse=True) # lista ordenada utilizando a lib Operator
    # itemgettetr (1) para ordenar pelo VALOR , REVERSE = True para ordem decrescente (o maior valor ganha)
    dadosResult.append(sortedResult) # Cada dicionário temporário criado é adicionado ao dadosResult que contem todos as rodadas
sleep(1)
linhas()
if (vitPlayer2 < vitPlayer1 > vitPlayer3) and vitPlayer1 > vitPlayer4:
    print(f'O GRANDE CAMPEÃO É O JOGADOR 1 COM {vitPlayer1} VITÓRIAS.')
elif (vitPlayer3 < vitPlayer2 > vitPlayer1) and vitPlayer2 > vitPlayer4:
    print(f'O GRANDE CAMPEÃO É O JOGADOR 2 COM {vitPlayer2} VITÓRIAS.')
elif (vitPlayer2 < vitPlayer3 > vitPlayer1) and vitPlayer3 > vitPlayer4:
    print(f'O GRANDE CAMPEÃO É O JOGADOR 3 COM {vitPlayer3} VITÓRIAS.')
elif (vitPlayer2 < vitPlayer4 > vitPlayer1) and vitPlayer4 > vitPlayer1:
    print(f'O GRANDE CAMPEÃO É O JOGADOR 4 COM {vitPlayer4} VITÓRIAS.')
else:
    print(f'NÃO HOUVE UM GRANDE CAMPEÃO... TIVEMOS EMPATE')

linhas()
sleep(1)
print(f'{"[bold yellow]ESTATÍSTICAS DO JOGO[/bold yellow]":^30}')
linhas()
#print(dadosResult)
print(f'''
JOGADOR 1 = {vitPlayer1} VITÓRIAS
JOGADOR 2 = {vitPlayer2} VITÓRIAS
JOGADOR 3 = {vitPlayer3} VITÓRIAS
JOGADOR 4 = {vitPlayer4} VITÓRIAS
EMPATES = {empates}
''')