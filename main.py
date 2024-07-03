def palindrome_check(word):
    """
    Checks if passed argument is a palindrome
    Arguments:
    str word
    """
    for i in range(0,len(word)//2):
        if word[i] != word[-i-1]:
            return False
    else:
        return True    

words = [
    "potop",
    "obiady",
    "Kobyła ma mały bok",
    "ilu beczy z cebuli?"
    ]

for word in words:
    print(f"Is {word} a palindrome? {palindrome_check(word)}")