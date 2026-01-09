def find_largest(numbers):
    # Your code goes here
    dic_str= {}
    for i, nr in enumerate(numbers):
        str_len = len(nr)
        dic_str[i] = str_len
    
    find_largest = max(dic_str.values())

    return find_largest



# # This is how your code will be called.
# # Your answer should be the length of the longest string in the list
# # You can edit this code to try different testing cases.
test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]

result = find_largest(test_strings)

print(result)
