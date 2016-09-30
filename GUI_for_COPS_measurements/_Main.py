# -*- coding: utf-8 -*-
"""
GUI main for recording COPS measurements.
made with tkinter, for interfacing

@author: dnor
"""
import numpy as np
import tkinter as tk


class Session(tk.Tk):
    # Buttons for starting or loading sessions
    def __init__(self):
        self.frame = tk.Frame()
        
        # Buttons set-up
        self.button_left = tk.Button(self.frame, text = "Start session", 
                                     command = self.startSession, height = 4, width = 40, bg = "green",
                                     font = "Arial 15")
        self.button_left.pack(side = "left", fill = "x", expand = True)
                                     
        self.button_right = tk.Button(self.frame, text = "Load session", 
                                      command = self.loadSession, height = 4, width = 40, bg = "yellow",
                                      font = "Arial 15")
        self.button_right.pack(side = "left", fill = "x", expand = True)
                
        # Stuff for packing frame        
        #self.frame.pack(side = "top", fill ="x", expand = True)
                
#        self.subwin = DataFields()
#        self.subwin.frame.pack(side="top")
        
    def startSession(self):
        print("Started Session")
        
        #lambda: controller.show_frame("measurementsWindow")
        
    
    def loadSession(self):
        print("Load Session")
        
class Sessiontest(tk.Tk):
    # Buttons for starting or loading sessions
    def __init__(self, frame, container):
        self.frame = container
        
        # Buttons set-up
        self.button_left = tk.Button(self.frame, text = "Start session", 
                                     command = self.startSession, height = 4, width = 40, bg = "green",
                                     font = "Arial 15")
        self.button_left.pack(side = "left", fill = "x", expand = True)
                                     
        self.button_right = tk.Button(self.frame, text = "Load session", 
                                      command = self.loadSession, height = 4, width = 40, bg = "yellow",
                                      font = "Arial 15")
        self.button_right.pack(side = "left", fill = "x", expand = True)

        # Stuff for packing frame        
        #self.frame.pack(side = "top", fill ="x", expand = True)
                
#        self.subwin = DataFields()
#        self.subwin.frame.pack(side="top")
        
    def startSession(self):
        print("Started Session")
        
        #lambda: controller.show_frame("measurementsWindow")
        
    
    def loadSession(self):
        print("Load Session")

class DataFields:
    # Data fields below button
    def __init__(self):
        self.frame = tk.Frame()
        
        # Set grid sizing for data entries
        self.frame.columnconfigure(4)
        self.frame.rowconfigure(2)
        data_fields = ["Name", "Sex", "Age", "something else"]
        
        
        for i, field in enumerate(data_fields):
            labelText = tk.StringVar()
            labelText.set(field)
            text = tk.Label(self.frame, text = field, height = 4, font = "Arial 10")
            text.grid(row= 1, column = i)
            #text.pack(side="left")
#            
            self.entry = tk.Entry(self.frame, justify='center')
            self.entry.grid(row = 2, column = i)
#        
        #self.frame.pack(side = "bottom",expand = True)

class measurementsWindow:
    # Frame for showing measurements and such during session
    def __init__(self):
        self.frame = tk.Frame()
        
        self.button_left = tk.Button(self.frame, text = "testing", height = 4, width = 40)
        self.frame.pack(fill = "x", expand = True)
        
        
class measurementsWindowtest:
    # Frame for showing measurements and such during session
    def __init__(self, frame, container):
        self.frame = container
        
        self.button_left = tk.Button(self.frame, text = "testing", height = 4, width = 40)
        self.button_left.pack(fill = "x", expand = True)
        
class PythonGUI(tk.Tk):
    """ Main window of the GUI, contains the sub windows (frames)
    could stack for increased speed - not necessary here.
    """
    def __init__(self):
        # Sub-windows
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
#        # Loop through all windows we have, and stack
#        for F in (Sessiontest, measurementsWindowtest):
#            frame = F(container,self)
#            
#            self.frames[F] = frame
#            
#            frame.grid(row = 0, column = 0)
        
        self.subwin0 = Session()
        self.subwin0.frame.pack(side = "top")
        
        self.subwin = DataFields()
        self.subwin.frame.pack(side="top")
##        
#        self.sessionWin = measurementsWindow()
#        self.sessionWin.frame.pack(side = "top")
        
    def show_measure(self):
        self.sessionWin.frame.tkraise()
    
      
if __name__ == "__main__":
    root = tk.Tk()
    
    app = PythonGUI()
    #sessionFrame = Session()
    #dataFrame = DataFields()
    
    root.geometry("1200x800")
    root.mainloop()


