import string
from collections import Counter

def analisar_texto(texto):
    """
    Analisa o texto fornecido e calcula a contagem de palavras, a frequência de palavras
    e a frequência de letras.

    Parameters
    ----------
    texto : str
        Texto a ser analisado

    Returns
    -------
    tuple
        Contagem de palavras, frequência de palavras e frequência de letras
    """

    #Remove a pontuação do texto
    tratamento = str.maketrans('', '', string.punctuation)
    texto_tratado = texto.translate(tratamento)

    palavras = texto_tratado.split()
    contagem_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)

    #Converte o texto para minuscula e conta a frequência das letras
    frequencia_letras = Counter(texto_tratado.lower())
    return contagem_palavras, frequencia_palavras, frequencia_letras