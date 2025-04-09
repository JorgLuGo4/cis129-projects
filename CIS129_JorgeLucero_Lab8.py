def is_palindrome(word): # you have to type: is_palindrome("word") in order to run the program correctly
    stack = []

    for letter in word:
        stack.append(letter)

    reversed_word = ""
    while stack:  
        reversed_word += stack.pop()

    # comparing the original word with the reversed
    if word == reversed_word:
        return True
    else:
        return False
