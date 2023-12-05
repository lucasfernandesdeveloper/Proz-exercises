"""
# Exercício 1 - Soma de dois números 

# Getting the numbers that are going to be added
number1 = int(input("Informe um número: "))
number2 = int(input("Informe outro número: "))

# The result
result = number1 + number2
print("O resultado da some é:", result)


# Exercício 2 - Média de notas

# Getting the grandes 
grades = []
grade1 = int(input("Informe a primeira nota: "))
grades.append(grade1)

grade2 = int(input("Informe a segunda nota: "))
grades.append(grade2)

grade3 = int(input("Informe a terceira nota: "))
grades.append(grade3)

# Average value
average = sum(grades) / len(grades)
print("A média é:", average)
"""

# Decraração de variavel do tipo inteiro = 
#quantidadeFaltas = 15

# Decraração de variavel do tipo string = tipo texto

#Decraração de variavel do tipo real
#quantidadeMetros = 2.5

#print('Olá mundo')
#print('Faltas =',quantidadeFaltas)
#print('Nome no jogo =',nickName)
#print('Quantidade de Metros =',quantidadeMetros)
 #Declaração de Área do retângulo
#alturaretângulo = 5
#larguraretângulo= 3

#print('Altura do Retângulo =',alturaretângulo)
#print('Largura do Retângulo =',larguraretângulo)
#totalÁrea = alturaretângulo*larguraretângulo
#print('Área Total do Retângulo =',totalÁrea)
#Quadro de operações
#numero1 = 12
#numero2 = 6
#soma
#print(numero1+numero2)
#subtrair
#print(numero1-numero2)
#multiplicação
#print(numero1*numero2)
#divisão
#print(numero1/numero2)

#nick = input('Escolha o seu nickname:')
#print('O nickname escolhido foi:',nick)

#estadoCivil = input('Digite aqui seu Estado Civil: ')
#print('Você está atualmente',estadoCivil,'(a)')

#numero1 = int(input('Digite um número:'))
#numero2 = int(input('Digite outro número:'))

#totalsoma = print('O resultado da soma é:',numero1+numero2)

#numero = int(input('Digite  o valor do número'))
#if numero % 2 ==0:
  #print('O numero é par')
#else:
  #print('O numero é impar') 
#Celsius = float(input('Digite uma valor de graus celsius para converto-lo para Fahrenheit:'))
#Fahrenheit = (Celsius*9/5)+32

#print(Fahrenheit,'É o valor Fahrenheit')

 #Declaração de Área do retângulo;
#alturaretângulo = int(input('Determine a altura do retângulo:'))
#larguraretângulo= int(input('Determine a largura do retângulo:'))

#print ('Altura do Retângulo =',(alturaretângulo))
#print('Largura do Retângulo =',(larguraretângulo))
#totalÁrea = alturaretângulo*larguraretângulo
#print('Área Total do Retângulo =',totalÁrea)0
  
#Cálculo de IMC;
#peso = float(input('Quanto voçê pesa? '))
#Altura = float(input('Qua é sua altura? '))
#IMC = peso/(Altura*Altura)

#print('Seu Índice de Massa corporal é:',IMC)

#Desconto de produto;
#valorProduto = int(input('quanto vale um saco de feijão? '))
#descontoProduto = int(input('qual será o Desconto desse produto?'))
#descAplicado = valorProduto - ((valorProduto/100)*descontoProduto)
#print('O desconto a plicado equivale a:',descAplicado)

#número menor e numero maior;
#numero1 = int(input('Digite o valor do número 1:')) 
#numero2 = int(input('Digite  o valor do número 2:'))
#if numero1<numero2:
#  print('O',numero1,'é menor que o',numero2)
#else:
#  print('O',numero1,'é maior que o',numero2) 

#Idade minima para dirigir;
#idade = int(input('qual é a sua idade?'))
#if idade>17:
 #  print('Com',idade,'anos, você já pode dirigir')
#else:
#   print('Com',idade,'anos, você não pode dirigir')

#Numero nagativo positivo ou zero;
#numero1 = int(input('Digite um número:'))
#if numero1>0.1:
#  print('O número que você digitou é positivo')
#if numero1<-0.1:
# print('O número que você digitou é negativo')
#if numero1 ==0:
  #print('O número que você digitou é zero')
  
#Clssificação de triângulos;
#lado1 = int(input('Digite o valor de um dos lados do triângulo'))
#lado2 = int(input('Digite o valor de outro lado do triângulo'))
#lado3 = int(input('Digite o valor de último lado do triângulo'))

