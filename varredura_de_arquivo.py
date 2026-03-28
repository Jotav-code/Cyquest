import os
from pathlib import Path
from queue import Queue
import threading

# Dicionário que define categorias de arquivos por extensão
EXTENSOES = {
    "fotos": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp",
        ".tiff", ".tif", ".svg", ".heic", ".raw"
    },
    "videos": {
        ".mp4", ".avi", ".mov", ".mkv", ".wmv",
        ".flv", ".webm", ".mpeg", ".mpg", ".3gp"
    },
    "documentos": {
        ".pdf", ".doc", ".docx", ".txt",
        ".xls", ".xlsx", ".ppt", ".pptx",
        ".odt", ".ods", ".csv", ".rtf"
    },
    "audio": {
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"
    },
    "compactados": {
        ".zip", ".rar", ".7z", ".tar", ".gz"
    },
    "codigo": {
        ".py", ".js", ".java", ".c", ".cpp", ".cs",
        ".html", ".css", ".php", ".json", ".xml"
    }
}


def escanear_diretorio(caminho_base, num_threads=8):

    caminho = Path(caminho_base)

    # Verifica se o caminho existe
    if not caminho.exists():
        raise ValueError(f"Diretório não encontrado: {caminho_base}")

    # Verifica se é realmente um diretório
    if not caminho.is_dir():
        raise ValueError(f"O caminho não é um diretório: {caminho_base}")

    # Inicializa o dicionário de resultados (listas vazias por categoria)
    resultados = {categoria: [] for categoria in EXTENSOES}

    # Fila de pastas a serem processadas (estrutura para controle da recursão)
    fila = Queue()

    # Coloca o diretório inicial na fila
    fila.put(caminho)

    # Lock para evitar conflitos entre threads ao escrever nos resultados
    lock = threading.Lock()

    def trabalhador():

        while True:

            # Pega uma pasta da fila
            pasta = fila.get()

            # Se receber None, significa que deve encerrar a thread
            if pasta is None:
                break

            try:
                # Abre a pasta e lista seus itens
                with os.scandir(pasta) as itens:

                    for item in itens:

                        try:
                            # Se for diretório, adiciona na fila (recursão)
                            if item.is_dir(follow_symlinks=False):
                                fila.put(item.path)

                            # Se for arquivo, classifica por extensão
                            elif item.is_file(follow_symlinks=False):

                                # Obtém a extensão do arquivo
                                ext = Path(item.name).suffix.lower()

                                # Verifica a qual categoria pertence
                                for categoria, extensoes in EXTENSOES.items():
                                    if ext in extensoes:

                                        # Usa lock para evitar conflito entre threads
                                        with lock:
                                            resultados[categoria].append(Path(item.path))

                                        break  # para após encontrar a categoria

                        except PermissionError:
                            # Ignora arquivos/pastas sem permissão
                            continue

            except PermissionError:
                # Ignora pastas inteiras sem permissão
                pass

            # Indica que a tarefa da fila foi concluída
            fila.task_done()

    # Lista que armazenará as threads
    threads = []

    # Cria e inicia as threads
    for _ in range(num_threads):
        t = threading.Thread(target=trabalhador)
        t.start()
        threads.append(t)

    # Aguarda até que toda a fila seja processada
    fila.join()

    # Envia sinal de parada para todas as threads
    for _ in threads:
        fila.put(None)

    # Aguarda todas as threads terminarem
    for t in threads:
        t.join()

    # Retorna o resultado final com os arquivos classificados
    return resultados