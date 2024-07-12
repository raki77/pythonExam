import sys
import os

# other_folder 경로를 sys.path에 추가
other_folder_path = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(other_folder_path)

# 이제 other_file을 임포트할 수 있습니다.
import utils.shjungUtil as ut

scores = {"학번": 1, "수학": 0, "영어":50, "코딩":100}
for subject in scores.keys():    
    if subject == '학번':
        print(subject, ut.lpad(str(scores[subject]), 6, '0'))
    else:
        print(subject, scores[subject])
        
       
