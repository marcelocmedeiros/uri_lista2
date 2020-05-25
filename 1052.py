'''
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor,
deve ser apresentado como resposta o mês do ano por extenso,
em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, c
om a primeira letra em maiúscula.
'''

v = int(input('v= '))

if v == 1:
    v = 'January'
    print(v)
elif v == 2:
    v = 'February'
    print(v)
elif v == 3:
    v = 'March'
    print(v)
elif v == 4:
    v = 'April'
    print(v)
elif v == 5:
    v = 'May'
    print(v)
elif v == 6:
    v = 'June'
    print(v)
elif v == 7:
    v = 'July'
    print(v)
elif v == 8:
    v = 'August'
    print(v)
elif v == 9:
    v = 'September'
    print(v)
elif v == 10:
    v = 'October'
    print(v)
elif v == 11:
    v = 'November'
    print(v)
elif v == 12:
    v = 'December'
    print(v)
