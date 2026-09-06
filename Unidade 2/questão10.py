print("=== ANÁLISE DE TEMPERATURAS SEMANAIS ===")
print("Digite as temperaturas dos 7 dias da semana:\n")

temperaturas = []

for dia in range(1, 8):
    while True:
        try:
            temp = float(input(f"Temperatura do {dia}º dia: "))
            temperaturas.append(temp)
            break
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

maior_temp = max(temperaturas)
menor_temp = min(temperaturas)
media = sum(temperaturas) / len(temperaturas)

dias_acima_media = 0
for temp in temperaturas:
    if temp > media:
        dias_acima_media += 1

print("\n" + "="*50)
print("RELATÓRIO DE TEMPERATURAS")
print("="*50)

print("Temperaturas registradas:")
for i, temp in enumerate(temperaturas, start=1):
    print(f"  Dia {i}: {temp:.1f}°C")

print("\n" + "-"*50)
print(f"Maior temperatura:        {maior_temp:.1f}°C")
print(f"Menor temperatura:        {menor_temp:.1f}°C")
print(f"Temperatura média:        {media:.2f}°C")
print(f"Dias acima da média:      {dias_acima_media} dia(s)")
print("="*50)