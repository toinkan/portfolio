#definição de variavel
tentat = 6
palsego = 'cachorro'
quanletr = 8
tema = 'animal'
letcer = []
leterr = []

#regras/dicas
print(f'dicas: \na palavra tem {quanletr} letras\nvocê tem {tentat} tentativas\no tema é {tema}\n\nregras:\nvocê só pode colocar uma letra por vez\ncoloque apenas letras nada de numeros\n\nboa sorte!!')

#começo do jogo
while True:
  palavrainc = ''
  for esclet in letcer:
    if esclet in letcer:
      palavrainc += esclet
    else:
      palavrainc += '_'
  print(palavrainc)

#pergunta qual a letra
  esclet = input('me diga uma letra:')

#vê se a letra que foi chutada ja não foi escolhida antes
  if esclet in letcer or esclet in leterr:
    print('tu chutou essa letra seu abestado')
    continue

#vê se a letra está certa
  if esclet in palsego:
    letcer.append(esclet)
    print("acertou!")

#se a letra está errada
  else:
    leterr.append(esclet)
    print("errou!!")
    tentat -= 1

#isso vê se a palavra está completa, caso acerte
  if all(esclet in letcer for esclet in palsego):
    print(f'meus parabens, você ganhou!\na palavra certa é {palsego}')
    break

#isso vê se a suas tentativas já acabaram ou não.
  if tentat < 1:
    print(f'you lose, a palavra era {palsego}')
    break

#te fala quantas tentativas você tem
  print(f'irmão, tu tem {tentat} tentativas, vá com deus.')