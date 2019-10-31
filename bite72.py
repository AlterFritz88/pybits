from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)

true_dic = {None: range(0, 10)}
for i, score in enumerate(scores):
    if score == 1000:
        true_dic[belts[i]] = range(1000, 10000000)
        break
    true_dic[belts[i]] = range(score, scores[i+1])



def get_belt(user_score):
    for k, v in true_dic.items():
        if user_score in v:
            return k

print(get_belt(999))