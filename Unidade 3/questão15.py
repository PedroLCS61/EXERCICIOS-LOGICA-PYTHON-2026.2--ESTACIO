print("=== CADASTRO E ANÁLISE POPULACIONAL DE CIDADES ===")
print("Cadastre pelo menos 5 cidades:\n")

cidades = []

quantidade_cidades = int(input("Quantas cidades deseja cadastrar? (mínimo 5): "))

while quantidade_cidades < 5:
    print("Erro: Mínimo de 5 cidades. Tente novamente.")
    quantidade_cidades = int(input("Quantas cidades deseja cadastrar? (mínimo 5): "))

for i in range(1, quantidade_cidades + 1):
    print(f"\n--- Cidade {i} ---")
    
    nome = input("Nome da cidade: ")
    
    while True:
        estado = input("Estado (sigla de 2 letras): ").upper()
        if len(estado) == 2 and estado.isalpha():
            break
        else:
            print("Erro: Digite uma sigla válida com 2 letras.")
    
    while True:
        try:
            populacao = int(input("População estimada: "))
            if populacao >= 0:
                break
            else:
                print("Erro: A população não pode ser negativa.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")
    
    cidade = {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }
    cidades.append(cidade)

cidade_maior_populacao = cidades[0]
cidade_menor_populacao = cidades[0]
populacao_total = 0

for cidade in cidades:
    populacao_total += cidade["populacao"]
    
    if cidade["populacao"] > cidade_maior_populacao["populacao"]:
        cidade_maior_populacao = cidade
    
    if cidade["populacao"] < cidade_menor_populacao["populacao"]:
        cidade_menor_populacao = cidade

media_populacional = populacao_total / len(cidades)

print("\n" + "="*70)
print("DADOS DAS CIDADES CADASTRADAS")
print("="*70)
print(f"{'Nº':<4} {'Cidade':<25} {'Estado':<8} {'População':<15}")
print("-"*70)

for i, cidade in enumerate(cidades, start=1):
    print(f"{i:<4} {cidade['nome']:<25} {cidade['estado']:<8} {cidade['populacao']:<15,}")

print("\n" + "="*70)
print("ANÁLISE POPULACIONAL")
print("="*70)
print(f"Cidade com maior população:  {cidade_maior_populacao['nome']} ({cidade_maior_populacao['estado']}) - {cidade_maior_populacao['populacao']:,} habitantes")
print(f"Cidade com menor população:  {cidade_menor_populacao['nome']} ({cidade_menor_populacao['estado']}) - {cidade_menor_populacao['populacao']:,} habitantes")
print(f"População total:             {populacao_total:,} habitantes")
print(f"Média populacional:          {media_populacional:.2f} habitantes")
print("="*70)