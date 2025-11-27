# Verificar se uma palavra é palíndromo:
def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]
