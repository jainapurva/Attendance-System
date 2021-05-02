from File import File
import config
import ImageTextConversion
import pandas as pd
import os

def folder_traversing(fileloc):
  path = fileloc
  filesList = list()
  print('Files/Folders to traverse: ',os.listdir(path))
  for i in os.listdir(path):
    if os.path.isdir(path+i):
      filesList.extend(folder_traversing(path+i))
    else:
      imageLoc = path+'\\'+i+'\\'
      section = None
      standard = None
      if '8a' in i.lower():
        section = 'a'
        standard = '8'
      elif '8b' in i.lower():
        section = 'b'
        standard = '8'
      elif '8c' in i.lower():
        section = 'c'
        standard = '8'
      
      for j in os.listdir(imageLoc):
        f = File(imageLoc+j, standard, section)
        filesList.append(f)
        #print(filesList)
  #print('List: ', filesList)
  return filesList

def markAttendance(presentDictionary):
  df_8a = pd.read_excel(config.nameLocation+'8a-attendance.xlsx')
  df_8b = pd.read_excel(config.nameLocation+'8b-attendance.xlsx')
  df_8c = pd.read_excel(config.nameLocation+'8c-attendance.xlsx')
  for key in presentDictionary.keys():
    df = None
    columnName = key[:10]+'('+key[-1]+')'
    standard = key[10:12]
    if standard == '8a':
      df = df_8a
    elif standard == '8b':
      df = df_8b
    elif standard == '8c':
      df = df_8c
    #for i in presentDictionary[key]:
    df[columnName] = ['P' if i in presentDictionary[key] else 'L' for i,value in df.iterrows()]
  
  os.chdir(config.attendanceLocation)
  #df_8a.drop(df_8a.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
  df_8a.to_excel('8a-attendance.xlsx')
  df_8b.to_excel('8b-attendance.xlsx')
  df_8c.to_excel('8c-attendance.xlsx')
  print('Attendance Marked')
  #print(df_8a)
  return 0


if __name__ == "__main__":
    fileList = folder_traversing(config.imagesLocation)
    #print(fileList)
    presentStudentsDict = dict()
    for f in fileList:
      date = f.getFileDate()
      #print(type(date))
      key = str(date)+f.standard+f.section+str(f.period)
      if key in presentStudentsDict:
        presentStudentsDict[key].update(f.presentIndex)
      else:
        presentStudentsDict[key] = set(f.presentIndex)
    markAttendance(presentStudentsDict)
    #print(presentStudentsDict)
    
    #print(df)
    #present = ImageTextConversion.mark_attendance(content,df, config.duplicateNames)
    #print(present)