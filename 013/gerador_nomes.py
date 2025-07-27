
import random

ADJETIVOS = [
    "rapido", "veloz", "agil", "sonolento", "curioso", "valente",
    "esperto", "sabio", "vermelho", "azul", "verde", "dourado"
]

SUBSTANTIVOS = [
    "leao", "tigre", "rio", "sol", "lua", "fantasma",
    "guerreiro", "mago", "dragao", "corvo", "lobo", "trovao"
]

def gerar_nomes_aleatorios(quantidade):

    print("\n--- Gerando Nomes de Usuário ---\n")
    if quantidade <= 0:
        print("Por favor, insira um número maior que zero.")
        return

    for i in range(quantidade):
        # 1. Escolhe um adjetivo e um substantivo aleatoriamente das listas.
        adjetivo_sorteado = random.choice(ADJETIVOS)
        substantivo_sorteado = random.choice(SUBSTANTIVOS)

        # 2. Gera um número aleatório entre 10 e 99.
        numero_aleatorio = random.randint(10, 99)

        # 3. Combina as partes para formar o nome de usuário.
        nome_gerado = f"{adjetivo_sorteado}_{substantivo_sorteado}{numero_aleatorio}"

        # 4. Imprime o nome gerado.
        print(f"Nome {i+1}: {nome_gerado}")

    print("\n--- Geração Concluída ---")

if __name__ == "__main__":
    print("--- Bem-vindo ao Gerador de Nomes de Usuário ---")

    try:
        num_nomes = int(input("Quantos nomes de usuário você quer gerar? "))
        gerar_nomes_aleatorios(num_nomes)

    except ValueError:
        print("\nErro: Entrada inválida. Por favor, digite um número inteiro.")