if os.path.exists(caminho_saida):
    print(f"AVISO: O arquivo '{caminho_saida}' já existe. Sobrescrever? (s/n)")
    if input().lower() != 's':
        print("Cancelado pelo usuário.")
        return
