"""while/else
string = 'valor qualquer'

i = 0

while i < len(string):
    print(string[i])
    i += 1
"""
"""
frase = 'aaaooo'

i = 0

while i < len(frase):
   letra_atual = frase[i]
   quantasvezesaletraapareceu = frase.count(letra_atual)

   print(letra_atual, quantasvezesaletraapareceu)

   i += 1
"""
import os
palavra_secreta = 'isaias'
letras_acertadas = ''
numero_tentativas = 0
while True:
    
    
    letra_digitada = input('digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada =''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('palavra formada: 'f'{palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('voce acertou a palavra secreta era: ' f'{palavra_secreta}')
        print('tentativas: ' f'{numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0

       
    
        







