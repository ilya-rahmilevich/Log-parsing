import re
from VSServer import VSServer

if __name__ == "__main__":
    vsp = VSServer("4Y\Synopsis\VSServer.2022.10.30.log")
    vsp.getNextData()
