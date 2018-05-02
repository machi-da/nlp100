import random


def knock00():
    string = 'stressed'
    print('Input: {}'.format(string))

    res = string[::-1]
    print('Output: {}'.format(res))


def knock01():
    string = 'パタトクカシーー'
    print('Input: {}'.format(string))

    res = string[::2]
    print('Output: {}'.format(res))


def knock02():
    string1 = 'パトカー'
    string2 = 'タクシー'
    print('Input: {}, {}'.format(string1, string2))

    res = ''
    for s1, s2 in zip(string1, string2):
        res += s1 + s2
    print('Output: {}'.format(res))


def knock03():
    string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    print('Input: {}'.format(string))

    string = string.replace(',', '').replace('.', '')
    res = [len(word) for word in string.split(' ')]
    print('Output: {}'.format(res))


def knock04():
    string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. ' \
            'New Nations Might Also Sign Peace Security Clause. ' \
            'Arthur King Can.'
    print('Input: {}'.format(string))

    num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    res = {}
    for i, s in enumerate(string.split(' '), start=1):
        if i in num_list:
            res[s[0]] = i
        else:
            res[s[0:2]] = i
    print('Output: {}'.format(sorted(res.items(), key=lambda x: x[1])))


def word_ngram(string, n):
    res = []
    string = string.split(' ')
    for i in range(len(string) - n + 1):
        res.append(string[i:i+n])
    return res


def char_ngram(string, n):
    res = []
    string = string.replace(' ', '')
    for i in range(len(string) - n + 1):
        res.append(string[i:i+n])
    return res


def knock05():
    string = 'I am an NLPer'
    print('Input: {}'.format(string))
    print('word bigram: {}'.format(word_ngram(string, 2)))
    print('char bigram: {}'.format(char_ngram(string, 2)))


def knock06():
    string1 = 'paraparaparadise'
    string2 = 'paragraph'
    print('Input: {}, {}'.format(string1, string2))

    X = set(char_ngram(string1, 2))
    Y = set(char_ngram(string2, 2))
    print('X : {}'.format(X))
    print('Y : {}'.format(Y))

    print('和集合: {}'.format(X | Y))
    print('積集合: {}'.format(X & Y))
    print('差集合: {}'.format(X - Y))
    print("'se' is included in X -> {}".format('se' in X))
    print("'se' is included in Y -> {}".format('se' in Y))


def knock07():
    def template(x, y, z):
        return '{}時の{}は{}'.format(x, y, z)

    x = 12
    y = '気温'
    z = 22.4
    print('Input : x={}, y={}, z={}'.format(x, y, z))
    print('Output: {}'.format(template(x, y, z)))


def knock08():
    def cipher(string):
        res = ''
        for s in string:
            res += chr(219-ord(s)) if s.islower() else s
        return res

    string = 'Tom is cool GUY.'
    print('Input: {}'.format(string))
    code = cipher(string)
    decode = cipher(code)
    print('暗号化: {}'.format(code))
    print('復号化: {}'.format(decode))


def knock09():
    def typoglycemia(string):
        res = []
        for s in string.split(' '):
            if len(s) > 4:
                middle = list(s[1:-1])
                random.shuffle(middle)
                res.append(s[0] + ''.join(middle) + s[-1])
            else:
                res.append(s)
        return ' '.join(res)

    string = "I couldn't believe that I could actually understand " \
             "what I was reading : the phenomenal power of the human mind ."
    print('Input: {}'.format(string))
    print('Output: {}'.format(typoglycemia(string)))


def main():
    for i in range(10):
        func_name = 'knock0{}'.format(i)
        print(func_name)
        eval(func_name)()


if __name__ == '__main__':
    main()