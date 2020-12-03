class IAgentBahavior:
    def doProbablityCalculation(self,me,agentList):
        pass

    def doIndividualCalculation(self,me,agent):
        pass

    def doMovement(self,me):
        pass


class NormalBehavior(IAgentBahavior):
    
    def doProbablityCalculation(self,me,agentList):
        #print("inside doProbabilityCalculation")
        probDeltaArray=[]
        maxProb = me.probabilities[me.ittr]
        for agent in agentList:
            #agentList[me.ittr].append(agent.id)
            value = me.prob_calculator.calculateDeltaProbabiliy(me.probabilities[me.ittr],agent.probabilities[me.ittr])
            probDeltaArray.append(value)
            if maxProb<agent.probabilities[me.ittr]:
                maxProb = agent.probabilities[me.ittr]
        
        me.probabilities.append(me.prob_calculator.calculateTotalProbability(me.probabilities[me.ittr],probDeltaArray,maxProb))
        print("agent id ",me.id," ",me.probabilities[0]," probabality : ",me.probabilities[me.ittr+1])


    def doIndividualCalculation(self,me,agent):
        pass

    def doMovement(self,me):
        pass


class QuarantiedBahavior(IAgentBahavior):
    def doProbablityCalculation(self,me,agentList):
        pass


    def doIndividualCalculation(self,me,agent):
        pass
