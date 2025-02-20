def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_char = get_num_char(text)
    #num_char_list = [{char: num_char[char]} for char in num_char if char.isalpha()]
    for char in num_char:
        if char.isalpha():
            print(f"The '{char}' character was found {num_char[char]} times")
    #num_char_list.sort(reverse=True, key=lambda item: item.values())
        

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_char(text):
    result = {}
    for char in list(text.lower()):
        if char in result.keys():
            result[char] += 1
        else:
            result[char] = 1
    return result



main()
