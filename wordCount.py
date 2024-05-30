def word_count(text):
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Count the number of words
    num_words = len(words)
    return num_words

text = input("Enter the text: ")
count = word_count(text)
print(f"The number of words in the given text is: {count}")
