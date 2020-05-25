# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/04/2020

'''
Leia um número inteiro que representa um código de DDD para discagem interurbana.
Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:
Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD não cadastrado

ver imagem URI

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada.
Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.

Exemplo de Entrada	    Exemplo de Saída
11                      Sao Paulo
'''

entrada = int(input())

if entrada == 61:
 print("Brasilia")
elif entrada == 71:
 print("Salvador")
elif entrada == 11:
 print("Sao Paulo")
elif entrada == 21:
 print("Rio de Janeiro")
elif entrada == 32:
 print("Juiz de Fora")
elif entrada == 19:
 print("Campinas")
elif entrada == 27:
 print("Vitoria")
elif entrada == 31:
 print("Belo Horizonte")
else:
 print("DDD nao cadastrado")
