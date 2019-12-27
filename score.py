import json
from game_stats import GameStats

class Score():
    def __init__(self):
        f = open('data/record.json', encoding='utf-8')
        score_json = json.load(f)
        self.high_score = score_json['high_score']

    def score_get(self):
        f = open('data/record.json', encoding='utf-8')
        score_json = json.load(f)
        self.high_score = score_json['high_score']
        return self.high_score
    def score_record(self,high_score):
        f = open('data/record.json', encoding='utf-8')
        score_json = json.load(f)
        score_json['high_score'] = high_score
        f1 = open('data/record.json', 'w',encoding='utf-8')
        json.dump(score_json,f1,indent=4,ensure_ascii=False) 
