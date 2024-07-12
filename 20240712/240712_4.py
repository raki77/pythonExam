import sys
import os 
 
other_folder_path = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(other_folder_path)
 
import utils.shjungUtil as ut

scores = {"학번": 1, "수학": 0, "영어":50, "코딩":100}
for subject in scores.keys():    
    if subject == '학번':
        print("="*60)
        print(subject, ut.lpad(str(scores[subject]), 6, '0'))
        print("-"*60)
    else:
        print(subject, scores[subject])
        

print()
print("{0:,}".format(100000000))
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))
print("{0:^<+30,}".format(100000000))

print("{0}".format(5/3))
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))

#################### SAVE FILE ####################
print()
score_file = open("score.txt", "w", encoding="utf-8")
#score_file = open("score.txt", "a", encoding="utf-8") # overwrite
scores = {"학번": 1, "수학": 0, "영어":50, "코딩":100}
for subject in scores.keys():    
    if subject == '학번':
        score_file.write("="*60 +"\n")
        score_file.write(subject +" : "+ str(ut.lpad(str(scores[subject]), 6, '0')) +"\n")
        score_file.write("-"*60 +"\n")
    else:
        score_file.write(subject +" : "+ str(scores[subject]) +"\n")
        
score_file.close()


#################### READ FILE ####################
read_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = read_file.readline() # readlines() --> for keyword possible
    if not line:
        break
    print(line, end="")        
read_file.close()

