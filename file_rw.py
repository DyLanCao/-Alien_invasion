import json


class FileRw():
    def __init__(self):
    def score_get(self):
        #f = open('data/record.json', encoding='utf-8')
        #high_score = json.load(f)
        #return high_score['high_score']
    def score_record(self):
        f1 = open('data/record.json','w',encoding='utf-8')
        json.dump(high_score,f1,indent=4,ensure_ascii=False)

