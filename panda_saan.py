import pandas as pd
import csv

df = pd.read_csv('digital_behaviour.csv') #df = reference to dataframe object

print(df.head())

print(df.tail())

print(list(df.columns))

print(df.shape)

#print(df['Instagram_Minutes'].describe())

#print(df[['Instagram_Minutes' , 'YouTube_Minutes']].describe())

#print(max(df['Instagram_Minutes'].sum(),df['WhatsApp_Minutes'].sum(),df['YouTube_Minutes'].sum(),df['LinkedIn_Minutes'].sum()))

print(df['Study_Minutes'].mean().round(2))

print(df['Study_Minutes'].max())

print(df[df['Instagram_Minutes']>100])

print(df[df['Study_Minutes']>180])

#more_insta = df[df['Instagram_Minutes']> df['Study_Minutes']]

#print(more_insta['Instagram_Minutes'])

#danger_days = df[(df["Instagram_Minutes"] > 100 ) & (df["Study_Minutes"]<100)]

#print(danger_days)

#----PYTHON---- SORT FIRST FIVE IN REVERSE ORDER
#lst = list(df['Instagram_Minutes'].head(5))
#lst = lst[:5]
#list.sort(lst,reverse = True)
#print(lst)

#lst = df['Instagram_Minutes'].head(5)
#lst = lst[:5]

top_insta = df.sort_values('Instagram_Minutes', ascending=False).head(10)

top_study = df.sort_values('Study_Minutes', ascending=False).head(10)
print(top_insta['Instagram_Minutes'])

df['Total_Screen_Time'] = df['Instagram_Minutes'] + df['WhatsApp_Minutes'] + df['YouTube_Minutes'] + df['LinkedIn_Minutes']

#print(df['Total_Screen_Time'].head(5))

df['Screen_Hours'] = (df['Total_Screen_Time']/60).round(2)

print(df['Screen_Hours'].head(5))

df['Digital_Balance'] = (df['Study_Minutes']/ df['Total_Screen_Time']).round(2) #Series(Column) DIVISION

print(df['Digital_Balance'].head(5))

df['Day_Type'] =  'Normal'

#df['Total_Screen_Time' > 300]

df.loc[df['Total_Screen_Time'] > 300,'Day_Type']  = "Heavy" #LABEL BASED SELECTOR

print(df['Day_Type'].head(5))

#df[df['Total_Screen_Time'] > 300]['xyz'] = "Heavy"

#print(df['Day_Type'].head(5))

print(df['Day_Type'].value_counts())

print("Total Minutes on each app", df['Total_Screen_Time'])

app_totals={
    "Insta":df["Instagram_Minutes"].sum(),
    "YouTube":df["YouTube_Minutes"].sum(),
    "Whatsapp":df["WhatsApp_Minutes"].sum();
    
}

most_app = max(app_totals,key=app_totals.get)

heavy_days = df.loc[df['Day_Type']=='Heavy'].count()

best_study_day = df.loc[df['Instagram_Minutes'] > df['Study_Minutes'], ['Study_Minutes']]

study_Onheavy = df.loc[df['Total_Screen_Time'].idxmax(),['Study_Minutes']]

avg_digitalbalance = df['Digital_Balance'].mean()

df.to_csv('my_analysis.csv',index='False')