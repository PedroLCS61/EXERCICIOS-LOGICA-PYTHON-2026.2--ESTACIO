print("=== ANÁLISE LINGUÍSTICA DE FRASE ===")

frase = input("Digite uma frase: ")

frase_tratada = " ".join(frase.split())
frase_sem_espacos = frase_tratada

total_caracteres = len(frase_sem_espacos)
palavras = frase_sem_espacos.split()
total_palavras = len(palavras)

if total_palavras > 0:
    primeira_palavra = palavras[0]
    ultima_palavra = palavras[-1]
else:
    primeira_palavra = "(frase vazia)"
    ultima_palavra = "(frase vazia)"

while True:
    letra = input("Digite uma letra para contar ocorrências: ")
    if len(letra) == 1 and letra.isalpha():
        break
    else:
        print("Erro: Digite apenas uma letra.")

ocorrencias = frase_sem_espacos.lower().count(letra.lower())

print("\n" + "="*50)
print("RESULTADO DA ANÁLISE")
print("="*50)
print(f"Frase original:        {frase}")
print(f"Quantidade total de caracteres (incluindo espaços): {total_caracteres}")
print(f"Quantidade de palavras: {total_palavras}")
print(f"Primeira palavra:      {primeira_palavra}")
print(f"Última palavra:        {ultima_palavra}")
print(f"Ocorrências da letra '{letra}': {ocorrencias}")
print(f"Frase em maiúsculas:   {frase_sem_espacos.upper()}")
print(f"Frase em minúsculas:   {frase_sem_espacos.lower()}")
print("="*50)