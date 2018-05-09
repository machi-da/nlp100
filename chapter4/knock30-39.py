import MeCab
from collections import Counter
import matplotlib.pyplot as plt


def knock30(file_name):
    res = []
    sentence = []
    text = load_file(file_name)
    for t in text:
        t = t.strip()
        if t != 'EOS':
            surface, feature = t.split('\t')
            feature = feature.split(',')
            dic = {
                'surface': surface,
                'base': feature[6],
                'pos': feature[0],
                'pos1': feature[1]
            }
            sentence.append(dic)
        else:
            res.append(sentence)
            sentence = []
    # 確認用
    # for sentence in sentences[:3]:
    #     print(sentence)
    return res


def knock31(file_name):
    data = knock30(file_name)
    res = [word['surface'] for sentence in data for word in sentence if word['pos'] == '動詞']
    '''以下と同じ処理をしてる
    for sentence in data:
        for word in sentence:
            if word['pos'] == '動詞':
                res.append(word['surface'])
    '''
    print(res)
    print('Total num: {}, Unique num: {}'.format(len(res), len(set(res))))


def knock32(file_name):
    data = knock30(file_name)
    res = [word['base'] for sentence in data for word in sentence if word['pos'] == '動詞']
    print(res)
    print('Total num: {}, Unique num: {}'.format(len(res), len(set(res))))


def knock33(file_name):
    data = knock30(file_name)
    res = [word['surface'] for sentence in data for word in sentence if word['pos1'] == 'サ変接続']
    print(res)
    print('Total num: {}, Unique num: {}'.format(len(res), len(set(res))))


def knock34(file_name):
    res = []
    data = knock30(file_name)
    for sentence in data:
        if len(sentence) < 3:
            continue
        for i, word in enumerate(sentence):
            try:
                if word['surface'] == 'の':
                    pre = sentence[i-1]
                    post = sentence[i+1]
                    if pre['pos'] == '名詞' and post['pos'] == '名詞':
                        res.append(pre['surface'] + 'の' + post['surface'])
            except IndexError:
                pass
    print(res)
    print('Total num: {}, Unique num: {}'.format(len(res), len(set(res))))


def knock35(file_name):
    res = []
    nouns = []
    data = knock30(file_name)
    for sentence in data:
        for word in sentence:
            if word['pos'] == '名詞':
                nouns.append(word['surface'])
            else:
                if len(nouns) > 1:
                    res.append(''.join(nouns))
                nouns = []
    print(res)
    print('Total num: {}, Unique num: {}'.format(len(res), len(set(res))))


def knock36(file_name):
    data = knock30(file_name)
    counter = Counter([word['surface'] for sentence in data for word in sentence])
    # 頻度の上位n件を表示
    n = 1000
    for k, v in counter.most_common(n):
        print('{}: {}'.format(k, v))


def knock37(file_name):
    data = knock30(file_name)
    counter = Counter([word['surface'] for sentence in data for word in sentence])
    label = []
    freq = []
    for k, v in counter.most_common(10):
        label.append(k)
        freq.append(v)

    plt.bar(range(len(label)), freq, tick_label=label)
    plt.title('High frequency word Top 10')
    plt.xlabel('word')
    plt.ylabel('appearance frequency')
    plt.savefig('knock37.png')
    plt.show()


def knock38(file_name):
    data = knock30(file_name)
    counter = Counter([word['surface'] for sentence in data for word in sentence])
    freq = [v for k, v in counter.most_common()]

    plt.hist(freq, bins=200, log=True)
    plt.title('Word appearance frequency histogram')
    plt.xlabel('appearance frequency')
    plt.ylabel('# of words')
    plt.savefig('knock38.png')
    plt.show()


def knock39(file_name):
    data = knock30(file_name)
    counter = Counter([word['surface'] for sentence in data for word in sentence])
    freq = [v for k, v in counter.most_common()]

    plt.xscale('log')
    plt.yscale('log')
    plt.plot(freq, range(len(freq)))
    plt.title('Zipf')
    plt.xlabel('rank')
    plt.ylabel('appearance frequency')
    plt.savefig('knock39.png')
    plt.show()


def load_file(file_name):
    with open(file_name, 'r')as f:
        data = f.readlines()
    return data


def preprocessing(text):
    res = []
    for t in text:
        t = t.strip()
        if t == '' or t == '一' or t == '十一':
            continue
        t = t.replace('　', '')
        res.append(t)
    return res


def make_mecab_file(file_name, output_file_name):
    res = []
    m = MeCab.Tagger()
    text = load_file(file_name)
    text = preprocessing(text)
    for t in text:
        t = m.parse(t)
        res.append(t)
    with open(output_file_name, 'w')as f:
        [f.write(r) for r in res]


def main():
    file_name = '../neko.txt'
    mecab_file_name = 'neko.txt.mecab'

    # neko.txt.mecab作成
    # make_mecab_file(file_name, mecab_file_name)

    # 実行しないものは適宜コメント化
    knock30(mecab_file_name)
    knock31(mecab_file_name)
    knock32(mecab_file_name)
    knock33(mecab_file_name)
    knock34(mecab_file_name)
    knock35(mecab_file_name)
    knock36(mecab_file_name)
    knock37(mecab_file_name)
    knock38(mecab_file_name)
    knock39(mecab_file_name)


if __name__ == '__main__':
    main()