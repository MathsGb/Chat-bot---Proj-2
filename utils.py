import os, shutil

def deleta_arquivos(dir):
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def cria_diretorio(path):
    os.mkdir(path)
