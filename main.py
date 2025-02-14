def palindrome_check(word):
    """
    Checks if passed argument is a palindrome,
    regardless of capitalisation, spaces or special characters
    Arguments:
    str word
    """
    word = "".join(char.lower() for char in word if char.isalpha())
    for i in range(0,len(word)//2):
        if word[i] != word[-i-1]:
            return False
    else:
        return True    

words = [
    "potop",
    "obiady",
    "Anna",
    "kobyła ma mały bok",
    "ilu beczy z cebuli?"
    ]

for word in words:
    print(f'Is "{word}" a palindrome? {palindrome_check(word)}')