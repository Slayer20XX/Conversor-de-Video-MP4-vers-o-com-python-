from moviepy.editor import VideoFileClip
import sys
import os

def converter_para_mp4(caminho_entrada):
    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_entrada):
        print(f"Erro: Arquivo '{caminho_entrada}' não encontrado.")
        return

    # Extrai nome do arquivo e diretório
    diretorio = os.path.dirname(caminho_entrada)
    nome_base = os.path.splitext(os.path.basename(caminho_entrada))[0]
    
    # Define o caminho de saída (mesmo nome, mas .mp4)
    caminho_saida = os.path.join(diretorio, f"{nome_base}.mp4")

    print(f"Convertendo '{caminho_entrada}' para '{caminho_saida}'...")

    try:
        # Carrega o vídeo
        with VideoFileClip(caminho_entrada) as video:
            # Exporta como MP4 usando codec H.264 (compatível com quase tudo)
            video.write_videofile(
                caminho_saida,
                codec='libx264',           # Codec de vídeo
                audio_codec='aac',         # Codec de áudio (padrão para MP4)
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                preset='medium',           # Qualidade e velocidade (slow = melhor qualidade)
                threads=4                  # Usa múltiplas threads
            )
        print(f"✅ Conversão concluída: {caminho_saida}")
    except Exception as e:
        print(f"❌ Erro durante a conversão: {e}")

# --- Execução principal ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python conversor.py <caminho_do_arquivo>")
        print("Exemplo: python conversor.py video.avi")
    else:
        arquivo_entrada = sys.argv[1]
        converter_para_mp4(arquivo_entrada)
        
