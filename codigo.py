# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:55:57 2021

@author: Bruce Martins
"""

# LIBS
import math
import random
import time
import pygame
import datetime

# EXERCICIO 035 - ANALISANDO TRIANGULO
r1 = float(input('Digite o tamanho da primera reta:'))
r2 = float(input('Digite o tamanho da segunda reta:'))
r3 = float(input('Digite o tamanho da terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triangulo com essas retas')
else:
    print('Não é possível formar um triangulo com essas retas')


# EXERCICIO 034 - AUMENTOS MULTIPLOS
s = float(input('Digite o salário: '))
if s > 1250:
    novo = s * 1.1
else:
    novo = s * 1.15
print('Um salário de R${:.2f} passa a ganhar R${:.2f}'.format(s,novo))


# EXERCICIO 033 - MAIOR E MENOR VALORES
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
menor = n1
if n3<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1   
if n3 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))


# EXERCICIO 032 - ANO BISSEXTO
ano = int(input('Digite um ano ou aperte zero para este ano: '))
if ano == 0:
    ano = datetime.date.today().year()
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')


# EXERCICIO 031 - CUSTO DA VIAGEM
dist = float(input('Qual a distância da sua viagem? '))
preco = dist * 0.50  if dist <= 200 else dist * 0.45
print('O preço da sua pasagem vai ser R${:.2f}'.format(preco))


# EXERCICIO 030 - PAR OU IMPAR
n = int(input('Digite um número: '))
if (n%2) == 0:
    print('Seu número é PAR')
else:
    print('Seu número é IMPAR')


# EXERCICIO 029 - RADAR ELETRONICO
v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('Teje multado! Você excedeu o limite de 80km/h')
    multa = (v - 80)*7
    print('Sua multa custará R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')


# EXERCICIO 028 - JOGO DA ADIVINHACAO
n = random.randint(0, 5)
print('Tente advinhar o número que eu escolhi de 0 a 5.')
tentativa = int(input('Em que número eu pensei? '))
if n == tentativa:
    print('Parabéns voce acertou!')
else:
    print('Eu pensei no número {} e não no {}'.format(n, tentativa))


# EXERCICIO 027 -  PRIMEIRO E ULTIMO NOME DE UMA PESSOA
nome = str(input('Qual seu nome completo?')).strip()
nomeSeparado = nome.split()
print('Prazer em te conhecer! {}'.format(nome))
print('Seu primeiro nome é {}'.format(nomeSeparado[0]))
print('Seu último nome é {}'.format(nomeSeparado[len(nomeSeparado)-1]))


# EXERCICIO 026 - PRIMEIRA E ULTIMA OCORRENCIA DE UMA STRING
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última  letra A aparece na posição {}'.format(frase.rfind('A')+1))


# EXERCICIO 025 - PROCURANDO UMA STRING EM OUTRA STRING
nome = str(input('Qual seu nome?')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))


# EXERCICIO 024 - VERIFICANDO AS PRIMEIRAS LETRAS
cid = str(input('Onde você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')


# EXERCICIO 023 - SEPARANDO DIGITOS DE UM NÚMERO
n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número {}'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


# EXERCICIO 022 - ANALISADOR DE TEXTOS
nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print('Seu nome possui {} letras'.format(len(nome)-nome.count(' ')))


# EXERCICIO 021 - TOCAR DE MP3
pygame.mixer.music.load()
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
