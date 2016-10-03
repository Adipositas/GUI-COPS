# -*- coding: utf-8 -*-
"""
GUI main for recording COPS measurements.
made with tkinter, for interfacing

@author: dnor
"""
import numpy as np
import tkinter as tk

class dataContainer:
    # Class for all data handling and storage
    # Build defs for saving, printing and unit tests
    # name, sex, date, age, hand, ID, feedback
    def __init__(self, inputData):
        self.name = inputData[0]
        self.sex = inputData[1]
        self.date = inputData[2]
        self.age = inputData[3]
        self.hand = inputData[4]
        self.ID = inputData[5]
        self.feedback = inputData[6]
        
    def sessionData(self):
        pass
    
    def saveData(self):
        # Save data as desired
        print("saving session: %s", self.ID)
        
    def testData(self):
        # Testing all data if made correctly and formatted as expected
        error = False
        if type(self.age) != int:
            print("Error. Age is not a number!")
            error = True
        if type(self.ID) != int:
            print("Error. ID is not a number!")
            error = True
        if self.sex not in ["m", "f"]:
            print("Error. Sex is of unknown type")
            error = True
        if self.hand not in ['l', 'r', 'L', 'R']:
            print("Error. Hand is of unknown type")
            error = True
        if self.feedback not in [0, 1]:
            print("Error. Feedback is of unknwon type")
            error = True
            
        if (error):
            return True
            
    def printData(self):
        print("Data added is. \n name: %s \n sex: %s \n date: %s \n age: %i \n hand: %s \n ID: %i \n Feedback: %i" %
              (self.name, self.sex, self.date, self.age, self.hand, self.ID, self.feedback))

# ["Name", "Sex", "Date", "Age", "L/R handed", "ID", "Given Feedback"]
# Data is global, should change to be parsed to classes later, initialized here
fields = ["Name", "Sex", "Date", "Age", "L/R handed", "ID", "Given Feedback"]
dataStandard = ["Carls", "m", "10-11-2015", 23, "L", 21, 1]
data = dataContainer(dataStandard)

class Session(tk.Tk):
    # Buttons for starting or loading sessions
    def __init__(self, frame, _dataFields, record):
        self.frame = frame
        
        # Buttons set-up
        self.button_left = tk.Button(self.frame, text = "Start Session", 
                                     command = lambda: self.startSession(_dataFields, record),
                                     height = 4, width = 40, bg = "green", font = "Arial 15")
        self.button_left.pack(side = "left", fill = "x", expand = True)
                                     
        self.button_middle = tk.Button(self.frame, text = "Load Session", 
                                      command = lambda: self.loadSession, height = 4, width = 40, bg = "yellow",
                                      font = "Arial 15")
        self.button_middle.pack(side = "left", fill = "x", expand = True)
        
        
        self.button_right = tk.Button(self.frame, text = "Stop Session", 
                                      command = lambda: self.stopSession(_dataFields, record),
                                      height = 4, width = 40, bg = "red", font = "Arial 15")
                                      
        self.button_right.pack(side = "left", fill = "x", expand = True)
        self.button_right.config(state = "disabled", bg = "gray")
                
                
    def startSession(self, _dataFields, record):

        _dataFields.setData()
        if (data.testData()):
            # If unit test is not met
            pass
        else:
            data.printData()
            print("Started Session")
            self.button_right.config(state = "normal", bg = "red")
            
            self.button_left.config(state = "disabled", bg = "gray")
            _dataFields.lockFields()
            
            record.setReady()
            
        
        #lambda: controller.show_frame("measurementsWindow")
        
    
    def loadSession(self):
        print("Load Session")
        
    def stopSession(self, _dataFields, record):
        print("Stopping")
        self.button_right.config(state = "disabled", bg = "gray")
        
        self.button_left.config(state = "normal", bg ="green")
        _dataFields.unlockFields()
        
        record.setPassive()
        
        

class DataFields:
    # Data fields below button
    def __init__(self, frame):
        self.frame = tk.Frame()
        
        # Set grid sizing for data entries
        self.frame.columnconfigure(4)
        self.frame.rowconfigure(2)
       # data_fields = ["Name", "Sex", "Age", "something else", "something more"]
        self.entryFields = {}
        
        for i, field in enumerate(fields):
            labelText = tk.StringVar()
            labelText.set(field)
            text = tk.Label(self.frame, text = field, height = 8, font = "Arial 15")
            text.grid(row= 1, column = i)
