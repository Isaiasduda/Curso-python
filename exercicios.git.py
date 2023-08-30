# Jogo palavra secreta
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

#calculadora com while 

while  True:
    numero1 = input('digite um numero: ')
    numero2 = input('digite outro numero: ')
    operacao = input('digite a operacao: ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
        
    except:
        numeros_validos = None

    if numeros_validos is  None:
        print('um ou ambos numeros sao invalidos. ')
        continue    

    operadores_permitidos ='+-/*'

    if operacao not in operadores_permitidos:
        print('operador invalido')
        continue

    if len(operacao) > 1:
        print('operador invalido')
        continue   

    print('realizando sua conta')
    
    if operacao == '+':
        print(num_1_float + num_2_float)
    elif operacao == '-':
        print(num_1_float - num_2_float)
    elif operacao == '*':
        print(num_1_float * num_2_float)
    elif operacao == '/':
        print(num_1_float / num_2_float)
    else:
        print('operacao invalida')
        

    sair = input('quer sair? [s]im:').lower().startswith('s')

    
    if sair is True:
        break

#tamanho da palavra

nome = input('digite seu nome :')
if len(nome) <= 4:
    print('seu nome tem 4 ou menos caracteres')
elif len(nome)==5 <= 6:
     print('seu nome e normal')
else:
    len(nome) > 6 
    print('seu nome tem mais de 6 caracteres')

# tabuada 

numero = input('digite um numero: ')
numero_int = int(numero)
print('tabuada : 'f'{numero_int  }  ' )
numero_int <- 0
faca = numero_int <= 10
while faca:
    print(f'{numero_int} x 1 = {numero_int * 1}')
    print(f'{numero_int} x 2 = {numero_int * 2}')
    print(f'{numero_int} x 3 = {numero_int * 3}')
    print(f'{numero_int} x 4 = {numero_int * 4}')
    print(f'{numero_int} x 5 = {numero_int * 5}')
    print(f'{numero_int} x 6 = {numero_int * 6}')
    print(f'{numero_int} x 7 = {numero_int * 7}')
    print(f'{numero_int} x 8 = {numero_int * 8}')
    print(f'{numero_int} x 9 = {numero_int * 9}')
    print(f'{numero_int} x 10 = {numero_int * 10}')
    break
