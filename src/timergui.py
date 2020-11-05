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
            docstring
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
        t_m, t_s = divmod(seconds, 60)
        t_h, t_m = divmod(t_m, 60)
        time_formated = str(t_h)+":"+str(t_m)+":"+str(t_s)
        return time_formated



