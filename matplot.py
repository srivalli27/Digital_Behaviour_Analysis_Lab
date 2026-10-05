import pandas as pd
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

df = pd.read_csv('digital_behaviour.csv')

df['Total_Screen_Time'] = df['Instagram_Minutes']+df['Study_Minutes']+df['YouTube_Minutes']

df['day_label'] = [f"Day {i+1} " for i in range(len(df))]

res = plt.figure(figsize=(12,6))

bar_ = plt.bar(df['day_label'],df['Total_Screen_Time'],color='blue')

plt.title('Screen Time By Day')
plt.xlabel('Days')
plt.ylabel('Total Screen Time')
plt.xticks(rotation=45)

#plt.tight_layout()

plt.savefig('charts/total_screen_time.png')
plt.close()

app_totals={
    "Insta":df["Instagram_Minutes"].sum(),
    "YouTube":df["YouTube_Minutes"].sum(),
    "WhatsApp":df["WhatsApp_Minutes"].sum(),
    "LinkedIn":df["LinkedIn_Minutes"].sum()
}

plt.figure(figsize=(12,8))
plt.bar(app_totals.keys(),app_totals.values(),color='orange')
plt.title('totals')
plt.xlabel('Days')
plt.ylabel('Totals')
plt.xticks(rotation=45)

plt.savefig('charts/bar_total.png')
plt.close()

plt.figure(figsize=(12,6))
plt.plot(df['day_label'],df['Study_Minutes'],marker='o',label='study',color='r')
plt.plot(df['day_label'],df['Total_Screen_Time'],marker='o',label='screen',color='b')
plt.legend()
plt.title("Study vs Screen per day")
plt.xlabel('Days')
plt.ylabel('Minutes')
plt.xticks(rotation=45)

plt.savefig('charts/studymin.png')
plt.close()



plt.figure(figsize=(12,6))
plt.pie(app_totals.values(),labels=app_totals.keys(),autopct='%1.1f%%',startangle=0)
plt.title("Total spent on Apps")

plt.savefig('charts/totals.png')
plt.close()