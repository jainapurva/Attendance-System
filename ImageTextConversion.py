import pytesseract
import re
import os
import os.path, time
import pandas as pd
from datetime import date
from datetime import datetime
import config
import glob
import numpy as np
# adds image processing capabilities
from PIL import Image

def imageToText(filenameImg):
  # opening an image from the source path
  img = Image.open(filenameImg)
  # describes image format in the output
  # #print(img)
  # path where the tesseract module is installed
  pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
	# converts the image to result and saves it into result variable
  result = pytesseract.image_to_string(img)
  # write text in a text file and save it to source path
  head,tail = os.path.split(filenameImg)
  filenameText = config.textLocation+tail+'.txt'
  with open(filenameText,'w') as file:
    file.write(result)
  return filenameText

def filterBadChar(nameStr):
	return re.sub('[^a-zA-Z ]', ' ', nameStr).strip()

def extractNames(filenameText):
  # Clean data image text file
  file = open(filenameText, 'r')
  content = file.readlines()
  content = [f.lower().strip() for f in content]
  content = [f for f in content if f != '']
  #print(content)
  content.sort()
  return content

def findPresent(imageNameList, studentDF, duplicateNames):
  presentKeys = []
  for key, value in studentDF.iterrows():
    for namesLine in imageNameList:
      if value['First Name'] in duplicateNames:
        if value['First Name'] in namesLine and value['Last Name'] in namesLine:
          presentKeys.append(key)
          break
      elif value['First Name'] in namesLine:
        presentKeys.append(key)
        break
  
  return presentKeys