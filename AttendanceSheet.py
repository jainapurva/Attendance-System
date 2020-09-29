import os
import pandas as pd
from datetime import date
import config

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
	for i in os.listdir(config.nameListTxt):
		print(i)
		temp = getNames(config.nameListTxt+i)
		df = pd.DataFrame(columns=['First Name','Last Name'])
		for j in temp:
			j=j.split()
			df = df.append({'First Name':j[0].lower(), 'Last Name': j[1].lower()}, ignore_index = True)
			print(df)
		df.to_excel(config.nameLocation+i+'-attendance.xlsx')

    # a6 = getNames(config.nameListTxt+'6a.txt')
    # #print(a8)
    # b6 = getNames(config.nameListTxt+'6b.txt')
    # c6 = getNames(config.nameListTxt+'6c.txt')
    # df = pd.DataFrame(columns=['First Name','Last Name'])
    # #print(df)
    # for i in c6:
    # 	i = i.split()
    # 	df = df.append({'First Name':i[0], 'Last Name': i[1]}, ignore_index = True)
    # 	print(df)
    # # names = df['First Name']
    # # surname = df['Last Name']
    # # present=[]
    # # for i in os.listdir('Images'):
    # # 	colName = date.today().strftime("%d/%m/%Y")+'(1)'
    # # 	imageNames = getNames(extractNames(imageToText(i))[0])
    # # 	#present = []
    # # 	for n in df['First Name']:
	# #         for m in imageNames:
	# #     	    if n in m:
	# #     	    	present.append(n)
	# #     	    	break
    # # 	print(present)
    # #df[colName]=['P' if x in present else 'L' for x in df['First Name']]
	#
    # df.to_excel('6c-attendance.xlsx')
    # print(df)
