from scipy import spatial
import numpy as np 
import random
import matplotlib.pyplot as plt

class Iterator:
    def __init__(self):
        pass

    def plot(self,probabilities):
        n, bins, patches = plt.hist(x=probabilities, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('My Very Own Histogram')
        plt.text(23, 45, r'$\mu=15, b=3$')
        maxfreq = n.max()
        # Set a clean upper y-axis limit.
        plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

    def runSingleTick(self,agents,tick):
        kdTreeArray =[]
        for agent in agents:
            #print("agent id",agent.id)
            agent.location.cord[0]+=random.randint(-15,15)
            agent.location.cord[1]+=random.randint(-15,15)
            kdTreeArray.append([agent.location.cord[0],agent.location.cord[1]])
    
        kdTree= spatial.KDTree(kdTreeArray)
        i=0
        probs=[]
        for agent in agents:
            #print("agent id : ",kdTreeArray[i])
            array_ = kdTree.query_ball_point(kdTreeArray[i],20,2)
            i+=1
            agentArryForCalc =[]
            #print("number of array : ",array_)
            for id in array_:
                agentArryForCalc.append(agents[id])
                #print("agent" ,id," cord ",kdTreeArray[id])
            agent.behavior.doProbablityCalculation(agent,agentArryForCalc)
            agent.ittr=agent.ittr+1
            probs.append(agent.probabilities[agent.ittr])
        #self.plot(probs)
