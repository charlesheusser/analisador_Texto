from funcion import analisar_texto

texto = "Olá mundo! Este é um teste, Olá novamente"
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)
print(f'Contagem de Palavras: {contagem_palavras}')
print(f'Frequência de Palavras: {frequencia_letras}')
print(f'Frequência de letras: {frequencia_letras}')
