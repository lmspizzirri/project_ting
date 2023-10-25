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
    
    instance.enqueue(dic)

    return sys.stdout.write(str(dic))

def remove(instance):
    if len(instance) > 0:
        item = instance.dequeue()['nome_do_arquivo']
        return sys.stdout.write(f'Arquivo {item} removido com sucesso\n')
    else:
        return sys.stdout.write('Não há elementos\n')


def file_metadata(instance, position):
    try:
        response = instance.read_instance()[position]
        sys.stdout.write(str(response))
    except IndexError:
        sys.stderr.write("Posição inválida")
