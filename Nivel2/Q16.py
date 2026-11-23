n = int(input("Quantos números deseja informar (1 a 8)?: "))

while n < 1 or n > 8:
    n = int(input("Digite uma quantidade de 1 a 8: "))

soma = 0

for i in range(n):
    numero = int(input("Digite um número: "))
    soma += numero

media = soma / n

print("Soma:", soma)
print("Média:", media)