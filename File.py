#File class to get and store file details
import os
import os.path, time
from datetime import datetime, timedelta, date
import config
import ImageTextConversion
import pandas as pd

class File():
    """docstring for File."""

    def __init__(self, name, standard, section):
        #super(File, self).__init__()
        self.name = name
        #time format "Thu Apr 22 11:04:10 2021"
        self.time = time.ctime(os.path.getctime(self.name))
        self.period = self.getPeriod(config.classStartTime)
        self.standard = standard
        self.section = section
        self.dataframe = self.getDataframe()
        self.duplicateNames = self.getDuplicateNames()
        self.textFile = ImageTextConversion.imageToText(name)
        self.textFileText = ImageTextConversion.extractNames(self.textFile)
        self.presentIndex = ImageTextConversion.findPresent(self.textFileText,self.dataframe,self.duplicateNames)
        

    def getFileDate(self):
        T = datetime.strptime(self.time, "%a %b %d %H:%M:%S %Y")
        return datetime.strftime(T, '%d-%m-%Y')
        

    def getFileTime(self):
        T = datetime.strptime(self.time, "%a %b %d %H:%M:%S %Y")
        T = datetime.strptime(datetime.strftime(T, '%H:%M:%S'),'%H:%M:%S')
        return T
    
    def getPeriod(self, startTime):
        endTime = datetime.strptime(startTime, "%H:%M:%S")
        for i in range(5):
            endTime += timedelta(minutes=40)
            if self.getFileTime() <= endTime:
                break
        return i+1
    
    def getDataframe(self):
        df = config.nameLocation+self.standard+self.section+'-attendance.xlsx'
        return pd.read_excel(df)
    
    def getDuplicateNames(self):
        if self.standard=='8' and self.section=='a':
            return config.duplicateNames8a
        if self.standard=='8' and self.section=='b':
            return config.duplicateNames8b
        if self.standard=='8' and self.section=='c':
            return config.duplicateNames8c
    
    def getStandard(self):
        pass

    def getSection(self):
        pass