#author Thomas Atkins and Edwin Recinos
#originally set up to run the script that would pull up the timer
from threading import Timer
from time import time
import PySimpleGUI as sg
from datetime import date, datetime, timedelta
from PySimpleGUI.PySimpleGUI import _FindElementWithFocusInSubForm

from requests.models import MissingSchema 

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

            self.finish_time = datetime.now() + timedelta(minutes=5)
            self.value = self.finish_time - datetime.now()
            self.active = False
            

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
       
        self.gui = sg.Window('FOOD TIME!', layout, finalize=True)

    def format_time(self, seconds:int)->str:
        """ This is a helper function to format the timer
        
        Args: 
            seconds (int): the time left on the timer

        Returns:
            str: the formatted string to display on the timer
        """
        t_m, t_s = divmod(seconds, 60)
        t_h, t_m = divmod(t_m, 60)
        time_formated = f"{t_h:02}:{t_m:02}:{t_s:02}"
        return time_formated

    def delta_from_event(self, tw_event:str) -> timedelta:
        """ converts the event string into the timedelta

        Args: 
            tw_event: The event string that contains what time the user has requested

        Returns:
            timedelta: the time delta that has been requedted to update the timer with
        """
        if tw_event == '+5 min':
            return timedelta(minutes=5)
        elif tw_event == '+1 min':
            return timedelta(minutes=1)
        elif tw_event == '+30 sec':
            return timedelta(seconds=30)
        elif tw_event == '-5 min':
            return timedelta(minutes=-5)
        elif tw_event == '-1 min':
            return timedelta(minutes=-1)
        elif tw_event == '-30 sec':
            return timedelta(seconds=-30)
        else:
            return timedelta(0)

    def event_handle(self, tw_event:str):
        # print(tw_event)
        if tw_event == 'Start':
            self.active = True
            self.finish_time = datetime.now() + self.value 
        elif tw_event == 'Pause':
            self.active = False
        # print(self.active)

        delta = self.delta_from_event(tw_event)
            
        if self.active:         
            if self.finish_time - datetime.now() < delta:
                self.finish_time = datetime.now()
                self.value = timedelta(0)
            else:
                self.finish_time += delta
                self.value = self.finish_time - datetime.now()
        else:
            if delta > self.value:
                self.value = timedelta(0)
            self.value += self.delta_from_event(tw_event)

        if self.value == timedelta(0):
            self.active=False

        time_formated = self.format_time(self.value.seconds)
        self.gui['--time--'](time_formated)