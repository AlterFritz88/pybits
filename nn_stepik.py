import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from keras.models import load_model


data_for_train = pd.read_csv('norm_data.csv')


X = data_for_train[['discovered', 'passed', 'started_attempt', 'viewed']]
y = data_for_train['win_course']
y = to_categorical(y)
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

n_cols = X_train.shape[1]


from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.callbacks import ModelCheckpoint
from keras.optimizers import SGD

def mean_pred(y_true, y_pred):
    return roc_auc_score(y_true, y_pred)

model = Sequential()
model.add(Dense(units=32, activation='relu', input_shape=(n_cols,)))

model.add(Dropout(0.3))

epochs =8
opt = SGD(lr=0.1, decay=0.1/epochs, momentum=0.9, nesterov=True)
model.add(Dense(units=2, activation='softmax'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['acc'])


checpoint = ModelCheckpoint('model.h5f', monitor='val_loss', save_best_only=True, verbose=1)
callbacks = [checpoint]


model.fit(X_train, y_train, epochs=epochs, batch_size=2, validation_data=(X_test, y_test), callbacks=callbacks)

model = load_model('model.h5f')

data_for_train = pd.read_csv('data_train_events.csv')

X = data_for_train[['discovered', 'passed', 'started_attempt', 'viewed']]
y = data_for_train['win_course']
y = to_categorical(y)
score, acc = model.evaluate(X, y)

preds = model.predict(X)
print(roc_auc_score(y, preds))

print(score, acc)