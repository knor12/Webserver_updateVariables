import logging
import threading
import time
from Hello import *


variable1 = 0; 
variable2 = 0; 
variable3 = 3; 


def getVariable(name):
    global  variable1
    global  variable2
    global  variable3
    if name == "variable1":
       return variable1
    elif name == "variable2":
       return variable2
    elif name == "variable3":
       return variable3
    else:        
       print (name + " not found in getVariable" )        


def setVariable(name, value):
    global  variable1
    global  variable2
    global  variable3
    if name == "variable1":
        variable1 = value
    elif name == "variable2":
        variable2 = value
    elif name == "variable3":
        variable3 = value
    else:    
        print (name + " not found in setVariable" )  

def UpdateVariable(name):
    while (True):
        time.sleep(0.01)
        setVariable("variable1", 3+getVariable("variable1"))
        setVariable("variable2", 7+getVariable("variable2"))
        setVariable("variable3", 11+getVariable("variable3"))
        #print("update variable1= "+str(getVariable("variable1")))