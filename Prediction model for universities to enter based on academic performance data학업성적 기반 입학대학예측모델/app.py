import pandas as pd 

#엑셀 만들어야하는데 엑셀이 안깔려있넹넹
data = pd.read_csv('gpascore.csv')
# print(data)

#빈칸 데이터를 읽어줌
# print(data.isnull().sum()) 
data= data.dropna()
# print(data.isnull().sum())

y데이터 = data['admit'].values

exit()

import numpy as np
import tensorflow as tf 

#딥러닝 model 디자인
model = tf.keras.models.Sequential([
 tf.keras.layers.Dense(64, activation='tanh'),
 tf.keras.layers.Dense(128, activation='tanh'),
 tf.keras.layers.Dense(1, activation = 'sigmoid'),
])
#함수는 sigmoid,tanh,relu,softmax,leakyRelu 등이 있따
#레이어에 activation funciton 넣기

#optimizer 목록 adam,adagrad,adadelta,rmsprop,sgd
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


#딥러닝 학습시킥
model.fit(np.array(x데이터),np.array(y데이터), epochs=10)
#x데이터 정답예측에 필요한 인풋 y데이터 정답


#예측
예측값 = model.predict([[750,3.7,3],[400,2.2,1]])
print(예측값)


#결론
#1모델만들고
#2데이터 집어넣고 학습
#3새로운 데이터 예측
#4 반복
#5 데이터전처리,모델튜닝 

