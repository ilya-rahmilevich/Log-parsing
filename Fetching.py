import re
from BasicLog import BasicLog
from Process import Process

class Fetching (BasicLog):

    def __init__(self,filePath):
      BasicLog.filePath = filePath

    def getNextData(self,fetch,process):
       pp = Process("4Y\Synopsis\ProcessingServer.2022.10.30.log")
       with open(BasicLog.filePath, 'r') as log:
         while True:
           line = log.readline()
           if not line:
              break
           if fetch in line:
              items = []
              start_time = re.search(r'StartTime: /d{2}/d{2}/d{4} /d:/d{2}:/d{2} [AM|PM]',line).group(0)
              end_time = re.search(r'EndTime: /d{2}/d{2}/d{4} /d:/d{2}:/d{2} [AM|PM]',line).group(0)
              while line != "Success":
                line = log.readline()
              status = re.search(r'status: Success',line).group(0).split(" ")[1]
              items.extend([start_time,end_time,status])
              items.extend(pp.getNextData(process))
              return items

              
           
    

