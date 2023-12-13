import numpy as np

train = np.load('./ValidData.npy', allow_pickle=True)
fermentation_phase = []
process_step =[]
production_brand = []
production_temperature = []
fermentation_day = []
maturity = []

#print(train)
newValid = []
for i in train :
   # print(i['info'])
    newValid.append(i['info'])
#print(newValid)
for j in newValid:
   fermentation_phase.append( j['fermentation_phase'])
   process_step.append( j['process_step'])
   production_brand.append( j['production_brand'])
   production_temperature.append( j['production_temperature'])
   fermentation_day.append( j['fermentation_day'])
   if j['maturity'] == '미숙':
      maturity.append(0)
   elif j['maturity'] == '적숙':
      maturity.append(1)
   elif j['maturity'] == '과숙':
      maturity.append(2)
#print(newTrain['item_name'])
ValidData = np.array([fermentation_phase,process_step,production_brand,production_temperature,fermentation_day,maturity])
NewValidData =  ValidData.transpose()
print(NewValidData)
np.save('C:/kimchi/NewValidData', NewValidData)