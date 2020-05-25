# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 16/04/2020

'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


Salário	            Percentual de Reajuste
0 - 400.00                  15%
400.01 - 800.00             12%
800.01 - 1200.00            10%
1200.01 - 2000.00           7%
Acima de 2000.00            4%

Leia o salário do funcionário e calcule e mostre o novo salário,
bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e
o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada	                Exemplo de Saída
400.00                              Novo salario: 460.00
                                    Reajuste ganho: 60.00
                                    Em percentual: 15 %

800.01                              Novo salario: 880.01
                                    Reajuste ganho: 80.00
                                    Em percentual: 10 %

2000.00                             Novo salario: 2140.00
                                    Reajuste ganho: 140.00
                                    Em percentual: 7 %
'''
a= float(input())
if (0<a<=400):
    rea=(((a*15)/100)+a)
    perc= 15
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(400<a<=800):
    rea=(((a*12)/100)+a)
    perc= 12
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(800<a<=1200):
    rea=(((a*10)/100)+a)
    perc= 10
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(1200<a<=2000):
    rea=(((a*7)/100)+a)
    perc= 7
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
else:
    rea=(((a*4)/100)+a)
    perc= 4
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
