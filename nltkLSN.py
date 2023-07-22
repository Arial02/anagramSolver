import nltk
from nltk.corpus import words


def get_depth(l):
    return 1 + max(get_depth(item) for item in l) if type(l) == list else 0


def smooth(l):
    res = []
    for lst in l:
        if type(lst) == list and get_depth(lst) > 0:
            for el in lst:
                res.append(el)
        else:
            res.append(lst)
    return res


def allCombs(src, res=''):
    if len(src) == 1:
        return res + src
    return smooth([allCombs(src[:i] + src[i + 1:], res + src[i]) for i in range(len(src))])


def main():
    print('Input letters: ')
    cmd = input()

    is_found = False

    try:
        english_vocab = set(w.lower() for w in words.words())
    except LookupError:
        nltk.download('words')
        english_vocab = set(w.lower() for w in words.words())
    for el in allCombs(cmd):
        if el in english_vocab:
            print(el)
            if not is_found:
                is_found = True

    if not is_found:
        print('Can\'t find the word!')


if __name__ == '__main__':
    main()