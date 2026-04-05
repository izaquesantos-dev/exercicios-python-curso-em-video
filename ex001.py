# Exercício 001 - Curso em Vídeo - variavel - cores - soma
nome=input('Qual é seu nome ?')
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m'}
print('Olá {} prazer em te conhecer, vamos fazer um exercio?'.format(nome))
n1=int(input('Digite um numero '))
n2=int(input('Digite outro numero '))
s=n1+n2
print('A soma dos numeros {} e {} é igual a {}{}{}!'.format(n1, n2, cores['vermelho'], s, cores['limpa']))
