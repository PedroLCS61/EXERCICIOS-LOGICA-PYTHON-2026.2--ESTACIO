print("=== ORDENAÇÃO DE TRÊS NÚMEROS ===")
print("Digite três números inteiros distintos:\n")

num1 = int(input("1º número: "))
num2 = int(input("2º número: "))
num3 = int(input("3º número: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("\nATENÇÃO: Os números devem ser distintos!")
    print("Por favor, execute o programa novamente com números diferentes.")
else:
    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num1 and num2 > num3:
        maior = num2
    else:
        maior = num3
    
    if num1 < num2 and num1 < num3:
        menor = num1
    elif num2 < num1 and num2 < num3:
        menor = num2
    else:
        menor = num3
    
    if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
        mediana = num1
    elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
        mediana = num2
    else:
        mediana = num3
    
    print("\n" + "="*40)
    print("RESULTADO DA ORDENAÇÃO")
    print("="*40)
    print(f"Números informados: {num1}, {num2}, {num3}")
    print(f"Maior número:       {maior}")
    print(f"Menor número:       {menor}")
    print(f"Número mediano:     {mediana}")
    print("="*40)
    
    print(f"\nOrdem crescente: {menor} < {mediana} < {maior}")
    print(f"Ordem decrescente: {maior} > {mediana} > {menor}")