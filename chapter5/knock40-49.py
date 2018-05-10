import pydot


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk:
    def __init__(self, morphs=[], dst=-1, srcs=[]):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def join_surface(self, remove_punctuation=True):
        surface = ''.join([m.surface for m in self.morphs])
        if remove_punctuation:
            surface = surface.replace('。', '').replace('、', '')
        return surface

    def include_pos(self, pos):
        return any([m.pos == pos for m in self.morphs])

    def include_pos1(self, pos1):
        return any([m.pos1 == pos1 for m in self.morphs])

    def match_pos(self, pos, position):
        return self.morphs[position].pos == pos

    def get_fist_match_pos_morph(self, pos, reverse=False):
        morphs = self.morphs[::-1] if reverse else self.morphs
        for m in morphs:
            if m.pos == pos:
                return m
        assert False, "No hit '{}' in {}".format(self.join_surface(), pos)

    def get_surface_index(self, surface):
        [m for m in self.morphs]
        return




def knock40(file_name):
    doc = []
    sentence = []
    text = load_file(file_name)
    for t in text:
        if t.startswith('*'):
            continue

        if t.startswith('EOS'):
            doc.append(sentence)
            sentence = []
        else:
            surface, features = t.split('\t')
            feature = features.split(',')
            morph = Morph(surface=t[0], base=feature[6], pos=feature[0], pos1=feature[1])
            sentence.append(morph)
    # 3文目を表示
    print(' '.join([word.surface for word in doc[2]]))


def knock41(file_name):
    doc = []
    sentence = []
    chunk = Chunk()
    text = load_file(file_name)
    for t in text:
        if t.startswith('*'):
            if len(chunk.morphs) > 0:
                sentence.append(chunk)
            dst = t.split(' ')[2]
            dst = int(dst[:-1])
            chunk = Chunk(morphs=[], dst=dst, srcs=[])
        elif t.startswith('EOS'):
            sentence.append(chunk)
            # srcsを入れる
            for i, s in enumerate(sentence):
                if s.dst != -1:
                    sentence[s.dst].srcs.append(i)
            doc.append(sentence)
            sentence = []
            chunk = Chunk()
        else:
            surface, features = t.split('\t')
            feature = features.split(',')
            morph = Morph(surface=surface, base=feature[6], pos=feature[0], pos1=feature[1])
            chunk.morphs.append(morph)
    # 8文目を表示
    # for i, c in enumerate(doc[7]):
    #     print('{}: {} {}'.format(i, c.dst, c.join_surface(remove_punctuation=False)))
    return doc


def knock42(file_name):
    doc = knock41(file_name)
    for sentence in doc:
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            print(chunk.join_surface() + '\t' + sentence[chunk.dst].join_surface())


def knock43(file_name):
    doc = knock41(file_name)
    for sentence in doc:
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            if chunk.include_pos('名詞') and sentence[chunk.dst].include_pos('動詞'):
                print(chunk.join_surface() + '\t' + sentence[chunk.dst].join_surface())


def knock44(file_name, n):
    doc = knock41(file_name)

    def graph(sentence):
        edges = []
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            direction = (chunk.join_surface(), sentence[chunk.dst].join_surface())
            edges.append(direction)
        g = pydot.graph_from_edges(edges, directed=True)
        g.write_png('knock44.png')

    graph(doc[n-1])


def knock45(file_name):
    res = []
    dic = {}
    doc = knock41(file_name)
    for sentence in doc:
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            if chunk.include_pos('助詞') and sentence[chunk.dst].include_pos('動詞'):
                particle = chunk.get_fist_match_pos_morph('助詞', reverse=True).surface
                verb = sentence[chunk.dst].get_fist_match_pos_morph('動詞').base
                if verb in dic:
                    dic[verb].append(particle)
                else:
                    dic[verb] = [particle]
        for k, v in dic.items():
            res.append('{}\t{}'.format(k, ' '.join(sorted(v))))
        dic = {}
    with open('knock45.txt', 'w')as f:
        [f.write(r + '\n') for r in res]


def knock46(file_name):
    dic = {}
    doc = knock41(file_name)
    for sentence in doc:
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            if chunk.include_pos('助詞') and sentence[chunk.dst].include_pos('動詞'):
                particle = chunk.get_fist_match_pos_morph('助詞', reverse=True).surface
                phrase = chunk.join_surface()
                verb = sentence[chunk.dst].get_fist_match_pos_morph('動詞').base
                if verb in dic:
                    dic[verb].append((particle, phrase))
                else:
                    dic[verb] = [(particle, phrase)]
        for k, v in dic.items():
            print('{}\t{}\t{}'.format(k, ' '.join([x[0] for x in sorted(v)]), ' '.join([x[1] for x in sorted(v)])))
        dic = {}


# def knock47(file_name):
#     doc = knock41(file_name)
#     for sentence in doc:
#         for chunk in sentence:
#             if chunk.include_pos1('サ変接続') and sentence:





def load_file(file_name):
    with open(file_name, 'r')as f:
        data = f.readlines()
    return data


def main():
    file_name = 'neko.txt.cabocha'
    # file_name = 'a'

    # 実行しないものは適宜コメント化
    # knock40(file_name)
    # knock41(file_name)
    # knock42(file_name)
    # knock43(file_name)
    # knock44(file_name, 1)
    # knock45(file_name)
    # knock46(file_name)
    # knock47(file_name)


if __name__ == '__main__':
    main()