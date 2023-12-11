################### Vetores #######################

"""
############### Soma de Vetores ###################
vetorOne = [8, 3, 7, 10]
vetorTwo = [7, 3, 10]

soma = 0
result = 0

result = sum(vetorOne)
result += sum(vetorTwo)
print(result)

############### Média de Vetores ##################
vetorOne = [8, 3, 7, 10]
vetorTwo = [7, 3, 10]

total = sum(vetorOne)
total += sum(vetorTwo)

lenOne = len(vetorOne)
lenTwo = len(vetorTwo)

lenght = lenOne + lenTwo

print(int(total / lenght))

################# Maior Elemento #################
vetorOne = [8, 3, 7, 10]
highest = max(vetorOne)
print(highest)

############ Ordenação de vetores ################
vetorOne = [3, 7, 10]

sortedVetor = sorted(vetorOne)
print(sortedVetor)

############# Vetor Invertido ###################
vetorOne = [8, 3, 7, 10]
vetorOne.reverse()

print(vetorOne)

############## Vetor Primo ######################
vetorPrimo = []
number = 0 
i = 1
aux = 0

number = int(input("Informe um número: "))

while i <= number: 
    if (number % i == 0): 
        aux = aux + 1
    i += 1

if aux == 2:
    vetorPrimo.append(number)
print(vetorPrimo)

############ Frequência de Elementos ############
vetor = [1,2,2, 3,3,3, 4,4,4,4, 5,5,5,5,5]
number = int(input("Digite um número: "))
totalt = 0

for value in vetor:
    if number == value:
        totalt += 1
print(totalt)

############### Soma de Vetores #################
    
"""