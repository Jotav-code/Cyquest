from pathlib import Path
import os

# print(f"{os.listdir('./arquivos_para_teste')}");

def lsitar_arquivos(caminho):
  try:
    p = Path(caminho)
    if not p.exists:
      raise print(f"esse {caminho} não foi encontrado")
    return [f.name for f in p.iterdir() if f.is_file()]
  except Exception as e:
    print(f"{e}")
    return []

caminho = "./arquivos_para_teste"
lista = lsitar_arquivos(caminho)

for arquivo in lista:
  print(arquivo);
