""""Date",
    "Instagram_Minutes",
    "YouTube_Minutes",
    "WhatsApp_Minutes",
    "LinkedIn_Minutes",
    "Reels_Watched",
    "Videos_Watched",
    "Messages_Sent",
    "Posts_Liked",
    "Study_Minutes","""
import csv
app="instagram"
minutes=[]
with open('digital_behaviour.csv','r',encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            minutes.append(int(row['Instagram_Minutes']))

minutes = minutes[0:7]





total=sum(minutes)
avg=total//len(minutes)

highest = max(minutes)
lowest  = min(minutes)

above_avg=0
for x in minutes:
    if x>avg:
        above_avg+=1

print(f"spent {sum} total minutes , {avg} average minutes on {app}\nfor a day highest and lowest are {highest}, {lowest} minutes\n number of days spent more than avg are {above_avg}")