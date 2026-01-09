import string


def is_palindrome(teststr):
    # Your code goes here.
    cleaned_str = ""
    for char in teststr:
        char = char.strip(string.punctuation)
        if char.isalpha() == True:
            char = char.lower()
            cleaned_str += char
    reversed_str = cleaned_str[::-1]
    if cleaned_str == reversed_str:
        return True
    
    return False
            
    
            
    

    
    
test_word = "Madam, I'm Adam."
# try using some of these other words:
# test_word = "RACE CAR!"
# test_word = "Hello, world"
# test_word = "Radar?"
# test_word = "A man, a plan, a canal Panama!"

result = is_palindrome(test_word)