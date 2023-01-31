def is_palindrome(word):
    temp = word.reverse()
    if temp == word:
        return True
    return False
