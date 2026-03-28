import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def criptografar_arquivo(caminho_arquivo, chave_aes_256):
    tamanho_chunk = 64 * 1024
    caminho_saida = caminho_arquivo + ".cyquest"

    iv = os.urandom(16)

    cipher = Cipher(
        algorithms.AES(chave_aes_256),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    try:
        with open(caminho_arquivo, "rb") as arquivo_in, open(caminho_saida, "wb") as arquivo_out:
            arquivo_out.write(iv)

            while True:
                chunk = arquivo_in.read(tamanho_chunk)
                if len(chunk) == 0:
                    break

                if len(chunk) < tamanho_chunk:
                    chunk = padder.update(chunk) + padder.finalize()
                    dados = encryptor.update(chunk) + encryptor.finalize()
                    arquivo_out.write(dados)
                    break
                else:
                    arquivo_out.write(encryptor.update(chunk))

        print(f"[+] Arquivo criptografado: {caminho_saida}")

        
        os.remove(caminho_arquivo)
        print(f"[!] Original apagado: {caminho_arquivo}")

        return caminho_saida

    except Exception as e:
        print(f"[-] Erro ao criptografar {caminho_arquivo}: {e}")
       
        if os.path.exists(caminho_saida):
            os.remove(caminho_saida)
        return None



def descriptografar_arquivo(caminho_arquivo_criptografado, chave_aes_256):
    tamanho_chunk = 64 * 1024
    caminho_saida = caminho_arquivo_criptografado.replace(".cyquest", "")

    try:
        with open(caminho_arquivo_criptografado, "rb") as arquivo_in:
            iv = arquivo_in.read(16)

            cipher = Cipher(
                algorithms.AES(chave_aes_256),
                modes.CBC(iv),
                backend=default_backend()
            )
            decryptor = cipher.decryptor()
            unpadder = padding.PKCS7(128).unpadder()

            with open(caminho_saida, "wb") as arquivo_out:
                while True:
                    chunk = arquivo_in.read(tamanho_chunk)
                    if len(chunk) == 0:
                        break

                    dados = decryptor.update(chunk)

                    if len(chunk) < tamanho_chunk:
                        dados += decryptor.finalize()
                        dados = unpadder.update(dados) + unpadder.finalize()
                        arquivo_out.write(dados)
                        break
                    else:
                        arquivo_out.write(dados)

        print(f"[+] Arquivo recuperado: {caminho_saida}")

        
        os.remove(caminho_arquivo_criptografado)
        print(f"[!] Arquivo criptografado apagado: {caminho_arquivo_criptografado}")

        return caminho_saida

    except Exception as e:
        print(f"[-] Erro ao descriptografar {caminho_arquivo_criptografado}: {e}")
       
        if os.path.exists(caminho_saida):
            os.remove(caminho_saida)
        return None