import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, 'r') as file:
            archive = file.read().split('\n')
            return archive
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
