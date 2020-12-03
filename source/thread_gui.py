import threading

class ThreadGUI(threading.Thread):
    def __init__(self,gui):
        threading.Thread.__init__(self)
        self.gui=gui

    def run(self):
        self.gui.threadFunc()