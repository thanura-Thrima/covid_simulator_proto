import math

class TimeInformer:
    def __init__(self,numberOfTicks):
        self.numberOfTickPerHour = numberOfTicks
        self.numberofTickPerDay =self.numberOfTickPerHour*24 
        self.dayTick=0 #6:00 am
        self.numberOfDayHours=12
        self.eveningTick= self.numberOfTickPerHour*self.numberOfDayHours
        self.days=0
        self.hours=0
        self.isDay= True
        pass

    def update(self,tick):
        dayTick = tick%self.numberofTickPerDay
        self.days = math.floor(tick/self.numberofTickPerDay)
        self.hours = math.floor(dayTick/self.numberOfTickPerHour)
        if(self.hours> self.numberOfDayHours):
            self.isDay = False

