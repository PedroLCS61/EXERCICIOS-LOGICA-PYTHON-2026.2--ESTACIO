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
            print("Erro: Digite um número válido. Tente novamente.")

print("=== SISTEMA DE VERIFICAÇÃO ACADÊMICA ===")
print("Digite as notas (0 a 10):\n")

nota1 = validar_nota("1ª nota: ")
nota2 = validar_nota("2ª nota: ")
nota3 = validar_nota("3ª nota: ")

media = (nota1 + nota2 + nota3) / 3

if media >= 7.0:
    situacao = "Aprovado"
elif 5.0 <= media < 7.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n" + "="*50)
print("RESULTADO")
print("="*50)
print(f"Notas informadas: {nota1:.1f}, {nota2:.1f}, {nota3:.1f}")
print(f"Média calculada:  {media:.2f}")
print(f"Situação final:   {situacao}")
print("="*50)