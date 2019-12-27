import json
import sys

f = open('data/record.json', encoding='utf-8')
#f = open('data/record.json',"w")
#print(f)
high_score = json.load(f)
print(high_score)
#print(high_score['high_score'])

high_score['high_score'] = 345

#print(high_score['high_score'])

f1 = open('data/record.json','w',encoding='utf-8')

json.dump(high_score,f1,indent=4,ensure_ascii=False)



