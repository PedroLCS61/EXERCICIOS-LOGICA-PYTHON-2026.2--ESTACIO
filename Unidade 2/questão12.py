print("=== SISTEMA DE CONTROLE DE ESTOQUE ===")
print("Cadastre pelo menos 5 produtos:\n")

produtos = []

quantidade_produtos = int(input("Quantos produtos deseja cadastrar? (mínimo 5): "))

while quantidade_produtos < 5:
    print("Erro: Mínimo de 5 produtos. Tente novamente.")
    quantidade_produtos = int(input("Quantos produtos deseja cadastrar? (mínimo 5): "))

for i in range(1, quantidade_produtos + 1):
    print(f"\n--- Produto {i} ---")
    
    nome = input("Nome do produto: ")
    
    while True:
        try:
            preco = float(input("Preço unitário: R$ "))
            if preco >= 0:
                break
            else:
                print("Erro: O preço não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
    
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade >= 0:
                break
            else:
                print("Erro: A quantidade não pode ser negativa.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)

print("\n" + "="*60)
print("PRODUTOS CADASTRADOS")
print("="*60)
print(f"{'Nº':<4} {'Produto':<20} {'Preço':<12} {'Quantidade':<12}")
print("-"*60)

for i, produto in enumerate(produtos, start=1):
    print(f"{i:<4} {produto['nome']:<20} R$ {produto['preco']:<9.2f} {produto['quantidade']:<12}")

valor_total_estoque = 0
for produto in produtos:
    valor_total_estoque += produto["preco"] * produto["quantidade"]

print("\n" + "="*60)
print(f"VALOR TOTAL DO ESTOQUE: R$ {valor_total_estoque:.2f}")
print("="*60)

produto_mais_caro = produtos[0] 

for produto in produtos:
    if produto["preco"] > produto_mais_caro["preco"]:
        produto_mais_caro = produto

print("\n" + "="*60)
print("PRODUTO COM MAIOR PREÇO UNITÁRIO")
print("="*60)
print(f"Nome:        {produto_mais_caro['nome']}")
print(f"Preço:       R$ {produto_mais_caro['preco']:.2f}")
print(f"Quantidade:  {produto_mais_caro['quantidade']}")
print("="*60)