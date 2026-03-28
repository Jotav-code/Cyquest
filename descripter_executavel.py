#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
from criptografia import descriptografar_arquivo

def main():
    diretorio_padrao = os.path.join(os.path.expanduser("~"), "Documents", "laboratorio_teste")

    parser = argparse.ArgumentParser(description="Decrypter - Descriptografa arquivos .cyquest")
    parser.add_argument("diretorio", nargs="?", default=diretorio_padrao,
                        help="Diretório onde estão os arquivos criptografados (padrão: ~/Documents/laboratorio_teste)")
    parser.add_argument("--keyfile", default=None,
                        help="Arquivo com a chave AES-256 (padrão: busca chave_resgate.key dentro do diretório alvo)")
    args = parser.parse_args()

    diretorio_alvo = os.path.abspath(args.diretorio)
    if not os.path.exists(diretorio_alvo):
        print(f"[-] Diretório não encontrado: {diretorio_alvo}")
        sys.exit(1)

    
    keyfile = args.keyfile if args.keyfile else os.path.join(diretorio_alvo, "chave_resgate.key")

    if not os.path.exists(keyfile):
        print(f"[-] Arquivo de chave não encontrado: {keyfile}")
        sys.exit(1)

    print("\n===== CYQUEST DECRYPTER =====\n")

    
    with open(keyfile, "rb") as key_file:
        chave_mestra = key_file.read()
    print(f"[+] Chave carregada de: {keyfile}")

    
    arquivos_cyquest = []
    for root, dirs, files in os.walk(diretorio_alvo):
        for file in files:
            if file.endswith(".cyquest"):
                arquivos_cyquest.append(Path(root) / file)

    if not arquivos_cyquest:
        print("[!] Nenhum arquivo .cyquest encontrado.")
        sys.exit(0)

    print(f"[*] Encontrados {len(arquivos_cyquest)} arquivos criptografados.")
    sucessos = 0
    erros = 0

    for caminho in arquivos_cyquest:
        print(f"[*] Descriptografando: {caminho.name}")
        try:
            descriptografar_arquivo(str(caminho), chave_mestra)
            sucessos += 1
        except Exception as e:
            print(f"[ERRO] {caminho.name}: {e}")
            erros += 1

    print("\n" + "="*40)
    print(f"Total arquivos processados: {len(arquivos_cyquest)}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print("[+] Recuperação finalizada!")

if __name__ == "__main__":
    main()