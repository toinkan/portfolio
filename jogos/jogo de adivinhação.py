#importação da biblioteca
import random

#função que serve apenas para criar traços
def traco():
  return print('------------'*4)

traco()
#regras
print('olá, este é um jogo de adivinhação.\no jogo vai funcionar da seguinte forma:\neu escolho um numero e você tenta acertar\noutra regra é que você só pode colocar numeros inteiros,\nou seja, NADA DE LETRAS OU NUMEROS QUEBRADOS')
traco()
#limite para o intervalo dos numeros
numa = int(input('qual o começo do intervalo:'))
numb = int(input('qual o final do intervalo:'))
traco()
#confirmação
print(f'o começo do seu intervalo é: {numa}\ne o final é: {numb}')

#escolhe o numero
alea = random.randint(numa , numb)

#começo do jogo
while True:
  num_res = int(input('qual é o numero?'))
  #caso acerte
  if alea == num_res:
    print('parabéns! você acertou!')
    break
  #caso erre
  else:
    print('errou! tente novamente')
    #se a sua resposta for maior que o numero escolhido
    if num_res > alea:
      print('está quase lá, um pouco mais pra baixo.')
    #se a sua resposta for menor que o numero escolhido
    elif num_res < alea:
      print("quase lá, um pouco mais para cima.")
    #em casos especiais
    else:
      print("como você errou?")