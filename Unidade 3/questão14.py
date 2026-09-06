def validar_nota(mensagem):
    """Função para validar se a nota está entre 0 e 10"""
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

def calcular_media(notas):
    """Função para calcular a média das três notas"""
    return sum(notas) / len(notas)

def determinar_situacao(media):
    """Função para determinar a situação do estudante"""
    if media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar_estudante():
    """Função para cadastrar um estudante"""
    print("\n--- Cadastro de Estudante ---")
    nome = input("Nome do estudante: ")
    
    print("Digite as 3 notas (0 a 10):")
    nota1 = validar_nota("1ª nota: ")
    nota2 = validar_nota("2ª nota: ")
    nota3 = validar_nota("3ª nota: ")
    
    notas = [nota1, nota2, nota3]
    media = calcular_media(notas)
    situacao = determinar_situacao(media)
    
    estudante = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }
    
    return estudante

print("=== SISTEMA DE GERENCIAMENTO DE NOTAS ===")
print("Cadastre pelo menos 5 estudantes:\n")

turma = []

quantidade_estudantes = int(input("Quantos estudantes deseja cadastrar? (mínimo 5): "))

while quantidade_estudantes < 5:
    print("Erro: Mínimo de 5 estudantes. Tente novamente.")
    quantidade_estudantes = int(input("Quantos estudantes deseja cadastrar? (mínimo 5): "))

for i in range(1, quantidade_estudantes + 1):
    print(f"\nEstudante {i}:")
    estudante = cadastrar_estudante()
    turma.append(estudante)

print("\n" + "="*70)
print("DADOS DA TURMA")
print("="*70)
print(f"{'Nº':<4} {'Nome':<20} {'Nota 1':<8} {'Nota 2':<8} {'Nota 3':<8} {'Média':<8} {'Situação':<12}")
print("-"*70)

for i, estudante in enumerate(turma, start=1):
    notas = estudante['notas']
    print(f"{i:<4} {estudante['nome']:<20} {notas[0]:<8.1f} {notas[1]:<8.1f} {notas[2]:<8.1f} {estudante['media']:<8.2f} {estudante['situacao']:<12}")

print("="*70)

estudante_maior_media = turma[0]
estudante_menor_media = turma[0]

for estudante in turma:
    if estudante["media"] > estudante_maior_media["media"]:
        estudante_maior_media = estudante
    if estudante["media"] < estudante_menor_media["media"]:
        estudante_menor_media = estudante

print("\n" + "="*70)
print("DESTAQUES DA TURMA")
print("="*70)
print(f"Estudante com maior média:  {estudante_maior_media['nome']} - Média: {estudante_maior_media['media']:.2f}")
print(f"Estudante com menor média:  {estudante_menor_media['nome']} - Média: {estudante_menor_media['media']:.2f}")
print("="*70)

aprovados = 0
recuperacao = 0
reprovados = 0

for estudante in turma:
    if estudante["situacao"] == "Aprovado":
        aprovados += 1
    elif estudante["situacao"] == "Recuperação":
        recuperacao += 1
    else:
        reprovados += 1

print("\n" + "="*70)
print("ESTATÍSTICAS DA TURMA")
print("="*70)
print(f"Estudantes aprovados:      {aprovados}")
print(f"Estudantes em recuperação: {recuperacao}")
print(f"Estudantes reprovados:     {reprovados}")
print("="*70)