import sys
def num_words(book):
    words_list = book.split()
    total = len(words_list)
    return total

def char_count(book):
    counts = {}
    for char in book.lower():
        if char not in [' ', '\n']:  # Skip spaces and newlines
            if char in counts:
                counts[char] += 1 
            else:
                counts[char] = 1
    return counts

def report(book):
    char_dict = char_count(book)
    number_of_words = num_words(book)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {sys.argv}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted(char_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: {value}")
    print("============= END ===============")