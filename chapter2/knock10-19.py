from collections import Counter


def knock10(file_name):
    file_obj = load_file(file_name)
    print('lines: {}'.format(len(file_obj)))


def knock11(file_name):
    file_obj = load_file(file_name)
    for line in file_obj:
        print(line.replace('\t', ' '))


def knock12(file_name):
    file_obj = load_file(file_name)
    col1, col2 = [], []
    for line in file_obj:
        line = line.split('\t')
        col1.append(line[0])
        col2.append(line[1])

    with open('col1.txt', 'w')as f:
        [f.write(c + '\n') for c in col1]
    with open('col2.txt', 'w')as f:
        [f.write(c + '\n') for c in col2]
    print('Create col1.txt, col2.txt')


def knock13():
    with open('col1.txt', 'r')as f1, open('col2.txt', 'r')as f2:
        res = []
        for line1, line2 in zip(f1, f2):
            res.append(line1.strip() + '\t' + line2.strip() + '\n')

    with open('merge.txt', 'w')as f:
        [f.write(r) for r in res]
    print('Create merge.txt')


def knock14(file_name, n):
    file_obj = load_file(file_name)
    for i in range(n):
        print(file_obj[i].strip())


def knock15(file_name, n):
    file_obj = load_file(file_name)
    for i in range(1, n+1)[::-1]:
        print(file_obj[-i].strip())


def knock16(file_name, n):
    file_obj = load_file(file_name)
    assert n <= len(file_obj), '分割数がファイルサイズを超えます'
    res = []
    mod = len(file_obj) % n
    if mod == 0:
        unit = len(file_obj) // n
        for i in range(n):
            res.append(file_obj[i * unit: (i + 1) * unit])
    else:
        unit = len(file_obj) // n + 1
        for i in range(n-1):
            res.append(file_obj[i * unit: (i + 1) * unit])
        res.append(file_obj[-mod:])

    for i, r in enumerate(res):
        with open('{}_{}'.format(file_name, i), 'w')as f:
            [f.write(rr) for rr in r]


def knock17(file_name):
    file_obj = load_file(file_name)
    res = set(map(lambda x: x.split('\t')[0], file_obj))
    print(res)
    print('Unique string: {}'.format(len(res)))


def knock18(file_name):
    file_obj = load_file(file_name)
    file_obj = list(map(lambda x: x.strip().split('\t'), file_obj))
    for line in sorted(file_obj, key=lambda x: x[2], reverse=True):
        print('\t'.join(line))


def knock19(file_name):
    file_ojb = load_file(file_name)
    col1 = list(map(lambda x: x.split('\t')[0], file_ojb))
    res = Counter(col1)
    for k, v in res.most_common():
        print('{}: {}'.format(k, v))


def load_file(file_name):
    with open(file_name, 'r')as f:
        data = f.readlines()
    return data


def main():
    file_name = '../hightemp.txt'
    n = 5

    # 実行しないものは適宜コメント化
    knock10(file_name)
    knock11(file_name)
    knock12(file_name)
    knock13()
    knock14(file_name, n)
    knock15(file_name, n)
    knock16(file_name, n)
    knock17(file_name)
    knock18(file_name)
    knock19(file_name)


if __name__ == '__main__':
    main()