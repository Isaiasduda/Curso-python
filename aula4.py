""""
entrada= input(" voce que 'entrar' ou 'sair'")
if entrada == 'sair':
    print('Sair')
elif entrada == 'entrar':
    print('Entrar')
else: 
    print('voce digitou outra coisa ')

"""
"""


primeiro_valor = input('digite um valor ')

segundo_valor = input('digite outro valor ')


if segundo_valor > primeiro_valor:
    print('o segundo valor é maior que o primeiro valor')
elif segundo_valor < primeiro_valor:
    print('o segundo valor é menor que o primeiro valor')
else :
    print('o segundo valor é igual ao primeiro valor')
"""
"""
if primeiro_valor > segundo_valor:
    print (
        f'{primeiro_valor=} E maior do que '
        f'{segundo_valor =}'
) 
else:
    print (
        f'{segundo_valor=} E maior do que '
        f'{primeiro_valor =}'
)
"""
"""
entrada = input('[E]ntrar  [S]air ' )
saida = input()
senha = input('senha:')
senha_permitida = '123'
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrar')

elif saida == 's' or 'S':
    print('Sair')
else: 
    print ('error')
"""
"""
nome = 'isaias'
print(nome[3])

print('a' in nome)
"""
"""
nome = input('digite seu nome: ')
encontrar = input('digite o que quer encontrar : ')

if encontrar in nome:
  print(  f'{encontrar} esta em {nome}')
else:
  print(f'{encontrar} nao esta em {nome}')
"""
"""
nome= 'isaias'
preco = 12.33
variavel = '%s o preco e %.2f' % (nome, preco)
print(variavel)
"""
variavel = 'ABC'
print(f'{variavel: >10}')