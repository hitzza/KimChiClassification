import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

#트레이닝 데이터, 검증데이터 불러오기
Train = np.load('./NewTrainData.npy')
Valid = np.load('./NewValidData.npy')
#넘파이 파일을 데이터 프레임으로 변경 + 컬렴명 추가
TrainDataFrame = pd.DataFrame(Train, columns=['fermentation_phase','process_step','production_brand','production_temperature','fermentation_day','maturity'])
ValidDataFrame = pd.DataFrame(Valid, columns=['fermentation_phase','process_step','production_brand','production_temperature','fermentation_day','maturity'])

#품목의 공정 단계 ,브랜드 컬럼 삭제
TrainDataFrame = TrainDataFrame.drop(['process_step','production_brand'],axis='columns')
ValidDataFrame = ValidDataFrame.drop(['process_step','production_brand'],axis='columns')

#트레이닝 데이터 검증데이터 분리
X_train  = TrainDataFrame.drop('maturity',axis=1)
X_test = ValidDataFrame.drop('maturity',axis=1)
Y_train = TrainDataFrame['maturity']
Y_test = ValidDataFrame['maturity']


print(TrainDataFrame)
#분류모델 임포트
knn = KNeighborsClassifier()
#최소 최대 스케일러 임포트
mm_scaler = MinMaxScaler()

#데이터 스케일링
mm_scaler.fit(X_train)
X_train_scaled = mm_scaler.transform(X_train)
X_test_scaled = mm_scaler.transform(X_test)

#학습
knn.fit(X_train_scaled,Y_train)
pred = knn.predict(X_test_scaled)
#검증
score =  accuracy_score(Y_test,pred)

print(score)