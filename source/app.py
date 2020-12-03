
from agent import Agent
from location import Location
from personal_paramters import PersonalParams
from gui import GUI 
from itterator import Iterator
import time
import random

class Application:

    

    def __init__(self,agents,name):
        print(name)
        self.sizex=1000
        self.sizey=1000
        self.numberOfAgents = agents
        self.mAgentsArray =[]
        self.window=GUI(self.sizex,self.sizey)
        self.iterator= Iterator()
        self.init()
        #self.window.join()
    
    def init(self):
        for x in range(self.numberOfAgents):
            # crate agent & appemd
            speed= 1+ random.randint(-5,5)/10
            locationArray = []
            rest = 84+random.randint(-24,24)
            origin = Location(random.randint(0,self.sizex),random.randint(0,self.sizey))
            locationArray.append(origin)
            intract = .5+random.randint(-25,50)/100

            if 2>random.randint(1,10):
                secondOrigin = Location(origin.cord[0]+random.randint(-1*self.sizex/4,self.sizex/4),origin.cord[1]+random.randint(-1*self.sizey/4,self.sizey/4))
                locationArray.append(secondOrigin)

            personalParams = PersonalParams(speed,1,locationArray,rest,intract)
            agent = Agent(self.sizex,self.sizey,personalParams)
            self.mAgentsArray.append(agent)


    def run(self):
        i=0
        array =[]
    
        count = 10#random.randint(0,30)
        for infect in range(count):
            index=random.randint(0,len(self.mAgentsArray))
            self.mAgentsArray[index].probabilities[self.mAgentsArray[index].ittr]=1.0
        while(1):
            
            #print("loop ",i)
            time.sleep(.1)
            self.iterator.runSingleTick(self.mAgentsArray,i)
            #print("agent size ",self.mAgentsArray.count)
            self.window.draw(self.mAgentsArray,i)
            i=i+1

