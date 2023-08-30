"""
contador = 0
while contador <= 100:
    contador += 1

    if  contador == 40:
        print("sei la ")
        continue
        
    print(contador)

    if contador == 41:
        break




print('fim')
"""

"""
qtd_linha = 5
qatd_colunas = 5

linha =1
while linha <= qtd_linha:
    
    coluna = 1
    while coluna <= qatd_colunas:
    
        print(linha, coluna)
        coluna += 1
    linha += 1
    
print('fim')

"""
"""
nome = 'isaias duda'

indice = 0
novo_nome=''
while indice < len(nome):
    letra = nome[indice] # + '*' 
    novo_nome += f' * {letra}'
    indice += 1

print(novo_nome)
"""

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

    


