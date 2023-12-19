
"""
def verificaPar(number):
    if number % 2 == 0:
        print("O número é par")
        vet.append(number) 
    else:
        print("O número é ímpar, não será adicionado ao vetor")

vet = []
x = 0
while x <= 10: 
    number = int(input("Digite um valor: "))
    verificaPar(number)
    x += 1
print(vet)
"""
############### Soma de Vetores ###################
def preencherVet(n):
    vet = []
    x = 0
    while x < n: 
        vet.append(int(input("Informe um número: ")))
        x +=1
    return vet
        
""""
vOne = preencherVet(5)
vTwo = preencherVet(5)

soma = 0
result = 0

result = sum(vOne)
result += sum(vTwo)
print(result)

############### Média de Vetores ##################
"""
vOne = preencherVet(5)
vTwo = preencherVet(5)

total = sum(vOne)
total += sum(vTwo)

lenOne = len(vOne)
lenTwo = len(vTwo)

lenght = lenOne + lenTwo

print(int(total / lenght))
