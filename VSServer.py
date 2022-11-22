import re
from BasicLog import BasicLog
from Fetching import Fetching

class VSServer(BasicLog):      

    def __init__(self,filePath):
      BasicLog.filePath = filePath

    def getNextData(self):
       fp = Fetching("4Y\Synopsis\FetchingService.2022.10.30.log")
       with open(BasicLog.filePath, 'r') as log:
         while True:
           line = log.readline()
           if not line:
              break
           if 'Fetching' in line:
            fetch_id_extract = re.search(r'Fetching Task: Id: \d{4}',line).group(0)
            process_extract = re.search(r'processing task: Id: \d{3}',line).group(0)
            print(fp.getNextData(fetch_id_extract,process_extract))