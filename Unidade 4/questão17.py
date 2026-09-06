import math

print("=== CÁLCULOS MATEMÁTICOS COM O MÓDULO MATH ===")

while True:
    try:
        numero = float(input("Digite um número real: "))
        break
    except ValueError:
        print("Erro: Digite um valor numérico válido.")

print("\n" + "="*50)
print("RESULTADOS DOS CÁLCULOS")
print("="*50)

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"Raiz quadrada:                  {raiz:.4f}")
else:
    print("Raiz quadrada:                  Não existe (número negativo)")

absoluto = math.fabs(numero)
print(f"Valor absoluto (módulo):        {absoluto:.4f}")

teto = math.ceil(numero)
print(f"Arredondamento para cima: {teto}")

piso = math.floor(numero)
print(f"Arredondamento para baixo: {piso}")

if numero >= 0 and numero.is_integer():
    fatorial = math.factorial(int(numero))
    print(f"Fatorial:                        {fatorial}")
else:
    print("Fatorial:                        O número deve ser inteiro e não negativo")

print("="*50)