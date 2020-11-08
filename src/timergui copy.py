#author Thomas Atkins and Edwin Recinos
#originally set up to run the script that would pull up the timer
import PySimpleGUI as sg
from datetime import datetime, timedelta 

"""Timer Overview

PySimpleGui used, sg is the class and any method call is sg.___

This script, when run will popup a timer which the user can add/subtract time from. 

Attributes:

    layout (rows of the window layout): 
        sg.Text Sets text so Food timer and the key 'OUTPUT1" is displayed on the counter
        sg.Button() sets buttons titled what is within the parenthesis
            Start starts the counter, Pause pauses, Exit closes the program
            +15mins, -15mins, etc does what it says it does.
        Everything within the brackets is a row.

"""


class TimerGui(object): 

    def __init__(self, theme: str):
            """Sets up the options for the GUI
            
            """

            self.width = 50

            self.theme = theme

            

            # Theme
            sg.theme(theme)



    def make_timer_gui(self) :
        """This function makes the GUI for the timer

        Returns:
            sg.Window: The timer window object
        """
        layout = [
            [sg.Input('Timer Label',font=('Arial',20),size=(25,1))],
            [sg.Text(font=('Arial', 45), size=(10, 1),
                     key='--time--', justification='center')],
            [sg.Button("+5 min"), sg.Button("+1 min"), sg.Button("+30 sec"), sg.VerticalSeparator() ,sg.Button("-5 min"), sg.Button("-1 min"), sg.Button("-30 sec")],
            [sg.Button('Start'),  sg.Button('Pause')]
        ]
       
        self.time_count = datetime.now() + timedelta(minutes=5)
        self.time_timr = True
        self.gui = sg.Window('FOOD TIME!', layout, finalize=True)

    def format_time(self, seconds:int)->str:
        """ This is a helper function to format the timer
        
        Args: 
            seconds (int): the time left on the timer

        Returns:
            str: the formatted string to display on the timer
        """
        print(seconds)
        t_m, t_s = divmod(seconds, 60)
        t_h, t_m = divmod(t_m, 60)
        time_formated = f"{t_h:02}:{t_m:02}:{t_s:02}"
        return time_formated


    

    def updateTimeON(self,min:int = 0 , sec:int = 0):
        self.time_count += timedelta(minutes=min,seconds=sec)
    
    def updateTimeOFF(self,min:int = 0 , sec:int = 0):
        self.timeLeft += timedelta(minutes=min,seconds=sec)


    def eventTimerOff(self,tw_event:str):
        if tw_event == '+5 min':
            self.updateTimeOFF(min=5)

        elif tw_event == '+1 min':
            self.updateTimeOFF(min=1)

        elif tw_event == '+30 sec':
            self.updateTimeOFF(sec=30)

        elif tw_event == '-5 min':
            self.updateTimeOFF(min=-5)

        elif tw_event == '-1 min':
            self.updateTimeOFF(min=-1)

        elif tw_event == '-30 sec':
            self.updateTimeOFF(sec=-30)

        if self.timeLeft.seconds >= 85000 :
            self.timeLeft.seconds = 0
        time_formated = self.format_time(self.timeLeft.seconds)
        self.gui['--time--'](time_formated)

    def eventTimerOn(self,tw_event:str):
        if tw_event == '+5 min':
            self.updateTimeON(min=5)

        elif tw_event == '+1 min':
            self.updateTimeON(min=1)

        elif tw_event == '+30 sec':
            self.updateTimeON(sec=30)

        elif tw_event == '-5 min':
            self.updateTimeON(min=-5)

        elif tw_event == '-1 min':
            self.updateTimeON(min=-1)

        elif tw_event == '-30 sec':
            self.updateTimeON(sec=-30)


        self.timeLeft = self.time_count - datetime.now()
        if self.timeLeft.seconds >= 85000 :
            self.timeLeft.seconds = 0
        time_formated = self.format_time(self.timeLeft.seconds)
        self.gui['--time--'](time_formated)


    def eventHandel(self, tw_event:str):
        if tw_event == 'Start':
            self.time_timr = True
            self.time_count = datetime.now() + self.timeLeft
        elif tw_event == 'Pause':
            self.time_timr = False

        if  self.time_timr == True:         
            self.eventTimerOn(tw_event)
        else:
           self.eventTimerOff(tw_event)