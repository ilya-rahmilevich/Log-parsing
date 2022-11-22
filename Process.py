import re
from BasicLog import BasicLog

class Process (BasicLog):

    def __init__(self,filePath):
      BasicLog.filePath = filePath

    def getNextData(self,process):
       with open(BasicLog.filePath, 'r') as log:
         while True:
           line = log.readline()
           if not line:
              break
           if process in line:
              start_time = re.search(r'Taken Start: /d{2}-/d{2}/d{4} /d:/d{2}:/d{2} [AM|PM]',line).group(0)
              end_time = re.search(r'end: /d{2}-/d{2}/d{4} /d:/d{2}:/d{2} [AM|PM]',line).group(0)
              while line != "Success":
                line = log.readline()
              status = re.search(r'ReturnCode: Success',line).group(0).split(" ")[1]
              return [start_time,end_time,status]