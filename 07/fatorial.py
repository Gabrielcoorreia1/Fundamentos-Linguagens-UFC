def fatorial(n):
    
    print(f"Calculando o fatorial de {n}...")
    
    if n == 0:
        print("Caso base atingido (n=0), retornando 1.")
        return 1
    else:
        resultado_parcial = fatorial(n - 1)
        resultado_final = n * resultado_parcial
        print(f"Retornando de fatorial({n}): {resultado_final}")
        return resultado_final

def main():

    numero_para_calcular = 3
    print(f"--- Iniciando cálculo do fatorial de {numero_para_calcular} ---")
    resultado = fatorial(numero_para_calcular)
    print("--- Fim do cálculo ---")
    print(f"O fatorial de {numero_para_calcular} é: {resultado}")

if __name__ == "__main__":
    main()