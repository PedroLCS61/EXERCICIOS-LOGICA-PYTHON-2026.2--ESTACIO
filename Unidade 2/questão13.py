print("=== AGENDA ELETRÔNICA ===")
print("Cadastre pelo menos 5 contatos:\n")

agenda = []

quantidade_contatos = int(input("Quantos contatos deseja cadastrar? (mínimo 5): "))

while quantidade_contatos < 5:
    print("Erro: Mínimo de 5 contatos. Tente novamente.")
    quantidade_contatos = int(input("Quantos contatos deseja cadastrar? (mínimo 5): "))

for i in range(1, quantidade_contatos + 1):
    print(f"\n--- Contato {i} ---")
    
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    agenda.append(contato)

print("\n" + "="*60)
print("CONTATOS CADASTRADOS")
print("="*60)
print(f"{'Nº':<4} {'Nome':<20} {'Telefone':<15} {'E-mail':<25}")
print("-"*60)

for i, contato in enumerate(agenda, start=1):
    print(f"{i:<4} {contato['nome']:<20} {contato['telefone']:<15} {contato['email']:<25}")

print("="*60)

print("\n" + "="*60)
print("CONSULTA DE CONTATO")
print("="*60)

nome_busca = input("Digite o nome do contato que deseja buscar: ")

contato_encontrado = None

for contato in agenda:
    if contato["nome"].lower() == nome_busca.lower():
        contato_encontrado = contato
        break

if contato_encontrado:
    print("\n" + "-"*60)
    print("CONTATO ENCONTRADO")
    print("-"*60)
    print(f"Nome:      {contato_encontrado['nome']}")
    print(f"Telefone:  {contato_encontrado['telefone']}")
    print(f"E-mail:    {contato_encontrado['email']}")
    print("-"*60)
else:
    print("\n" + "-"*60)
    print("Contato não encontrado.")
    print("-"*60)

print("="*60)