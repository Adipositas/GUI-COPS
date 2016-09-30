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
                                     
        self.button_middle = tk.Button(self.frame, text = "Load session", 
                                      command = self.loadSession, height = 4, width = 40, bg = "yellow",
                                      font = "Arial 15")
        self.button_middle.pack(side = "left", fill = "x", expand = True)
        
        
        self.button_right = tk.Button(self.frame, text = "Load session", 
                                      command = self.stopSession, height = 4, width = 40, bg = "green",
                                      font = "Arial 15")
        self.button_right.pack(side = "left", fill = "x", expand = True)
        self.button_right.config(state = "disabled", bg = "gray")
                
    def startSession(self):
        print("Started Session")
        self.button_right.config(state = "normal", bg = "green")
        
        self.button_left.config(state = "disabled", bg = "gray")
        
        #lambda: controller.show_frame("measurementsWindow")
        
    
    def loadSession(self):
        print("Load Session")
        
    def stopSession(self):
        print("Stopping")
        self.button_right.config(state = "disabled", bg = "gray")
        
        self.button_left.config(state = "normal", bg ="green")

class DataFields:
    # Data fields below button
    def __init__(self):
        self.frame = tk.Frame()
        
        # Set grid sizing for data entries
        self.frame.columnconfigure(4)
        self.frame.rowconfigure(2)
        data_fields = ["Name", "Sex", "Age", "something else", "something more"]
        
        
        for i, field in enumerate(data_fields):
            labelText = tk.StringVar()
            labelText.set(field)
            text = tk.Label(self.frame, text = field, height = 8, font = "Arial 15")
            text.grid(row= 1, column = i)
            #text.pack(side="left")
#       
            self.entry = tk.Entry(self.frame, justify='center', font = "Arial 15")
            self.entry.grid(row = 2, column = i)
            
#        
        #self.frame.pack(side = "bottom",expand = True)

class Record:
    def __init__(self):
        self.frame=tk.Frame()
        
        
        self.button_start_record = tk.Button(self.frame, text = "Start Record",
                                       command = self.startRecord, height = 4, width = 40, bg = "red",
                                       font = "Arial 15")
                                       
        self.button_start_record.pack(side = "left", fill = "x", expand = True)
        
        self.button_stop_record = tk.Button(self.frame, text = "Stop Record",
                                       command = self.stopRecord, height = 4, width = 40, bg = "gray",
                                       font = "Arial 15")

        self.button_stop_record.config(state = "disabled")                                       
        self.button_stop_record.pack(side = "left", fill = "x", expand = True)
        
        
        
    def startRecord(self):
        print("record start")
        self.button_start_record.configure(bg = "gray")
        self.button_start_record.config(state = "disabled")
        
        self.button_stop_record.configure(bg = "red")
        self.button_stop_record.config(state = "normal")


        
    def stopRecord(self):
        print("Stopping")
        self.button_stop_record.configure(bg = "gray")
        self.button_stop_record.config(state = "disabled")
        
        self.button_start_record.configure(bg = "red")
        self.button_start_record.config(state = "normal")
        

class PythonGUI(tk.Tk):
    """ Main window of the GUI, contains the sub windows (frames)
    could stack for increased speed - not necessary here.
    """
    def __init__(self):
        self.subwin0 = Session()
        self.subwin0.frame.pack(side = "top", pady = 50)
        
        self.subwin = DataFields()
        self.subwin.frame.pack(side="top", pady = 30)
        
        self.subwin2 = Record()
        self.subwin2.frame.pack(side = "top", pady = 30)
        
    def show_measure(self):
        self.sessionWin.frame.tkraise()
    
      
if __name__ == "__main__":
    root = tk.Tk()
    
    app = PythonGUI()
    #sessionFrame = Session()
    #dataFrame = DataFields()
    
    root.geometry("1200x800")
    root.mainloop()


