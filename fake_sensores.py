from __future__ import division
import time
import random
import threading

class Refrigerator(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.cooling = False
        
    def run(self):
        global intern_temp
        self.cooling = True
        print "Refrigerator engine is On"
        while self.cooling:
            print "Current temperature is", intern_temp
            intern_temp += -0.1
            time.sleep(0.5)

    def stop(self):
        self.cooling = False
        print "Refrigerator engine is Off"

def read_temp():
#    global intern_temp
    return intern_temp

def read_humid():
    return random.randint(0, 1023)

if __name__ == "__main__":

    intern_temp = 22.2
    intern_humid = 78.2
    set_point = 20.0 
    
    engine = Refrigerator()
    
    while True:
        temp = read_temp()
        print "Current temperature is", temp
        if temp > set_point:
            engine.run()
        if temp <= set_point:
            engine.stop()
            #global intern_temp
            intern_temp = float(raw_input("Insert new chamber internal temperature: ")) 
        else:
            print "OK"
            
    