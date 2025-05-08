''' Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
os valores PARES sorteados pela função anterior. '''

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma_par = 0
    for k in lista:
        if k % 2 == 0:
            soma_par += k
    print(f'A soma dos valores PARES da lista {lista} é {soma_par}.')


números = list()
sorteia(números)
somaPar(números)

