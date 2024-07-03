import numpy as np

a = np.array([1,2,3,4,5])
#array bidimensional
biD = np.array([
    [1,2,3,4,5],
    [5,4,3,2,1],
    [5,1,4,2,3]
])
print(biD.ndim)#retorna o número de dimensões do array
print(biD.shape)#retorna o formato do array(Número de linhas e colunas)
print(len(a))#autodescritivo kk

c = np.arange(0, 100, 2)#cria array com tamanho que deseja de forma automática(0 a 99 de 1 e de 2 em 2 o valor de cada casa) 
print(c)

d = np.linspace(1, 10, 20, endpoint=False)#cria array que começa em 1, termina em 10 e o terceiro parâmetro é o número de elementos entre 1 e 10.O false remove o elemento final, remove o 10
print(d)

e = np.ones((3,3))#cria matriz de números 1 com dimensões de 3x3
print(e)

f = np.random.rand(10)#cria array com 10 posições preenchidos de forma aleatória com números entre 0 e 1
print(f)

g = np.eye(3)#Cria matriz 3x3 com números 1 na diagonal
print(g)

h = np.diag(np.array([1,2,3,4]))#cria matriz 3x3 com 1 a 4 na diagonal

