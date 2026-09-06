def exibir_menu():
    """Função para exibir o menu principal"""
    print("\n" + "="*40)
    print("GERENCIAMENTO DE NÚMEROS")
    print("="*40)
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")
    print("="*40)

def cadastrar_numero(lista):
    """Função para cadastrar um número"""
    try:
        numero = float(input("Digite o número a ser cadastrado: "))
        lista.append(numero)
        print(f"Número {numero} cadastrado com sucesso!")
    except ValueError:
        print("Erro: Digite um valor numérico válido.")

def listar_numeros(lista):
    """Função para listar todos os números"""
    if not lista:
        print("Nenhum número cadastrado.")
    else:
        print("\nNúmeros cadastrados:")
        for i, num in enumerate(lista, start=1):
            print(f"  {i}º: {num}")

def exibir_maior(lista):
    """Função para exibir o maior número"""
    if not lista:
        print("Nenhum número cadastrado.")
    else:
        maior = max(lista)
        print(f"Maior número cadastrado: {maior}")

def exibir_menor(lista):
    """Função para exibir o menor número"""
    if not lista:
        print("Nenhum número cadastrado.")
    else:
        menor = min(lista)
        print(f"Menor número cadastrado: {menor}")

def calcular_media(lista):
    """Função para calcular e exibir a média"""
    if not lista:
        print("Nenhum número cadastrado.")
    else:
        media = sum(lista) / len(lista)
        print(f"Média dos números cadastrados: {media:.2f}")

print("=== SISTEMA DE GERENCIAMENTO DE NÚMEROS ===")

numeros = []

while True:
    exibir_menu()
    
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
        continue
    
    if opcao == 0:
        print("\nEncerrando o programa... Obrigado por utilizar!")
        break
    elif opcao == 1:
        cadastrar_numero(numeros)
    elif opcao == 2:
        listar_numeros(numeros)
    elif opcao == 3:
        exibir_maior(numeros)
    elif opcao == 4:
        exibir_menor(numeros)
    elif opcao == 5:
        calcular_media(numeros)
    else:
        print("Opção inválida! Tente novamente.")