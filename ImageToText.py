# import the following libraries
# will convert the image to text string
import pytesseract
import re
import os
import os.path, time
import pandas as pd
from datetime import date
from datetime import datetime

# adds image processing capabilities
from PIL import Image

def imageToText(filenameImg):
	# opening an image from the source path
	img = Image.open('Images/'+filenameImg)

	# describes image format in the output
	print(img)
	# path where the tesseract module is installed
	pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
	# converts the image to result and saves it into result variable
	result = pytesseract.image_to_string(img)
	# write text in a text file and save it to source path
	filenameText = 'Text/'+filenameImg+'.txt'
	with open(filenameText,'w') as file:
		file.write(result)
		#print(result)
	return filenameText

def filterBadChar(nameStr):
	return re.sub('[^a-zA-Z ]', ' ', nameStr).strip()

def extractNames(filenameText):
	# Clean data image text file
	file = open(filenameText, 'r')
	content = file.readlines()

	content = [f.lower().strip() for f in content]
	delete_data = set()

	host = None
	num_participants = None

	# List cleaning
	for i in range(len(content)):
		bad_words = ['participant','mute','invite','assay','search','v mv v']
		content[i] = filterBadChar(content[i])
		#if 'host' in f:
		#	host = f
		#	delete_data.add(f)
		if len(content[i]) <= 3:
			delete_data.add(content[i])
		else:
			for b in bad_words:
				if b in content[i]:
					delete_data.add(content[i])

	for d in delete_data:
		content = list(filter((d).__ne__, content))

	with open(filenameText,'w') as file:
		file.write(', '.join(content))

	return filenameText, content

def getNames(filename):
	file = open(filename,'r')
	names = file.readlines()
	names = [i.strip().lower() for i in names]
	names.sort()
	#print(names)
	return names

def max_count(a,b,c):
	return (a if a>b and a>c else b if b>a and b>c else c )

def mark_attendance(df, imgList, colName):
    present = []
    for i in imgList:
    	imageNames = getNames(extractNames(imageToText(i))[0])
    	#present = []
    	for n in df['First Name']:
	        for m in imageNames:
	    	    if n in m:
	    	    	present.append(n)
	    	    	break
    	print(present)
    df[colName]=['P' if x in present else 'L' for x in df['First Name']]
    #print(df)
    print(df[colName].value_counts())
    #df.to_excel('8b-attendance.xlsx')
    return df

def attendance(excel,d):
    #imageToText('Images\m1.jpeg')
    imageNames = None
    present=[]
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p5=[]
    s1 = datetime.strptime('11:40','%H:%M')
    s2 = datetime.strptime('12:20','%H:%M')
    s3 = datetime.strptime('13:00','%H:%M')
    s4 = datetime.strptime('13:40','%H:%M')
    s5 = datetime.strptime('14:20','%H:%M')
    e1 = datetime.strptime('12:10','%H:%M')
    e2 = datetime.strptime('12:50','%H:%M')
    e3 = datetime.strptime('13:30','%H:%M')
    e4 = datetime.strptime('14:10','%H:%M')
    e5 = datetime.strptime('14:50','%H:%M')
    c1 = datetime.strptime('23:40','%H:%M')
    c2 = datetime.strptime('00:20','%H:%M')
    c3 = datetime.strptime('01:00','%H:%M')
    c4 = datetime.strptime('01:40','%H:%M')
    c5 = datetime.strptime('02:20','%H:%M')
    t1 = datetime.strptime('00:10','%H:%M')
    t2 = datetime.strptime('00:50','%H:%M')
    t3 = datetime.strptime('01:30','%H:%M')
    t4 = datetime.strptime('02:10','%H:%M')
    t5 = datetime.strptime('02:50','%H:%M')

    #excel = '6c-attendance'
    df = pd.read_excel(excel+'.xlsx')
    print(df)
    names = df['First Name']
    surname = df['Last Name']
    for i in os.listdir('Images'):
        t = time.ctime(os.path.getmtime('Images/'+i))
        T = datetime.strptime(t, "%a %b %d %H:%M:%S %Y")
        T = datetime.strptime(datetime.strftime(T, '%H:%M'),'%H:%M')
        print(T)
        if s1<T<e1 or c1<T<t1:
            p1.append(i)
        elif s2<T<e2 or c2<T<t2:
            p2.append(i)
        elif s3<T<e3 or c3<T<t3:
            p3.append(i)
        elif s4<T<e4 or c4<T<t4:
            p4.append(i)
        elif s5<T<e5 or c5<T<t5:
            p5.append(i)
	#for i in
    print(p1, p2, p3, p4, p5)
    #d = '04-09-2020'
    df = mark_attendance(df, p1, d+'(1)')
    df = mark_attendance(df, p2, d+'(2)')
    df = mark_attendance(df, p3, d+'(3)')
    df = mark_attendance(df, p4, d+'(4)')
    df = mark_attendance(df, p5, d+'(5)')

    #print(df)
    # print(df[colName].value_counts())
    df.to_excel(excel+'_'+d+'.xlsx')
    print(excel+'_'+d)

if __name__ == '__main__':
	attendance('8c-attendance','8c-test')
