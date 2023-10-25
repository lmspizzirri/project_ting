from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    txt = txt_importer(path_file)

    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt
    }

    for each in range(len(instance)):
        if instance.search(each)["nome_do_arquivo"] == path_file:
            return
    instance.enqueue(dict)

    return sys.stdout.write(str(dict))


def remove(instance):
    if len(instance) > 0:
        item = instance.dequeue()
        return sys.stdout.write(
        f'Arquivo {item["nome_do_arquivo"]} removido com sucesso\n'
        )
    else:
        return sys.stdout.write('Não há elementos\n')


def file_metadata(instance, position):
    try:
        response = instance.search(position)
        return sys.stdout.write(str(response))
    except IndexError:
        sys.stderr.write("Posição inválida")
