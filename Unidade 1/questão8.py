print("=== ESTATÍSTICA DESCRITIVA ===")
print("Digite 10 números inteiros:\n")

soma = 0
positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range(1, 11):
    while True:
        try:
            numero = int(input(f"{i}º número: "))
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

    soma += numero

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

media = soma / 10

print("\n" + "="*50)
print("RELATÓRIO ESTATÍSTICO")
print("="*50)
print(f"Soma de todos os números:       {soma}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de números pares:     {pares}")
print(f"Quantidade de números ímpares:   {impares}")
print(f"Média aritmética dos valores:    {media:.2f}")
print("="*50)