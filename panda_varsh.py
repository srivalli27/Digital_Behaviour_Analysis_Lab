'''import pandas as pd

df = pd.read_csv("digital_behaviour.csv")
print(df)'''

import pandas as pd
import csv


df = pd.read_csv('digital_behaviour.csv')
print(df)
# df = reference || pointer
head_=df.head()
tail_=df.tail()
shape_=df.shape
column_=list(df.columns)
print(head_)
print(tail_)
print(shape_)
print(column_)
print(df['Instagram_Minutes'])
print(df[['Instagram_Minutes','Study_Minutes']].describe())
print(round(22/7,2))
print(df['Instagram_Minutes'].sum())
print(round(df['Study_Minutes'].mean(),2))
print(df['YouTube_Minutes'].max())
insta=head_["Instagram_Minutes"].sort_values(ascending=False)
print(insta)
print(df["Instagram_Minutes"].sort_values(ascending=False).head())
# operator chaining
print(head_["Instagram_Minutes"])#statdard
print(df["Study_Minutes"].sort_values(ascending=False).head())
total_s_t=(df["Instagram_Minutes"]+df["YouTube_Minutes"]+df["LinkedIn_Minutes"]+df["WhatsApp_Minutes"])
print(total_s_t)
df["Total_Screen_Time"]=total_s_t
print(df)
df["Screen_Hours"]=(total_s_t/60).round(2)
print(df)
df["Digital_Balance"]=(df["Study_Minutes"]/df["Total_Screen_Time"]).round(2)
print(df)
df["Day_Type"] = "NORMAL"
df[df["Total_Screen_Time"]>300]["Day_Type"]="Heavy"
#check the above statement it might be wrong 
print(df)  
df.loc[df["Total_Screen_Time"]>300,"Day_Type"]="HIGH"
print(df) 
# if in the above we didnt mention Day_Type as a parameter it makes the entire row as high #
# @ boolean Masking
"""df["Total_Screen_Time">300]["Day_Type"]="Heavy"
print(df)           
#IT'S AN ERROR"""
""" loc is inplace operation
    df[df["Total_Screen_Time"]>300]["Day_Type"]="Heavy"
    line 50 is standard (it is creating a copy ) """
print(df['Day_Type'].value_counts())
print(df["Instagram_Minutes"].sum())
print(df["YouTube_Minutes"].sum())
print(df["LinkedIn_Minutes"].sum())
print(df["Study_Minutes"].sum())
i=df["Instagram_Minutes"].sum()
y=df["YouTube_Minutes"].sum()
l=df["LinkedIn_Minutes"].sum()
max=0;
if(max<i):
    max=i
if(max<l):
    max=l
if(max<y):
    max=y
if(max==i):
    print("Insta")
if(max==y):
    print("You Tube")
if(max==l):
    print("LinkedIn")
App_Totals={
    "Insta":df["Instagram_Minutes"].sum(),
    "YouTube":df["YouTube_Minutes"].sum(),
}

most_time = max(App_totals,key=App_totals.get)


