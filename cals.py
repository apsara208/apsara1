#conditional statements with formulas
from data import df_12,df_6
import pandas as pd
import numpy as np
continue_program=True   
while  continue_program:
    data=int(input("monthy(1)or 6 or 12 months data?"))
    if data==1:
        month=input("enter month:")
    elif data==6:
        nav6=input("nav6:tc:totalcost,pc:productioncost,mc:materialcost,hce:humancapitalexpense,lc:logisticscost,oc:overhead,rv:remainingmaterialvolume,ttc:totaltotalcost")
        if nav6=="tc":
            df_6["total cost"]=df_6["material cost"]+df_6["human capital expense"]+df_6["logistics cost"]+df_6["overhead"]
            print(df_6)
        elif nav6=="pc":
            pc=df_6["jan"].values[0]+["feb"].values[0]+df_6["march"].values[0]+df_6["april"].values[0]+df_6["may"].values[0]+df_6["june"].values[0]
            print(pc)
        elif nav6=="mc":
            mc=df_6["jan"].values[1]+["feb"].values[1]+df_6["march"].values[1]+df_6["april"].values[1]+df_6["may"].values[1]+df_6["june"].values[1]
            print(mc)
        elif nav6=="hce":
            hce=df_6["jan"].values[2]+["feb"].values[2]+df_6["march"].values[2]+df_6["april"].values[2]+df_6["may"].values[2]+df_6["june"].values[2]
            print(hce)
        elif nav6=="lc":    
            lc=df_6["jan"].values[3]+["feb"].values[3]+df_6["march"].values[3]+df_6["april"].values[3]+df_6["may"].values[3]+df_6["june"].values[3]
            print(lc)
        elif nav6=="oc":
            df_6["overhead"]=df_6["jan"].values[4]+["feb"].values[4]+df_6["march"].values[4]+df_6["april"].values[4]+df_6["may"].values[4]+df_6["june"].values[4]
            print(df_6)
        elif nav6=="rv":
            rv=(df_6["jan"].values[0]+["feb"].values[0]+df_6["march"].values[0]+df_6["april"].values[0]+df_6["may"].values[0]+df_6["june"].values[0])-((df_6["jan"].values[1]+["feb"].values[1]+df_6["march"].values[1]+df_6["april"].values[1]+df_6["may"].values[1]+df_6["june"].values[1])/20)
            print(rv)
        elif nav6=="ttc":
            ttc=df_6["jan"].values[5]+["feb"].values[5]+df_6["march"].values[5]+df_6["april"].values[5]+df_6["may"].values[5]+df_6["june"].values[5]
            print(ttc)

        user_choice=input("do you want to continue?yes/no:")
        if user_choice.lower()!="yes":
            continue_program=False
'''elif data=="12":
    nav12=input("tc:totalcost,pc:productioncost,mc:materialcost,hce:humancapitalexpense,lc:logisticscost,oc:overhead,rv:remainingmaterialvolume")
def cal12():
    if nav12=="tc":
        df_12["total cost"]=df_12["material cost"]+df_12["human capital expense"]+df_12["logistics cost"]+df_12["overhead"]
        return '''