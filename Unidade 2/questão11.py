print("=== RELATÓRIO ANALÍTICO DE LISTA NUMÉRICA ===")
print("Digite 10 números inteiros:\n")

numeros = []

for i in range(1, 11):
    while True:
        try:
            num = int(input(f"{i}º número: "))
            numeros.append(num)
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("\n" + "="*50)
print("RELATÓRIO ANALÍTICO")
print("="*50)

print(f"Números informados: {numeros}")
print(f"Números pares:      {pares}")
print(f"Números ímpares:    {impares}")
print(f"Soma dos valores:   {soma}")
print(f"Média dos valores:  {media:.2f}")
print(f"Maior valor:        {maior}")
print(f"Menor valor:        {menor}")
print("="*50)