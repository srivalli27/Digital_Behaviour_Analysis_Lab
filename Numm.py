import numpy as np
import csv

insta_min=[]
study_min=[]
with open('digital_behaviour.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_min.append(int(row['Instagram_Minutes']))
        study_min.append(int(row['Study_Minutes']))

insta_min=insta_min[:7]
study_min=study_min[:7]

insta = np.array(insta_min)
study = np.array(study_min)

#print(insta,study)
#total_insta = np.sum(insta)
total_insta = insta.sum()
avg_insta   = insta.mean()
max_insta   = insta.max()
min_insta   = insta.min()
days_insta  = len(insta)

total_study = study.sum()
avg_study = study.mean()
max_study = study.max()
min_study = study.min()
days_study = len(study)


print(insta[0] ,study[0],insta[-1] ,study[-1],insta[2] ,study[2])
print(insta[:3] ,study[:3],insta[-2:] ,study[-2:],insta[1:4] , study[1:4])
print(insta[::2] ,study[::2])

insta_hours = insta/60
insta_hours = insta_hours.round(2)

study_hours = study/60
study_hours = study_hours.round(2)

print(insta_hours,study_hours)
diff = study-insta
print(diff)

i_greater = insta>100
s_greater = study>100

greater = insta[insta>100]
data=[20,125,30,150,40,200,50]
above_avg = insta[insta>avg_insta]

print(above_avg)