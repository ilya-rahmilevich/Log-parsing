import re
import BasicLog

class VSServer(BasicLog):

    def __init__(self,filePath):
        BasicLog.__init__(self,filePath)

    def getNextData():
       with open(super().getFilePath(), 'r') as log:
         while True:
           line = log.readline()
           if not line:
              break
         fetch_code_extract = re.search(r'\bFETCHING\b',line)
         if fetch_code_extract: 
            print(fetch_code_extract)