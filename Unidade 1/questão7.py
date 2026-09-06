print("=== ANÁLISE DE SINAL E PARIDADE ===")
numero = int(input("Digite um número inteiro: "))

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "nulo"

if numero == 0:
    paridade = "par"
    mensagem = f"O número {numero} é {sinal} e {paridade}."
else:
    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"
    mensagem = f"O número {numero} é {sinal} e {paridade}."

print("\n" + "="*50)
print("RESULTADO DA ANÁLISE")
print("="*50)
print(mensagem)
print("="*50)