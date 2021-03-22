'''
Definindo as estruturas do jogo: escolha aelatória,
banco de palavras, e efeitos visuais
'''

import random # Módulo aleatório do Python
import sys # Para o usuário ter a opção de digitar 'SAIR' e desligar o programa
from palavras import pt_words # Lista de arquivos contento milhares de palavras em português
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # Lista de caracteres válidos para o usuário dgitiar
from graficos import forca_vsfx

'''
Criando as mecânicas para a função do jogo
'''
def obter_plv(): # Obter palavra aleatória
  plv_rd = random.choice(pt_words)
  return plv_rd.upper()

def user_interf(acertos, erros, plv_sorteada): # Intarface do usuário a ser mostrada
  print(forca_vsfx[len(erros)])
  print()

  print('Letras erradas:', end ='')
  for letra in erros:
    print(letra, end='')
  print()

  lacunas = '_' * len(plv_sorteada) # TODO: colocar o sublinhado nas letras

  for i in range(len(plv_sorteada)):
    if plv_sorteada[i] in acertos:
      lacunas = (lacunas[:i] + plv_sorteada[i] + lacunas[i + 1:])
  
  for letra in lacunas:
    print(letra, end='')
  print()

def obter_tent(tent_feita): # Mecânicas das tentativas do usário com validação implementada
# TODO: implementar a mecânica de arriscar a palavra toda e ganhar ou perder
  while True:
    tentativa = input('Escolha uma letra ou digite\n"SAIR" para encerrar o jogo: ').upper()
    if tentativa == 'SAIR':
      sys.exit('Até a próxima!')
    elif len(tentativa) > 1:
      print('Apenas uma letra por tentativa, por favor.')
    elif len(tentativa) < 1:
      print('Tenativa vazia. Digite uma letra.')
    elif tentativa in tent_feita:
      print('Você já escolheu esta letra. Escolha uma outra.')
    elif tentativa not in alfabeto:
      print('Apenas LETRAS!')
    else:
      return tentativa

def novo_jogo(): # Reiniciar o jogo
  print('Deseja jogar novamente? SIM/NAO')
  return input().upper().startswith('S')

'''
Criando a execução do jogo
'''

print('----- X___X O JOGO DA FORCA X___X -----') # gamestart
acertos = ''
erros = ''
plv_sorteada = obter_plv()
fim_de_jogo = False

while True: # Loop principal de execução do jogo
  user_interf(acertos, erros, plv_sorteada)

  tentativa = obter_tent(acertos + erros)

  if tentativa in plv_sorteada:
    acertos = acertos + tentativa

    acertou_tudo = True # Condição de vitória
    for i in range(len(plv_sorteada)):
      if plv_sorteada[i] not in acertos:
        acertou_tudo = False
        break
    if acertou_tudo:
      print('Acertou! A palavra escolhida é ', plv_sorteada)
      fim_de_jogo = True
  else:
    erros = erros + tentativa

    if len(erros) == len(forca_vsfx) - 1: # Condição de derrota
      user_interf(acertos, erros, plv_sorteada)
      print('Fim de jogo!\n Depois de ' + str(len(erros)) + ' erros e ' + str(len(acertos)) + ' acertos, a palavra era ' + str(plv_sorteada))
      fim_de_jogo = True
  if fim_de_jogo:
    if novo_jogo(): # Replay
      erros = ''
      acertos =  ''
      fim_de_jogo = False
      plv_sorteada = obter_plv()
    else:
      break