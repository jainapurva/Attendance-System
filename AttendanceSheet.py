import os
import pandas as pd
from datetime import date

def getNames(filename):
	file = open(filename,'r')
	names = file.readlines()
	names = [i.strip().lower() for i in names]
	names.sort()
	#print(names)
	return names

def max_count(a,b,c):
	return (a if a>b and a>c else b if b>a and b>c else c )

if __name__ == "__main__":
    #imageToText('Images\m1.jpeg')
    imageNames = None
    a6 = getNames('6a.txt')
    #print(a8)
    b6 = getNames('6b.txt')
    c6 = getNames('6c.txt')
    df = pd.DataFrame(columns=['First Name','Last Name'])
    #print(df)
    for i in c6:
    	i = i.split()
    	df = df.append({'First Name':i[0], 'Last Name': i[1]}, ignore_index = True)
    	print(df)
    # names = df['First Name']
    # surname = df['Last Name']
    # present=[]
    # for i in os.listdir('Images'):
    # 	colName = date.today().strftime("%d/%m/%Y")+'(1)'
    # 	imageNames = getNames(extractNames(imageToText(i))[0])
    # 	#present = []
    # 	for n in df['First Name']:
	#         for m in imageNames:
	#     	    if n in m:
	#     	    	present.append(n)
	#     	    	break
    # 	print(present)
    #df[colName]=['P' if x in present else 'L' for x in df['First Name']]

    df.to_excel('6c-attendance.xlsx')
    print(df)
