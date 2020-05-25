# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/04/2020

'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível
segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual
dos animais seguintes foi escolhido, através das três palavras fornecidas.

ver tabela no URI

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

Exemplos de Entrada	    Exemplos de Saída
vertebrado              homem
mamifero
onivoro
'''

x = input()
y = input()
z = input()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    a = 'aguia'

if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    a = 'pomba'

if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    a = 'homem'

if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    a = 'vaca'

if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    a = 'pulga'

if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    a = 'lagarta'

if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    a = 'sanguessuga'

if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    a = 'minhoca'

print(a)
