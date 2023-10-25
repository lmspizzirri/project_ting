def exists_word(word, instance):
    result = []
    for file in range(len(instance)):
        file = instance.search(file)
        occurrences = [
            {"linha": line_number}
            for line_number, line in enumerate(
                file["linhas_do_arquivo"], 1
            )
            if word.lower()
            in line.lower()
        ]

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    result = []
    word = word.lower()

    for file in instance.queue:
        linhas = file["linhas_do_arquivo"]
        occur = []

        for i, linhas in enumerate(linhas):
            line = linhas.lower()
            if word in line:
                occur.append({
                    "linha": i + 1,
                    "conteudo": linhas
                              })

        if len(occur) >= 1:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occur
            })

    return result