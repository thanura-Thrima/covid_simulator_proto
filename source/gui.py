from tkinter import *
from thread_gui import ThreadGUI
import threading

class GUI:
    def __init__(self,size_x,size_y):
        self.agentRadius =3
        self.sizeX=size_x
        self.sizeY=size_y
        self.uiThread= ThreadGUI(self)
        self.uiThread.start()
        self.lock = threading.Lock()
        

    def draw(self,arrayAgents,i):
        with self.lock:
            self.canvas.delete("all")
            #print("drawing --------- ",i)
            iteration = "iteration : ",i
            self.canvas.create_text(self.sizeX/2,10,fill="darkblue",font="Times 20 italic bold",text=iteration)
            for elem in arrayAgents:
                x=elem.location.cord[0]
                y=elem.location.cord[1]
                #print("drawing ---------x,y ",x,y)
                color = "#0F0"

                if elem.probabilities[elem.ittr]>.8:
                    color = "#F00"
                elif elem.probabilities[elem.ittr]>.6:
                    color = "#A00"
                elif elem.probabilities[elem.ittr]>.4:
                    color = "#800"
                elif elem.probabilities[elem.ittr]>.2:
                    color = "#080"
                
                self.canvas.create_oval(x-self.agentRadius,y-self.agentRadius,x+self.agentRadius,y+self.agentRadius,fill=color)
          
           # if i%2==0: 
           #     self.root.configure(background="black")
           # else:
           #     self.root.configure(background="white")


    def threadFunc(self):
        self.root=Tk()
        self.root.configure(background="black")
        self.root.title("planogram")
        size = str(self.sizeX)+"x"+str(self.sizeY)
        self.root.geometry(size)
        self.canvas = Canvas(self.root, width=self.sizeX, height=self.sizeY)
        self.canvas.grid(row=0,column=1) 
        self.root.mainloop()

    def join(self):
        self.uiThread.join()