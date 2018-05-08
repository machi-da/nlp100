import json
import gzip
import re
import requests
'''
wikipediaのマークアップ記法
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
'''


def knock20(gz_file_name, json_file_name):
    with gzip.open(gz_file_name, 'rb')as f:
        for article in f:
            # bytes型からstr型へデコード
            article = article.decode('utf-8')
            # loadsでstr型->json型へ変換できる
            article = json.loads(article)
            if article['title'] == 'イギリス':
                print(article['text'])
                # 21以降で使うためイギリスの記事を保存しておく
                with open(json_file_name, 'w')as json_f:
                    json.dump(article, json_f, ensure_ascii=False, indent=2)
                return


def knock21(file_name):
    data = load_json(file_name)
    text = data['text'].split('\n')
    pattern = re.compile(r'\[\[Category:(.*)\]\]')
    for t in text:
        m = re.match(pattern, t)
        if m:
            print(m.group())


def knock22(file_name):
    data = load_json(file_name)
    text = data['text'].split('\n')
    pattern = re.compile(r'\[\[Category:(.*)\]\]')
    for t in text:
        m = re.match(pattern, t)
        if m:
            print(m.group(1))


def knock23(file_name):
    data = load_json(file_name)
    text = data['text'].split('\n')
    pattern = re.compile(r'(==+)\s*(.*?)\s*(==+)')
    for t in text:
        m = re.match(pattern, t)
        if m:
            print('{}: {}'.format(m.group(2), len(m.group(1))))


def knock24(file_name):
    data = load_json(file_name)
    text = data['text'].split('\n')
    pattern = re.compile(r'(File|ファイル):(.*?)\|')
    for t in text:
        m = re.search(pattern, t)
        if m:
            print(m.group(2))


def knock25(file_name):
    dic = {}
    data = load_json(file_name)
    text = data['text']
    # DOTALLで改行も含めてマッチング
    info_text = re.search(r'\{\{基礎情報 国\n(.*?)\n\}\}\n', text, re.DOTALL).group(1).split('\n')
    pattern = re.compile(r'\|(.*?) = (.*?)$')
    for t in info_text:
        m = re.match(pattern, t)
        if m:
            dic[m.group(1)] = m.group(2)

    # 確認用
    for k, v in sorted(dic.items()):
        print('{}: {}'.format(k, v))


def knock26_27_28(file_name):
    dic = {}
    data = load_json(file_name)
    text = data['text']
    # DOTALLで改行も含めてマッチング
    info_text = re.search(r'\{\{基礎情報 国\n(.*?)\n\}\}\n', text, re.DOTALL).group(1).split('\n')
    pattern = re.compile(r'\|(.*?) = (.*?)$')

    def remove_markup(s):
        remove_symbol = [
            # knock26
            r"'{2,5}",
            # knock27
            r'\[\[',
            r'\]\]',
            # knock28
            r'<ref>.*?</ref>',
            r'<ref name=.*?(</ref>|/>)',
            r'<ref>',
            r'<br\s*/>'
        ]
        for r in remove_symbol:
            s = re.sub(r, '', s)
        return s

    for t in info_text:
        m = re.match(pattern, t)
        if m:
            dic[m.group(1)] = remove_markup(m.group(2))

    # 確認用
    for k, v in sorted(dic.items()):
        print('{}: {}'.format(k, v))


def knock29(file_name):
    data = load_json(file_name)
    text = data['text']
    # DOTALLで改行も含めてマッチング
    info_text = re.search(r'\{\{基礎情報 国\n(.*?)\n\}\}\n', text, re.DOTALL).group(1).split('\n')
    pattern = re.compile(r'\|国旗画像 = (.*?)$')
    image_url = None
    for t in info_text:
        m = re.match(pattern, t)
        if m:
            image_url = m.group(1)
            break

    api_url = 'http://ja.wikipedia.org/w/api.php?'
    param = {
        'format': 'json',
        'action': 'query',
        'prop': 'imageinfo',
        'titles': 'File:' + image_url,
        'iiprop': 'url'
    }
    res = requests.get(api_url, param).json()
    url = res['query']['pages']['-1']['imageinfo'][0]['url']
    print(url)


def load_json(file_name):
    with open(file_name, 'r')as f:
        data = json.load(f)
    return data


def maint():
    gz_file_name = 'jawiki-country.json.gz'
    json_file_name = 'uk.json'

    # 実行しないものは適宜コメント化
    knock20(gz_file_name, json_file_name)
    knock21(json_file_name)
    knock22(json_file_name)
    knock23(json_file_name)
    knock24(json_file_name)
    knock25(json_file_name)
    knock26_27_28(json_file_name)
    knock29(json_file_name)


if __name__ == '__main__':
    maint()