#if lado1 == lado2 == lado3:
#  print ('O triângulo é equilátero.')
#elif lado1 == lado2 != lado3:
#  print('O triângulo é isósceles')
#elif lado2 == lado3 !=lado1:
#  print('O triângulo é isósceles')
#elif lado3 == lado1 !=lado2:
#  print('O triângulo é isósceles')
#else:
#  print('O triângulo é escaleno')
  
#Aprovação em disciplina
#nota = int(input('Qual foi a sua nota?'))
#if nota>7:
#  print('Você foi aprovado(a)')
#else:
#  print('Você foi reprovado(a)')

#numero = int(input('Digite um número para verificar se ele é divisível por 3 e 5:'))
#if numero %3==0 and numero %5==0:
#   print (numero,'é divisível por 3 e 5')
#else:
#  print(numero,'Não é divisível por 3 e 5') 

  #8 Vogal ou consoante
#Letra = str(input('Digite uma letra para verificar se ela é Vogal ou Consoante:'))
#if Letra == 'a' or Letra == 'e' or Letra == 'i' or Letra == 'o' or Letra == 'u':
#  print('A letra',Letra,'é uma Vogal')
#else:
#  print('A letra',Letra,'é uma Consoante')
  
  #9 Cálculo de desconto com a condição
#valor de um produto aplicar o desconto apenas se for maior que R$100
#valorProduto = int(input('quanto vale um pc gamer? '))
#if valorProduto<100:
#  print('O desconto será aplicado só se o pc gamer custar mais de 100 reais.')
#else:
#  descontoProduto = int(input('qual será o Desconto desse produto?'))
#  descAplicado = valorProduto - ((valorProduto/100)*descontoProduto)
#  print('Com desconto a plicado o valor equivale a:',descAplicado)
  
  

#10 ClassificaçãO De idade (criança, Adolescente, Adulto jovem, Adulto)
#idade = int(input('Qual é a sua idade? '))
#if idade<11.1:
#  print('Você ainda é uma Criança.')
#if idade>11.9 and idade<17.9:
#  print('Você é um Adolescente.')
#if idade>18.9 and idade<24.9:
#  print('Você é um Jovem Adulto')
#if idade>24.9:
#  print('Você é um Adulto')

#while
#x = 1
#soma = 0
#while x<=5:
#    x=x+1
#    numero = int(input('Digite um número para somar:'))
#    soma = soma + numero
#    print(soma)
#soma=0
#x = 1
#while x<=1:
#    x=x+1
#    numero = int(input('Digite um número para ver a tabuada dele:'))
#    print('(1 x',numero,'=',numero*1,')')
#    print('(2 x',numero,'=',numero*2,')')
#    print('(3 x',numero,'=',numero*3,')')
#    print('(4 x',numero,'=',numero*4,')')
#    print('(5 x',numero,'=',numero*5,')')
#    print('(6 x',numero,'=',numero*6,')')
#    print('(7 x',numero,'=',numero*7,')')
#    print('(8 x',numero,'=',numero*8,')')
#    print('(9 x',numero,'=',numero*9,')')
#    print('(10 x',numero,'=',numero*10,')')

#Numero pares entre entervalos
#primeiro = 0
#segundo= 0
#primeiro =int(input('escreva o valor inicial:' ))
#segundo = int(input('Escreva o valor final:'))
#print('Os Números pares entre',primeiro,'e',segundo,'são:')
#while primeiro<=segundo:
#    primeiro = primeiro+1
#    if primeiro%2==0:
#        print(primeiro,'')

#Adivinhar Número aleatório:


#import random


#palpite = 0
#numeroSecreto = random.randint(1,100)
#while palpite !=numeroSecreto:
#  palpite = int(input('Tente adivinhar um número secreto entre 1 e 100:'))
#  if palpite<numeroSecreto:
#    print('tente um número maior.')
#  elif palpite>numeroSecreto:
#    print('tente um número menor.')
#  else:
#    print('Parabéns! Você acertou o número secreto.')

#Número Primo
#numero = int(input('Digite o número:'))
#x = 1
#contador = 0
#while x<=numero:
#    if numero %x ==0:
#        contador += 1
#    x = x+1    
#if contador == 2:
#    print('O número',numero,'é um número primo.')
#else:
#    print('O número',numero,'não é primo.')

#Calcular Fatoreal.
#numero = int(input('digite um número para calcular:'))
#x = numero *1
#resultado = numero
#while x>=1:
#    resultado = resultado * 


     


    




    

  
 



  
  
  






  
  
  
  
   
   
  










