print("=== TABUADA DE MULTIPLICAÇÃO ===")

while True:
    try:
        numero = int(input("Digite um número inteiro para ver sua tabuada: "))
        break
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

print(f"\nTabuada do {numero}:")
print("="*20)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado:3}")

print("="*20)