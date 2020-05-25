# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 16/04/2020

'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e
a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
        ver imagem no URI
Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao
código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo
valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada	    Exemplo de Saída
3 2                     Total: R$ 10.00

4 3                     Total: R$ 6.00

2 3                     Total: R$ 13.50
'''

c = input().split(" ")
a, b = c
a = int(a)
b = int(b)
if a == 1:
  tot = b * 4.00;
elif a == 2:
  tot = b * 4.50;
elif a == 3:
  tot = b * 5.00;
elif a == 4:
  tot = b * 2.00;
elif a == 5:
  tot = b * 1.50;
print("Total: R$ {:.2f}".format(tot))
