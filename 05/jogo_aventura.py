import time

def iniciar_jogo():
    
    print("--- A Fuga do Quarto ---")
    print("Você acorda em um quarto mal iluminado. Sua única saída é uma porta de madeira.")
    print("Para sair, você precisa encontrar a chave.")
    print("Comandos possíveis: 'olhar mesa', 'pegar chave', 'abrir porta', 'desistir'")
    print("-" * 25)

    jogador_tem_a_chave = False
    mesa_revistada = False

    while True:
        time.sleep(1)
        acao = input("\nO que você faz? > ").lower()

        if acao == "olhar mesa":
            if not mesa_revistada:
                print("Você olha a mesa de carvalho. Em uma das gavetas, você encontra uma pequena chave de ferro.")
                mesa_revistada = True
            else:
                print("Você já revistou a mesa. Não há mais nada aqui.")

        elif acao == "pegar chave":
            if mesa_revistada and not jogador_tem_a_chave:
                print("Você pegou a chave. Ela parece ser a certa para a porta.")
                jogador_tem_a_chave = True
            elif jogador_tem_a_chave:
                print("Você já tem a chave!")
            else:
                print("Não há nenhuma chave à vista para pegar.")
        
        elif acao == "abrir porta":
            if jogador_tem_a_chave:
                print("\nVocê insere a chave na fechadura, gira... e a porta se abre!")
                print("Parabéns, você escapou!")
                break
            else:
                print("A porta está trancada. Você precisa de uma chave.")

        elif acao == "desistir":
            print("\nA persistência é uma virtude, mas não hoje. Fim de jogo.")
            break

        else:
            print("Comando não reconhecido. Tente 'olhar mesa', 'pegar chave', 'abrir porta' ou 'desistir'.")

if __name__ == "__main__":
    iniciar_jogo()