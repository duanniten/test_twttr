def main():
    text = input("Input: ")
    
    new_text = creat_text(text)
    
    print("Output:", new_text)

def shorten(word: str):
    word = str(word)
    vowels = [
            'A', 'a',
            'E', 'e',
            'I', 'i',
            'O', 'o', 
            'U', 'u'
            ]
    new_word = ""
    for lether in word:
        if lether not in vowels:
            new_word += lether
    return new_word

def creat_text(text: str): 
    text = text.split(sep = ' ')
    new_text = ''
    for word in text:
        new_text += f'{shorten(word)} '
    return new_text[:-1]

if __name__ == '__main__':
    main()