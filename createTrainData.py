import numpy as np
#data.py에서 내보낸 파일을 불러와서
train = np.load('./TrainData.npy', allow_pickle=True)

#해당 컬럼명에 해당하는 데이터를 받을 리스트 미리 선언
fermentation_phase = []
process_step =[]
production_brand = []
production_temperature = []
fermentation_day = []
maturity = []

#최종 필터링된 데이터를 담을 리스트
newTrain = []

#데이터 필터링
for j in newTrain:
   fermentation_phase.append( j['fermentation_phase'])
   process_step.append( j['process_step'])
   production_brand.append( j['production_brand'])
   production_temperature.append( j['production_temperature'])
   fermentation_day.append( j['fermentation_day'])
   #미숙은 0 적숙은 1 과숙은 2로 저장
   if j['maturity'] == '미숙':
      maturity.append(0)
   elif j['maturity'] == '적숙':
      maturity.append(1)
   elif j['maturity'] == '과숙':
      maturity.append(2)

#넘파일 배열로 재생성
TrainData = np.array([fermentation_phase,process_step,production_brand,production_temperature,fermentation_day,maturity])
#전치 행렬로 만들어서 사용하기 좋은 데이터로 재배열
newTrainData =  TrainData.transpose()
print(newTrainData)
#저장
np.save('C:/kimchi/NewTrainData', newTrainData)