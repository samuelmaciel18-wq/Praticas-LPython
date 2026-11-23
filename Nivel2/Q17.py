soma = 0
aprovados = 0
i = 1

while i <= 5:
    nota = float(input(f"Digite a nota {i}: "))

    if nota < 1 or nota > 10:
        print("Nota inválida! Digite novamente.")
    else:
        soma += nota

        if nota >= 6:
            aprovados += 1

        i += 1

media = soma / 5

print("Média:", media)
print("Notas maiores ou iguais a 6:", aprovados)