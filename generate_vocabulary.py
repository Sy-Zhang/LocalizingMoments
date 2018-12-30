import re
import json

def word_tokenize(s):
    sent = s.lower()
    sent = re.sub('[^A-Za-z0-9\s]+',' ', sent)
    return sent.split()

if __name__ == '__main__':

    glove_dim = 300
    glove_path = '/localdisk/szhang83/Developer/LocalizingMoments/data/glove.6B.%dd.txt' % glove_dim
    glove_txt = open(glove_path).readlines()
    glove_txt = [g.strip() for g in glove_txt]
    glove_vector = [g.split(' ') for g in glove_txt]
    glove_words = [g[0] for g in glove_vector]

    txt_path = 'data/didemo_vocab_glove_complete.txt'
    vocab_file = open(txt_path, 'w')
    words = []
    for split in ['train', 'val', 'test']:
        anno_list = json.load(open('data/{}_data.json'.format(split)))

        for anno in anno_list:
            words.extend(word_tokenize(anno['description']))
    valid_words = list(filter(lambda w: w in glove_words, set(words)))
    vocab_file.write('\n'.join(set(valid_words)))


