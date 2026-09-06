import os
import time

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa a execução até o usuário pressionar Enter"""
    input("\nPressione Enter para continuar...")

def validar_nota(mensagem):
    """Valida se a nota está entre 0 e 10"""
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

def validar_idade(mensagem):
    """Valida se a idade é um inteiro positivo"""
    while True:
        try:
            idade = int(input(mensagem))
            if idade > 0:
                return idade
            else:
                print("Erro: A idade deve ser um número positivo.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def calcular_media(notas):
    """Calcula a média de três notas"""
    return sum(notas) / len(notas)

def determinar_situacao(media):
    """Determina a situação acadêmica baseada na média"""
    if media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar_estudante(turma):
    """Cadastra um novo estudante"""
    limpar_tela()
    print("="*50)
    print("CADASTRAR ESTUDANTE")
    print("="*50)
    
    nome = input("Nome: ").strip()
    if not nome:
        print("Erro: O nome não pode ser vazio.")
        pausar()
        return
    
    idade = validar_idade("Idade: ")
    curso = input("Curso: ").strip()
    
    print("\nDigite as 3 notas (0 a 10):")
    nota1 = validar_nota("1ª nota: ")
    nota2 = validar_nota("2ª nota: ")
    nota3 = validar_nota("3ª nota: ")
    
    notas = [nota1, nota2, nota3]
    media = calcular_media(notas)
    situacao = determinar_situacao(media)
    
    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }
    
    turma.append(estudante)
    print(f"\nEstudante {nome} cadastrado com sucesso!")
    pausar()

def listar_estudantes(turma):
    """Lista todos os estudantes cadastrados"""
    limpar_tela()
    print("="*50)
    print("LISTAR ESTUDANTES")
    print("="*50)
    
    if not turma:
        print("Nenhum estudante cadastrado.")
        pausar()
        return
    
    print(f"{'Nº':<4} {'Nome':<20} {'Idade':<6} {'Curso':<15} {'Média':<8} {'Situação':<12}")
    print("-"*70)
    
    for i, est in enumerate(turma, start=1):
        print(f"{i:<4} {est['nome']:<20} {est['idade']:<6} {est['curso']:<15} {est['media']:<8.2f} {est['situacao']:<12}")
    
    print("-"*70)
    pausar()

def consultar_estudante(turma):
    """Consulta um estudante pelo nome"""
    limpar_tela()
    print("="*50)
    print("CONSULTAR ESTUDANTE")
    print("="*50)
    
    if not turma:
        print("Nenhum estudante cadastrado.")
        pausar()
        return
    
    nome_busca = input("Digite o nome do estudante: ").strip().lower()
    
    encontrado = False
    for est in turma:
        if est["nome"].lower() == nome_busca:
            print("\n" + "-"*50)
            print("DADOS DO ESTUDANTE")
            print("-"*50)
            print(f"Nome:     {est['nome']}")
            print(f"Idade:    {est['idade']}")
            print(f"Curso:    {est['curso']}")
            print(f"Notas:    {est['notas'][0]:.1f}, {est['notas'][1]:.1f}, {est['notas'][2]:.1f}")
            print(f"Média:    {est['media']:.2f}")
            print(f"Situação: {est['situacao']}")
            print("-"*50)
            encontrado = True
            break
    
    if not encontrado:
        print("\nEstudante não encontrado.")
    
    pausar()

def alterar_estudante(turma):
    """Altera os dados de um estudante existente"""
    limpar_tela()
    print("="*50)
    print("ALTERAR DADOS")
    print("="*50)
    
    if not turma:
        print("Nenhum estudante cadastrado.")
        pausar()
        return
    
    nome_busca = input("Digite o nome do estudante a ser alterado: ").strip().lower()
    
    for est in turma:
        if est["nome"].lower() == nome_busca:
            print("\nDados atuais:")
            print(f"Nome:     {est['nome']}")
            print(f"Idade:    {est['idade']}")
            print(f"Curso:    {est['curso']}")
            print(f"Notas:    {est['notas']}")
            print(f"Média:    {est['media']:.2f}")
            print(f"Situação: {est['situacao']}")
            
            print("\nO que deseja alterar?")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Curso")
            print("4 - Notas")
            print("5 - Todos os dados")
            print("0 - Cancelar")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                novo_nome = input("Novo nome: ").strip()
                if novo_nome:
                    est["nome"] = novo_nome
                    print("Nome alterado com sucesso!")
            elif opcao == "2":
                est["idade"] = validar_idade("Nova idade: ")
                print("Idade alterada com sucesso!")
            elif opcao == "3":
                est["curso"] = input("Novo curso: ").strip()
                print("Curso alterado com sucesso!")
            elif opcao == "4":
                print("Digite as novas notas:")
                nota1 = validar_nota("1ª nota: ")
                nota2 = validar_nota("2ª nota: ")
                nota3 = validar_nota("3ª nota: ")
                est["notas"] = [nota1, nota2, nota3]
                est["media"] = calcular_media(est["notas"])
                est["situacao"] = determinar_situacao(est["media"])
                print("Notas alteradas com sucesso!")
            elif opcao == "5":
                est["nome"] = input("Novo nome: ").strip()
                est["idade"] = validar_idade("Nova idade: ")
                est["curso"] = input("Novo curso: ").strip()
                print("Digite as novas notas:")
                nota1 = validar_nota("1ª nota: ")
                nota2 = validar_nota("2ª nota: ")
                nota3 = validar_nota("3ª nota: ")
                est["notas"] = [nota1, nota2, nota3]
                est["media"] = calcular_media(est["notas"])
                est["situacao"] = determinar_situacao(est["media"])
                print("Dados alterados com sucesso!")
            elif opcao == "0":
                print("Operação cancelada.")
            else:
                print("Opção inválida.")
            
            pausar()
            return
    
    print("Estudante não encontrado.")
    pausar()

def remover_estudante(turma):
    """Remove um estudante do sistema"""
    limpar_tela()
    print("="*50)
    print("REMOVER ESTUDANTE")
    print("="*50)
    
    if not turma:
        print("Nenhum estudante cadastrado.")
        pausar()
        return
    
    nome_busca = input("Digite o nome do estudante a ser removido: ").strip().lower()
    
    for i, est in enumerate(turma):
        if est["nome"].lower() == nome_busca:
            print(f"\nDados do estudante: {est['nome']} - {est['curso']}")
            confirmacao = input("Tem certeza que deseja remover este estudante? (S/N): ").upper()
            
            if confirmacao == "S":
                turma.pop(i)
                print("Estudante removido com sucesso!")
            else:
                print("Operação cancelada.")
            
            pausar()
            return
    
    print("Estudante não encontrado.")
    pausar()

def gerar_relatorio(turma):
    """Gera um relatório completo da turma"""
    limpar_tela()
    print("="*50)
    print("RELATÓRIO DA TURMA")
    print("="*50)
    
    if not turma:
        print("Nenhum estudante cadastrado.")
        pausar()
        return
    
    total_estudantes = len(turma)
    
    maior_media = turma[0]
    menor_media = turma[0]
    
    for est in turma:
        if est["media"] > maior_media["media"]:
            maior_media = est
        if est["media"] < menor_media["media"]:
            menor_media = est
    
    soma_medias = sum(est["media"] for est in turma)
    media_geral = soma_medias / total_estudantes
    
    aprovados = sum(1 for est in turma if est["situacao"] == "Aprovado")
    recuperacao = sum(1 for est in turma if est["situacao"] == "Recuperação")
    reprovados = sum(1 for est in turma if est["situacao"] == "Reprovado")
    
    print(f"Total de estudantes:    {total_estudantes}")
    print(f"Maior média:            {maior_media['nome']} - {maior_media['media']:.2f}")
    print(f"Menor média:            {menor_media['nome']} - {menor_media['media']:.2f}")
    print(f"Média geral da turma:   {media_geral:.2f}")
    print("-"*50)
    print(f"Aprovados:              {aprovados} ({aprovados/total_estudantes*100:.1f}%)")
    print(f"Recuperação:            {recuperacao} ({recuperacao/total_estudantes*100:.1f}%)")
    print(f"Reprovados:             {reprovados} ({reprovados/total_estudantes*100:.1f}%)")
    print("="*50)
    
    pausar()

def exibir_menu():
    """Exibe o menu principal"""
    limpar_tela()
    print("="*50)
    print("SISTEMA ACADÊMICO")
    print("="*50)
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Consultar estudante")
    print("4 - Alterar dados")
    print("5 - Remover estudante")
    print("6 - Gerar relatório da turma")
    print("0 - Encerrar sistema")
    print("="*50)

def main():
    """Função principal do programa"""
    turma = []
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("Digite a opção desejada: ")
        except KeyboardInterrupt:
            print("\n\nEncerrando o sistema...")
            break
        
        if opcao == "0":
            print("\nEncerrando o sistema... Obrigado por utilizar!")
            break
        elif opcao == "1":
            cadastrar_estudante(turma)
        elif opcao == "2":
            listar_estudantes(turma)
        elif opcao == "3":
            consultar_estudante(turma)
        elif opcao == "4":
            alterar_estudante(turma)
        elif opcao == "5":
            remover_estudante(turma)
        elif opcao == "6":
            gerar_relatorio(turma)
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(1)

if __name__ == "__main__":
    main()