def int_func(word: str):
    return word.capitalize()

while True:
    words = input('Typed words devided by space (empty - exit): ')
    if words == '':
        break
    words = map(int_func, words.lower().split())
    print(' '.join(list(words)))