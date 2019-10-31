from keras.models import load_model
import pandas as pd


model = load_model('model.h5f')

data = pd.read_csv('test_pivored.csv')
#X = data[['passed', 'discovered']]

#preds = model.predict(X)
ids = []
predicts = []
for index, item in data.iterrows():

    pred = model.predict([[[item['passed']]]])

    predicts.append(round(pred[0][1], 2))
    ids.append(item['user_id'])

print(ids)
print(predicts)

frame = pd.DataFrame({'user_id': ids, 'is_gone': predicts})
print(len(frame))
frame.to_csv('anwer.csv')