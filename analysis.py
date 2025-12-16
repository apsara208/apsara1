from data import df_6,df_12
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
analyze_more=True
while analyze_more:
    analyze=(input("Do you want to analyze 6 months data or 12 months data? (enter 6 or 12): "))
    if analyze=="6":
        month=input("Enter month (jan, feb, march, april, may, june): ")
        if month not in df_6.index:
            print("Invalid month")
        else:
            plt.figure(figsize=(10,6))
            df_6.loc[month].plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
            plt.title(f'Cost Analysis for {month.capitalize()} (6 Months Data)')    
            plt.ylabel('Values')
            plt.xlabel('Categories')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            plt.tight_layout()
            plt.savefig(f'cost_analysis_6months_{month}.png')
    elif analyze=="12":
        month=input("Enter month (jan, feb, march, april, may, june, july, aug, sept, oct, nov, dec): ")
        if month not in df_12.index:
            print("Invalid month")
        else:
            plt.figure(figsize=(10,6))
            df_12.loc[month].plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
            plt.title(f'Cost Analysis for {month.capitalize()} (12 Months Data)')    
            plt.ylabel('Values')
            plt.xlabel('Categories')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            plt.tight_layout()
            plt.savefig(f'cost_analysis_12months_{month}.png')
    else:
        print("Invalid input. Please enter 6 or 12.")
    more_analysis=input("Do you want to analyze another month? (yes/no): ").lower()
    if more_analysis!="yes" or more_analysis!="y":
        analyze_more=False
            