def palindrome_check(word):
    for i in range(0,len(word)):
        if word[i] != word[-i-1]:
            return False
    else:
        return True    

words = [
    "potop",
    "obiad"
    ]

for word in words:
    print(f"Is {word} a palindrome? {palindrome_check(word)}")