num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n" + "="*40)
print("RESULTADOS")
print("="*40)

print(f"{num1} + {num2} = {num1 + num2}")

print(f"{num1} - {num2} = {num1 - num2}")

print(f"{num1} × {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} ÷ {num2} = {num1 / num2}")
else:
    print("Divisão por zero não permitida")

if num2 != 0:
    print(f"{num1} // {num2} = {num1 // num2}")
else:
    print("Divisão por zero não permitida")

if num2 != 0:
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Divisão por zero não permitida")

print(f"{num1} ** {num2} = {num1 ** num2}")

print("="*40)