#       
            self.entryFields[i] = tk.Entry(self.frame, justify = 'center', font = "Arial 15")
            self.entryFields[i].grid(row = 2, column = i)
            self.entryFields[i].insert("end", dataStandard[i])
            
        # Set standard values
            
    def setData(self):
        # Initialize new data with values
        temp = []
        for i, field in enumerate(fields):
            temp.append(self.entryFields[i].get())
        temp = dataContainer(temp)
        if temp.testData():
            temp.testData()
        else:
            # Set as global, should be passed as argument
            global data 
            data = temp
        
    def lockFields(self):
        for i, field in enumerate(fields):
            self.entryFields[i].configure(state = "disabled")
            
    def unlockFields(self):
        for i, field in enumerate(fields):
            self.entryFields[i].configure(state = "normal")
#        
        #self.frame.pack(side = "bottom",expand = True)

class Record:
    def __init__(self):
        self.frame=tk.Frame()
        
        
        self.button_start_record = tk.Button(self.frame, text = "Start Record",
                                       command = self.startRecord, height = 4, width = 40, bg = "gray",
                                       font = "Arial 15")
                                       
        self.button_start_record.config(state = "disabled")
        self.button_start_record.pack(side = "left", fill = "x", expand = True)
        
        self.button_stop_record = tk.Button(self.frame, text = "Stop Record",
                                       command = self.stopRecord, height = 4, width = 40, bg = "gray",
                                       font = "Arial 15")

        self.button_stop_record.config(state = "disabled")                                       
        self.button_stop_record.pack(side = "left", fill = "x", expand = True)
        
        self.recording = False
        
    def setReady(self):
        self.button_start_record.config(state = "normal", bg = "green")
        self.button_start_record.pack(side = "left", fill = "x", expand = True)
        
        self.button_stop_record.configure(bg = "gray")
        self.button_stop_record.config(state = "disabled")
        
    def setPassive(self):
        # If set passive, recordings also needs to stop
        self.stopRecord()        
        
        self.button_start_record.config(state = "disabled", bg = "gray")
        self.button_stop_record.config(state = "disabled", bg = "gray")
        
    def startRecord(self):
        self.recording = True
        # Stuff that happens when recordings are started
        print("record start")
        self.button_start_record.configure(bg = "gray")
        self.button_start_record.config(state = "disabled")
        
        self.button_stop_record.configure(bg = "red")
        self.button_stop_record.config(state = "normal")


        
    def stopRecord(self):
        # Stuff that happens if recordings are stopped
        print("Stopping")
        
        # Make pop-up for case choosing and if successfull or not
        # Check if start record is active (not running if stopped from session)
        if (self.recording == True):
            # make new window
#            pop_root = tk.Tk()
#            pop_root.geometry("1200x1200")
#            app2 = PopUp(pop_root.frame)
            #self.app2 = tk.Toplevel(root)
            self.app2 = PopUp()
            
        self.button_stop_record.configure(bg = "gray")
        self.button_stop_record.config(state = "disabled")
        
        self.button_start_record.configure(bg = "green")
        self.button_start_record.config(state = "normal")
        
        self.recording = False
        

class PopUp:
    def __init__(self):
        self.frame = tk.Tk()
        self.frame.geometry("1200x1200")
        self.frame.protocol('WM_DELETE_WINDOW', self.closeWindow)
        self.frame.grab_set()
        self.buttonQuit = tk.Button(self.frame, text = "quit", command =self.closeWindow, 
                                    height = 4, width = 40, bg ="green", font = "Arial 15")
        self.buttonQuit.pack(side = "top", pady=30)
        
        
    def closeWindow(self):
        # Make underlying window responsive(soon) and destory pop-up
        self.frame.grab_release()
        self.frame.destroy()
        


class PythonGUI(tk.Tk):
    """ Main window of the GUI, contains the sub windows (frames)
    could stack for increased speed - not necessary here.
    """
    def __init__(self):
        self.frame=tk.Frame()

        # Create sub frames first, so they can be passed
        self.subwin = DataFields(self.frame) 
        self.subwin2 = Record()
        
        self.subwin0 = Session(self.frame, self.subwin, self.subwin2)
        
        # Pack datafields on-top
        self.subwin.frame.pack(side="top", pady = 30)
        self.subwin0.frame.pack(side = "top", pady = 50)
                
        self.subwin2.frame.pack(side = "top", pady = 30)
        
    def show_measure(self):
        self.sessionWin.frame.tkraise()
    
      
if __name__ == "__main__":
    root = tk.Tk()
    
    app = PythonGUI()
    
    root.geometry("1650x1000")
    root.mainloop()


