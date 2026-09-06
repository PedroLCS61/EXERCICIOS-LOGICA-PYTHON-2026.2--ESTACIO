def main():
    print("=" * 50)
    print("        CADASTRO DE PERFIL PESSOAL")
    print("=" * 50)

    nome = input("Nome completo: ").strip()
    while not nome:
        print("Erro: O nome não pode estar vazio.")
        nome = input("Nome completo: ").strip()

    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Erro: A idade deve ser um número inteiro não negativo.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido para a idade.")

    while True:
        try:
            altura = float(input("Altura (em metros): "))
            if altura <= 0:
                print("Erro: A altura deve ser um valor positivo.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número válido para a altura.")

    cidade = input("Cidade onde reside: ").strip()
    while not cidade:
        print("Erro: A cidade não pode estar vazia.")
        cidade = input("Cidade onde reside: ").strip()

    print("\n" + "=" * 50)
    print("          CARTÃO DE IDENTIFICAÇÃO PESSOAL")
    print("=" * 50)
    print(f"Nome completo:   {nome}")
    print(f"Idade:           {idade} anos")
    print(f"Altura:          {altura:.2f} m")
    print(f"Cidade:          {cidade}")
    print("=" * 50)
    print("         Dados cadastrados com sucesso!")

if __name__ == "__main__":
    main()