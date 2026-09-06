celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

print("\n" + "="*40)
print("CONVERSÃO DE TEMPERATURA")
print("="*40)
print(f"Celsius:    {celsius:.2f} °C")
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin:     {kelvin:.2f} K")
print("="*40)