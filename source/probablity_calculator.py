class ProbabilityCalculator:

    def __init__(self):
        self.transmittingCofficient = 0.1

    def calculateDeltaProbabiliy(self,prob1,prob2):
        #print("calculate probability")
        if prob1>prob2:
            return 0
        else:
            return (prob2-prob1)*self.transmittingCofficient

    def calculateTotalProbability(self,prob1, deltaProbArray,maxProb):
        maxCummulative = maxProb-prob1
        cumulative=0.0
        for delta in deltaProbArray:
            cumulative = delta+cumulative
        
        if maxCummulative< cumulative:
            return maxProb
        else:
            return prob1+cumulative


