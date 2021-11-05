b = input('Podaj palindrom : ')

def is_palindrome(word):
    word = ''.join([word.lower() for x in word if word.isalpha()])
    """
    sprawdza czy podane słowo to palindrom
    zwraca wartosc false jesli nie, true jesli tak
    """
    return word == word[::-1]
    
print(is_palindrome(b))






