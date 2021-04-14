# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:55:57 2021

@author: Bruce Martins
"""

# LIBS
import math
import random
import pygame

# EXERCICIO 029 - 
# EXERCICIO 028 - 
# EXERCICIO 027 - 
# EXERCICIO 026 - 
# EXERCICIO 025 - 
# EXERCICIO 024 - 
# EXERCICIO 023 - 
# EXERCICIO 022 - 



# EXERCICIO 021 - TOCAR DE MP3
pygame.mixer.music.load('C:\Users\Home\Desktop\Projetos\Camila Campanha\go_no_go\beep_sound.mp3')
pygame.mixer.music.play()
pygame.event.wait()


# EXERCICIO 020 - SORTEAR ORDEM
primeiro = input('Digite o primeiro aluno: ')
segundo = input('Digite o segundo aluno: ')
terceiro = input('Digite o terceiro aluno: ')
quarto = input('Digite o quarto aluno: ')
lista = [primeiro,segundo,terceiro,quarto]
random.shuffle(lista)
print('A ordem de apresentação é:')
print(lista)


# EXERCICIO 019 - SORTEIO
primeiro = input('Digite o primeiro aluno: ')
segundo = input('Digite o segundo aluno: ')
terceiro = input('Digite o terceiro aluno: ')
quarto = input('Digite o quarto aluno: ')
lista = [primeiro,segundo,terceiro,quarto]
escolhido = random.choice(lista)
print('O aluno escolhido é {}'.format(escolhido))


# EXERCICIO 018 - SENO, COSSENO, TANGENTE
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('Para o angulo {} o seno é {:.2f}, o coseno é {:.2f}, e a tangente é {:.2f}'.format(angulo,seno,coseno,tan))


# EXERCÍCIO 017 - CATETOS E HIPOTENUSA
op = float(input("Digite o valor do cateto oposto: "))
adj = float(input("Digite o valor do cateto adjacente: "))
hip = math.hypot(op,adj)
print('A hipotenusa é {:.2f}'.format(hip))


# EXERCICIO 016 - QUEBRANDO NÚMEROS
n = float(input('Digite um número real: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n,math.trunc(n)))


# EXERCICIO 015 - ALUGUEL DE CARROS
dias = int(input('Quantos dias vc ficou com o carro? '))
km = int(input('Quantos Kms rodados? '))
pago = (dias*60)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(pago))


# EXERCÍCIO 014 - CONVERSOR DE TEMPERATURAS
c = float(input('Informe a temperatura em Cº: '))
f = ((9*c)/5)+32
print('A temperatura de {}ºC é {}ºF.'.format(c,f))


# EXERCICIO 013 - REAJUSTE DE SALÁRIO
salario = float(input('Qual o valor do salário? '))
novo = salario*1.15
print('O Salário novo é R${:.2f}'.format(novo))


# EXERCICIO 012 - CALCULANDO DESCONTOS
preco = float(input('Qual o valor do produto? '))
novo = preco * 0.95
print('O produto que custa {:.2f} reais com 5% de desconto vai custar {:.2f} reais'.format(preco, novo))


# EXERCICIO 011 - PINTANDO PAREDE
largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))
area = largura*altura
print('Sua parede tem a dimensao de {}x{} e a sua área é de {}m².'.format(largura,altura,area))
print('Para pintar essa parede você vai precisar de {}L de tinta'.format(area/2))


# EXERCICIO 010 - CONVERSOR DE MOEDAS
carteira = float(input('Quanto você tem na sua carteira? '))
dolar = carteira/5.73
print('Com {:.2f} reais você compraria {:.2f} dólares'.format(carteira, dolar))
# PS: o Guanabara estava certo sobre o dólar


# EXERCICIO 009 - TABUADA
num = int(input('Digite um número que você queira saber a tabuada: '))
print('{} x {:2} = {}'.format(num,1,num*1))
print('{} x {:2} = {}'.format(num,2,num*2))
print('{} x {:2} = {}'.format(num,3,num*3))
print('{} x {:2} = {}'.format(num,4,num*4))
print('{} x {:2} = {}'.format(num,5,num*5))
print('{} x {:2} = {}'.format(num,6,num*6))
print('{} x {:2} = {}'.format(num,7,num*7))
print('{} x {:2} = {}'.format(num,8,num*8))
print('{} x {:2} = {}'.format(num,9,num*9))
print('{} x {:2} = {}'.format(num,10,num*10))


# EXERCICIO 008 - CONVERSOR DE MEDIDAS
medida = float(input('Digite um valor: '))
cm = medida*100
mm = medida*1000
print('A medida de {}m corresponde a {:.0f}cm e {:0f}mm'.format(medida, cm, mm))


# EXERCICIO 007 - MÉDIA ARITMÉTICA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A média de {} e {} é {}'.format(n1, n2, ((n1+n2)/2)))


# EXERCICIO 006 - DOBRO, TRIPLO, RAIZ QUADRADA
n = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(n,(n*2)))
print('O triplo de {} vale {}'.format(n,(n*3)))
print('A raiz quadrada de {} é {:.2f}'.format(n,(n*0.5)))


# EXERCICIO 005 - ANTECESSOR E SUCESSOR
n = int(input('Digite um número: '))
antecessor = n - 1
sucessor = n + 1
print('Você digitou o número {}. O antecessor é {} e o sucesso é {}.'.format(n, antecessor, sucessor))


# EXERCICIO 004 - TIPO DE VARIÁVEL
valor = input('Digite algo: ')
print('O que você digitou é {}'.format(type(valor)))


# EXERCÍCIO 003 - SOMANDO DOIS NÚMEROS
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
s = n1 + n2
print('A soma de {} e {} é {}'.format(n1, n2, s))


# EXERCÍCIO 002 - RESPONDENDO AO USUARIO
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))


# EXERCÍCIO 001 - DEIXANDO TUDO PRONTO
print('Hello World!')
