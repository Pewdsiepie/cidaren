import json
import time
while True:
    f = open('c:\\cdr\\responseBody.txt', 'r', encoding='utf-8')
    j = json.load(f)
    #print(j['data']['options'])
    if 'options' in j['data']:
        lenth=len(j['data']['options'])
        for i in range(0,lenth):
            # print(j['data']['options'][i]['answer'])
            answer = str(j['data']['options'][i]['answer'])
            if answer == 'True':
                print(j['data']['options'][i]['content'])
        
    if 'answer_content' in j['data']:
        if 'stem' in j['data']:
            print(j['data']['answer_content'])
    time.sleep(4)
    import os
    i = os.system('cls')