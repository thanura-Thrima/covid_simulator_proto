from location import Location
from probablity_calculator import ProbabilityCalculator
from interface_agent_bahavior import *
from personal_paramters import PersonalParams
import numpy as np
import random

class Agent:
    __count =0
    def __init__(self,locationx,locationy,personalParams):
        self.id= Agent.__count
        #print("create agent ID :",self.id)
        self.prob_calculator= ProbabilityCalculator()
        Agent.__count =Agent.__count+1
        self.location=personalParams.originList[0]
        #print("create agent ID :",self.id,"location ",self.location.cord)
        self.probabilities =[]
        self.probabilities.append(0.0)
        self.agents =[]
        self.ittr=0
        self.behavior=NormalBehavior()
        self.personalParameters= personalParams


    def distanceTo(self,agent):
        return self.location.calculateDistance(agent.location)
    
    def calulateDeltaProbability(self,agent):
        pass


    def calculateProb(self,arrayAgent):
        probDeltaArray =[]
        maxProb = self.probabilities[self.ittr]
        for agent in arrayAgent:
            self.agents[self.ittr].append(agent.id)
            value = self.prob_calculator.calculateDeltaProbabiliy(self.probabilities[self.ittr],agent.probabilities[self.ittr])
            probDeltaArray.append(value)
            if maxProb<agent.probabilities[self.ittr]:
                maxProb = agent.probabilities[self.ittr]
        
        self.probabilities.append(self.prob_calculator.calculateTotalProbability(self.probabilities[self.ittr],probDeltaArray,maxProb))

