import threading
import time
import random

def simular_download(nome_arquivo):
    
    tempo_espera = random.uniform(1, 4)  
    print(f"Iniciando download de '{nome_arquivo}'... (vai levar {tempo_espera:.2f}s)")
    
    time.sleep(tempo_espera)
    
    print(f"[OK] Download de '{nome_arquivo}' concluído!")


def main():

    arquivos_para_baixar = [
        "relatorio_anual.pdf",
        "video_tutorial.mp4",
        "dataset_clientes.csv",
        "apresentacao.pptx",
        "imagem_alta_resolucao.jpg"
    ]
    
    lista_de_threads = []
    
    print("--- Iniciando downloads concorrentes com Threads ---")
    tempo_inicial = time.time()

    for arquivo in arquivos_para_baixar:
        thread = threading.Thread(target=simular_download, args=(arquivo,))
        lista_de_threads.append(thread)
        thread.start()

    for thread in lista_de_threads:
        thread.join()
        
    tempo_final = time.time()
    
    print("\n--- Todos os downloads foram finalizados. ---")
    print(f"Tempo total da operação: {tempo_final - tempo_inicial:.2f} segundos.")


if __name__ == "__main__":
    main()