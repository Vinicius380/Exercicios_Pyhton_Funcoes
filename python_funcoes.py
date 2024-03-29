# -*- coding: utf-8 -*-
"""Python_Funcoes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NwSnBxiUotq8tB18x8_xTWwhwApVNtdZ

FUNCAO DEF
"""

def saudacao(nome):
  print("Ola", nome)

nome = input("Entre com seu nome: ")

saudacao(nome)

#E a criacao de uma funcao funciona com um "apelido" para uma sequencia de codigos que pode ser chamado a qualquer momento no programa

def alterna(n):
  n = float(input("Insira o numero: "))
  mult = -1
  fat = 1
  i = 0
  while i < n:
    num = fat * (n-i)
    fat *= mult
    i += 1

def perimetro(altura, largura):                   #Nomeacao de todas as variaveis que serao calculadas
  perimetro = (altura + largura)*2                #Calculo
  return perimetro                                #Retornar o calculo

altura1 = 3                                       #Atribuicao de valor
largura1 = 2                                      #Atribuicao de valor

print("O perimetro do retangulo e:",perimetro(altura1, largura1))          #A funcao perimetro faz o calculo direto a partir dos valores adicionados a ela

def saudacao(nome, mensagem):
  print = ("Ola", nome, mensagem)

nome1 = input("Nome: ")
mensagem1 = input("Mensagem")

saudacao(nome1, mensagem1)

def soma_pn(valores):
  soma_p = 0  #numero positivo
  soma_n = 0  #numero negativo
  for n in valores:
    if n > 0:
     soma_p += n     #Se positivo executa a soma
    else:
      soma_n += n   #Se negativo executa a soma
  return soma_p, soma_n    #Retorna multiplos valores (resultados do codigo)

valores = [2, -1, 3, -4]      #Criacao de uma lista
soma_p, soma_n = soma_pn(valores)     #Aplica a variavel "valores" (no caso uma lista) a funcao "soma_pn"

print(f'soma dos positivos = {soma_p} \nsoma dos negativos = {soma_n}')

def somas(valores):
  soma, soma2 = 0, 0
  for num in valores:
    soma = soma + num
    soma2 = soma + num**2
  return soma, soma2

valores = [1, 2, 3]

soma, soma2, = somas(valores)

print(f'soma = {soma}\nsoma2 = {soma2}')