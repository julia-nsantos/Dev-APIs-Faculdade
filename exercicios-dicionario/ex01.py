# O objetivo dessa atividade é fazer uma função contador, que recebe uma
# string e devolve uma contagem de palavras, na forma de um dicionário


def contador(texto):
    palavras = texto.split()
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem


d = contador("o doce mais doce")
print(d)
