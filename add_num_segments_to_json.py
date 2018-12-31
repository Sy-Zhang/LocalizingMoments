import re
import json

if __name__ == '__main__':

    for split in ['train', 'val', 'test']:
        didemo_anno_list = json.load(open('data/{}_data.json'.format(split)))
        tempo_anno_list = json.load(open('data/tempoHL+didemo_{}.json'.format(split)))

        nb_dict = {}
        for anno in didemo_anno_list:
            if anno['video'] not in nb_dict:
                nb_dict[anno['video']] = anno['num_segments']

        data = []
        for anno in tempo_anno_list:
            anno['num_segments'] = nb_dict[anno['video']]
            anno['times'] = anno['train_times']
            del anno['train_times']
            if not isinstance(anno['times'][0],list):
                anno['times'] = [anno['times']]
            data.append(anno)
        with open('data/new_tempoHL+didemo_{}.json'.format(split), 'w') as json_file:
            json.dump(data, json_file)

