"""
nome = 'isaias'
sobrenome = 'duda'
idade= 27
ano = 2023 - idade
maior_de_idade = idade>= 18
altura_metros = 1.77


adicao = 10 + 15
print('adicao:',adicao)

subtracao = 10 - 15
print('subtracao:',subtracao)

exponenciacao = 2**10

print('exponenciacao:',exponenciacao)

peso = 95
altura = 1.80 **2
imc = peso / altura 
print ('imc:',imc)

a = 'A'
b = 'B'
c = '1.1'
string = 'a={} b={} c={}'
formato = string.format(a, b, c)

print('formato:',formato)

nome = input('qual o seu nome')
print('nome:',nome)

"""
"""

numero = input(' digite um numero inteiro ')

if numero.isdigit():
     numero_int = int(numero)
     par_impar = numero_int % 2 == 0
     par_impar_texto = 'impar'
     
     if par_impar is True:
          par_impar_texto  = 'par'

     print(f'o numero {numero_int} e {par_impar_texto}')

else:
     print('esse numero e invalido')
"""
"""
numero = input(' digite um numero inteiro ')

try:
     numero_int = int(numero)
     par_impar = numero_int % 2 == 0
     par_impar_texto = 'impar'
     
     if par_impar is True:
          par_impar_texto  = 'par'

     print(f'o numero {numero_int} e {par_impar_texto}')

except:
     print('esse numero e invalido')
"""




"""
hora=input('que horas sao :')
hora_float= float(hora)

if (hora_float > 00.00) and hora_float < 05.00:
    print('boa noite')
elif (hora_float > 06.00) and hora_float <= 12:
    print('bom dia')
else:
    print('boa tarde')


"""
"""
nome = input('digite seu nome :')
if len(nome) <= 4:
    print('seu nome tem 4 ou menos caracteres')
elif len(nome)==5 <= 6:
     print('seu nome e normal')
else:
    len(nome) > 6 
    print('seu nome tem mais de 6 caracteres')
"""
