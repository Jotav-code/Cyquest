import os
from pathlib import Path
from criptografia import descriptografar_arquivo

def recuperar_arquivos():
    diretorio_alvo = os.path.abspath("./laboratorio_teste")

    # carregar chave salva durante o teste
    with open("chave_resgate.key", "rb") as key_file:
        chave_mestra = key_file.read()

    print("[*] Iniciando recuperação...")

    for root, dirs, files in os.walk(diretorio_alvo):
        for file in files:
            if file.endswith(".cyquest"):
                caminho = Path(root) / file
                print(f"[*] Recuperando: {file}")
                descriptografar_arquivo(str(caminho), chave_mestra)

    print("[+] Recuperação finalizada!")

if __name__ == "__main__":
    recuperar_arquivos()