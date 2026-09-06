def validar_idade():
    """Função para validar se a idade é um número não negativo"""
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade >= 0:
                return idade
            else:
                print("Erro: A idade não pode ser negativa. Tente novamente.")
        except ValueError:
            print("Erro: Digite um número inteiro válido. Tente novamente.")

print("=== CLASSIFICAÇÃO ETÁRIA ===")
idade = validar_idade()

if idade <= 12:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print("\n" + "="*40)
print("RESULTADO")
print("="*40)
print(f"Idade informada: {idade} anos")
print(f"Classificação:   {classificacao}")
print("="*40)