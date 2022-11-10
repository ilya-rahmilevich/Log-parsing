class BasicLog:
    
    def __init__(self,filePath):
       self.filePath = filePath

    @property
    def filePath(self):
        return self.filePath
       
    @filePath.setter
    def filePath(self,filePath):
        self.filePath = filePath
