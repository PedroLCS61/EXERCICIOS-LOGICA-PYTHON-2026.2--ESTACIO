import random

print("=== SIMULAÇÃO DE LANÇAMENTO DE DADOS ===\n")

print("--- PARTE 1: Lançamento Único ---")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma = dado1 + dado2

print(f"Resultado do primeiro dado:  {dado1}")
print(f"Resultado do segundo dado:   {dado2}")
print(f"Soma dos dois valores:       {soma}\n")

print("--- PARTE 2: Múltiplos Lançamentos (10 vezes) ---")

contador_soma7 = 0
resultados = []

for i in range(1, 11):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    soma_atual = d1 + d2
    
    resultados.append((d1, d2, soma_atual))
    
    if soma_atual == 7:
        contador_soma7 += 1
    
    print(f"Lançamento {i:2}: Dado 1 = {d1}, Dado 2 = {d2}, Soma = {soma_atual}")

print("\n" + "="*50)
print("ANÁLISE ESTATÍSTICA")
print("="*50)
print(f"Quantidade de vezes que a soma foi igual a 7: {contador_soma7}")
print(f"Percentual de ocorrências: {contador_soma7/10*100:.0f}%")
print("="*50)