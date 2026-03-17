import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from pathlib import Path
from cryptography.fernet import Fernet
import aes

# with é um protetor, meio que impede que os dados sejam comrropidos
# with open('texto.txt','r') as arquivo:
#   conteudo = arquivo.read();
# print(conteudo);
# caminho = Path('texto.cyquest');
# caminho_novo = caminho.with_suffix('.cyquest');
# caminho.rename(caminho_novo);

# with caminho.open() as f:
#   texto = f.read();

# print(texto);

key = os.urandom(32);
# print(f"chave gerada {key}");
iv = os.urandom(16);
# print(f"iv gerada {iv}");

# usamos o algorithms.AES para definir que criptografia estamos utilizando, o modes.CBC significa o modo que meu algoritmo vai implementar a criptografia, CBC(Cipher Block Chaining) 
cipher = Cipher(algorithms.AES(key), modes.CBC(iv));
# encryptor "liga" a função para criptografar
encryptor = cipher.encryptor();

ct = encryptor.update(b"a secret message") + encryptor.finalize()
print(f"criptografado {ct}");
decryptor = cipher.decryptor();
mensagem_limpa = decryptor.update(ct) + decryptor.finalize();
b'a secret message'
print(f"Descriptografado {mensagem_limpa}");
