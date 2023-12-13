# 데이터 정렬 파일

import os
import json
import numpy as np

#데이터가 있는 디렉터리
train_path = 'train_data'
valid_path = 'valid_data'

# 경로 내에 파일을 모두 불러옴
train_file_list = os.listdir(train_path)
valid_file_list = os.listdir(valid_path)

#json 확장자를 가진 파일로 새로운 리스트 생성
train_json_file_list = [file for file in train_file_list if file.endswith('.json')]
valid_json_file_list = [file for file in valid_file_list if file.endswith('.json')]

#변환된 데이터를 담을 리스트
TrainDataFrame = []
ValidDataFrame = []
'''

for i in train_json_file_list:
	with open('./train_data/'+i,  encoding = 'utf-8') as f:
		try: TrainDataFrame.append(json.load(f)) 
		except: print(i+'error')


newTest = np.array(TrainDataFrame)

np.save('C:\kimchi\TrainData',newTest)

'''
#불러온 제이슨 파일 리스트를 순회
for i in valid_json_file_list:
	#해당 경로의 제이슨 파일을 인코딩 하여
	with open('./valid_data/'+i,  encoding = 'utf-8') as f:
		#ValidDataFrame에 하나 씩 푸시
		try: ValidDataFrame.append(json.load(f)) 
		#파일 수가 많아져서 에러가 뜨는 이슈가 있어 try except문을 작성
		except: print(i+'error')

#리스트를 넘파이 배열로 전환
newTest = np.array(ValidDataFrame)
#새 파일로 저장
np.save('C:\kimchi\ValidData',newTest)
#np.save('C:\kimchi\TestData',newTest)