from functools import reduce

alunos_dados = [
    {'nome': 'Ana', 'notas': [8, 9, 9.5]},
    {'nome': 'Bruno', 'notas': [5, 6, 7.5]},
    {'nome': 'Carla', 'notas': [9, 9, 10]},
    {'nome': 'Daniel', 'notas': [3, 5, 4.5]},
    {'nome': 'Alice', 'notas': [7, 7, 7]},
]


def calcular_media(aluno):
    notas = aluno['notas']
    media = sum(notas) / len(notas)
    return {'nome': aluno['nome'], 'media': round(media, 2)}

def foi_aprovado(aluno):
    return aluno['media'] >= 7.0

def soma_recursiva(numeros):
    if not numeros:
        return 0
    else:
        return numeros[0] + soma_recursiva(numeros[1:])


def main():

    print("--- Processamento Funcional de Dados de Alunos ---")

    alunos_com_media = list(map(calcular_media, alunos_dados))
    print(f"\nAlunos com médias calculadas: {alunos_com_media}")

    alunos_aprovados = list(filter(foi_aprovado, alunos_com_media))
    print(f"\nAlunos aprovados (média >= 7.0): {alunos_aprovados}")

    medias_dos_aprovados = list(map(lambda aluno: aluno['media'], alunos_aprovados))
    print(f"\nLista de médias dos aprovados: {medias_dos_aprovados}")
    
    if not medias_dos_aprovados:
        media_final = 0
        print("\nNenhum aluno foi aprovado.")
    else:
        soma_das_medias = soma_recursiva(medias_dos_aprovados)
        media_final = soma_das_medias / len(medias_dos_aprovados)
        print(f"\nSoma das médias (calculada com recursão): {soma_das_medias:.2f}")

    print("-" * 20)
    print(f"Resultado Final: A média dos alunos aprovados é {media_final:.2f}")
    print("-" * 20)


if __name__ == "__main__":
    main()