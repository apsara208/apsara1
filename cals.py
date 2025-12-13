#conditional statements with formulas
from data import df_12,df_6
import pandas as pd
import numpy as np
continue_program=True   
while  continue_program:
    data=int(input("what type of data do you want ?monthy(1)or 6 or 12 months data?"))
    if data==1:
        month=input("enter month:jan,feb,march,april,may,june ")
        if month not in df_6.index:
            print("invalid month")
        else:
            print(df_6.loc[month])
    elif data==6:
        nav6=input("nav6:tc:totalcost,pc:productioncost,mc:materialcost,hce:humancapitalexpense,lc:logisticscost,oc:overhead,rv:remainingmaterialvolume,ttc:totaltotalcost= ")
        if nav6=="tc":
            df_6["total cost"]=df_6["material cost"]+df_6["human capital expense"]+df_6["logistics cost"]+df_6["overhead"]
            print(df_6)
        elif nav6=="pc":
            pc=df_6["production volume"].sum()
            print(pc)
        elif nav6=="mc":
            mc=df_6["material cost"].sum()
            print(mc)
        elif nav6=="hce":
            hce=df_6["human capital expense"].sum()
            print(hce)
        elif nav6=="lc":    
            lc=df_6["logistics cost"].sum()
            print(lc)
        elif nav6=="oc":
            oc=df_6["overhead"].sum()
            print(oc)
        elif nav6=="rv":
            rv=df_6["production volume"].sum()-df_6["sales volume"].sum()
            print(rv)
        elif nav6=="ttc":
            df_6["total cost"]=df_6["material cost"]+df_6["human capital expense"]+df_6["logistics cost"]+df_6["overhead"]
            ttc=df_6["total cost"].sum()
            print(ttc)
        else:
            print("invalid input")

    elif data==12:
        nav12=input("tc:totalcost,pc:productioncost,mc:materialcost,hce:humancapitalexpense,lc:logisticscost,oc:overhead,rv:remainingmaterialvolume")
        if nav12=="tc":
            df_12["total cost"]=df_12["material cost"]+df_12["human capital expense"]+df_12["logistics cost"]+df_12["overhead"]
            print(df_12)
        elif nav12=="pc":
            pc=df_12["production volume"].sum()
            print(pc)
        elif nav12=="mc":
            mc=df_12["material cost"].sum()
            print(mc)
        elif nav12=="hce":
            hce=df_12["human capital expense"].sum()
            print(hce)
        elif nav12=="lc":    
            lc=df_12["logistics cost"].sum()
            print(lc)
        elif nav12=="oc":
            oc=df_12["overhead"].sum()
            print(oc)
        elif nav12=="rv":  
            rv=df_12["production volume"].sum()-df_12["sales volume"].sum()
            print(rv)
        elif nav12=="ttc":
            df_12["total cost"]=df_12["material cost"]+df_12["human capital expense"]+df_12["logistics cost"]+df_12["overhead"]
            ttc=df_12["total cost"].sum()
            print(ttc)
        else:
            print("invalid input")
    else:
        print("invalid input")
    user_choice=input("do you want to continue?yes/no:y/n")
    if user_choice.lower()!="y":
            continue_program=False