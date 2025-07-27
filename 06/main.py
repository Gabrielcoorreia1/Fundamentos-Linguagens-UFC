def tentar_modificar_numero(num):

    print(f"  > Dentro da função, o número recebido foi {num}. Será 99.")
    num = 99

def modificar_lista(lista_de_itens):

    print(f"  > Dentro da função, a lista recebida foi {lista_de_itens}.")
    lista_de_itens.append("item novo")
    print(f"  > A lista agora é {lista_de_itens}.")

def main():

    meu_numero = 5
    minha_lista = ["item 1", "item 2"]

    print("--- Teste com Tipo Imutável (int) ---")
    print(f"Número original antes: {meu_numero}")
    tentar_modificar_numero(meu_numero)
    print(f"Número original depois: {meu_numero}\n")

    print("--- Teste com Tipo Mutável (list) ---")
    print(f"Lista original antes: {minha_lista}")
    modificar_lista(minha_lista)
    print(f"Lista original depois: {minha_lista}")

if __name__ == "__main__":
    main()