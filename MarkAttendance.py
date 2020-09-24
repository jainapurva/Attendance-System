#Extracted names to attendance sheet

import imageToText;
from datetime import datetime, date;

class MarkAttendance(object):
    """docstring for MarkAttendance."""

    def __init__(self, month):
        self.month = month

    def folderProcess(self):
        os.chdir(month)
        for i in os.listdir():
            #Find modified directory sysdate
            modifiedTime = time.ctime(os.path.getmtime(i))
            modifiedTime = datetime.strptime(modifiedTime, "%a %b %d %H:%M:%S %Y")
            modifiedTime = datetime.strptime(datetime.strftime(modifiedTime, '%b:%d'),'%b:%d')
            today = datetime.strptime(datetime.datetime.now(),'%b:%d')
            if modifiedTime == today:
                os.chdir(i)
                for j in os.listdir():
                    modifiedTime = time.ctime(os.path.getmtime(j))
                    modifiedTime = datetime.strptime(modifiedTime, "%a %b %d %H:%M:%S %Y")
                    modifiedTime = datetime.strptime(datetime.strftime(modifiedTime, '%b:%d'),'%b:%d')
                    today = datetime.strptime(datetime.datetime.now(),'%b:%d')
                    



        os.chdir('..')
