b = input('Podaj palindrom : ')

def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ","")
    """
    sprawdza czy podane słowo to palindrom
    zwraca wartosc false jesli nie, true jesli tak
    """
    return word == word[::-1]
    
print(is_palindrome(b))






