from tkinter.constants import TRUE
import PySimpleGUI as sg
import textwrap
from datetime import datetime, timedelta 

from PySimpleGUI.PySimpleGUI import TabGroup
from Recipe import Recipe


class RecipeGui(object):
    """ The class that creates a GUI to display a recipe

    Attributes:
        titleFont (str): font settings for the title
        sectionFont (str): font settings for the section header
        subSectionFont (str): font settings for the subsection header
        bodyFont (str): font settings for the body
        self.width (int): The width of the divider line
        self.recipe (recipe): the recipe object that will be displayed
    """

    def __init__(self, theme: str, recipeOBJ: Recipe):
        """Sets up the options for the GUI
        docstring
        """

        self.titleFont = 'any 25'
        self.sectionFont = 'any 20'
        self.subSectionFont = 'any 12'
        self.bodyFont = 'any 10'
        self.width = 125

        self.theme = theme

        self.recipe = recipeOBJ

        # Theme
        sg.theme(theme)

        # This prints the debug prints to a window
        # sg.Print(do_not_reroute_stdout=False)

    def collapse(self, layout, key):
        """
        Helper function that creates a Column that can be later made hidden, thus appearing "collapsed". Modified from pysimpleGUI cookbook
        Args:
            layout: The layout for the section
            key: Key used to make this seciton visible / invisible
        Returns:
            A pinned column that can be placed directly into your layout
        """
        return sg.pin(sg.Column(layout, key=key, visible=False))

    def make_rec_gui(self) -> sg.Window:
        """ This function creates the window for the recipe

        Returns:
            sg.Window: The recipe window object
        """
        
        SYMBOL_UP = '▲'
        SYMBOL_DOWN = '▼'


        # Defines the summary framed element
        summary_layout = [
            [sg.Text('Summary', font=self.sectionFont, enable_events=True)],
            [sg.T(textwrap.fill(self.recipe.summary, self.width), font=self.bodyFont)],
            [sg.Text('_'*(self.width-18), font=self.bodyFont)]
        ]

        # Defines the Ingredients framed element
        tree_ingredients = sg.TreeData()
        for i in range(len(self.recipe.ingredients)):
            print(self.recipe.ingredients[i])
            tree_ingredients.Insert(
                '', str(i), self.recipe.ingredients[i]['name'], values=[self.recipe.ingredients[i]['amount'], self.recipe.ingredients[i]['unit']])

        ingredients_layout = [
            [sg.Text('Ingredients', font=self.sectionFont)],
            [sg.Tree(data=tree_ingredients,
                     headings=['Amount', 'Unit'],
                     #    auto_size_columns=True,
                     num_rows=5,
                     col0_width=75,
                     show_expanded=False,)],
            [sg.Text('_'*(self.width-18), font=self.bodyFont)]

        ]

        # Defines the Ingredients element
        self.list_col_instructions = []  # Holds the Instruction columns
        self.state_of_instructions = []  # If the text is hidden
        for step in range(len(self.recipe.instructions)):
            name = " Step " + str(step) + ":"
            details = textwrap.fill(self.recipe.instructions[step], self.width)

            elm_state = sg.Text(SYMBOL_UP, key='--Step:' +
                                str(step)+':SYM--', enable_events=True)
            elm_name = sg.Text(name, font=self.subSectionFont,
                               enable_events=True, key='--Step:'+str(step)+':TITLE--')

            elm_details = sg.Text(
                details, font=self.bodyFont)

            # Appended the step to steps list
            self.list_col_instructions.append([[elm_state, elm_name], [
                                              self.collapse([[elm_details]], '--Step:'+str(step)+':TEXT--')]])

            # set the default state to be hidden
            self.state_of_instructions.append(False)

        instructions_layout = [
            [sg.Text('Instructions', font=self.sectionFont)]]

        for col in self.list_col_instructions:
            instructions_layout += col
            pass

        instructions_layout += [[sg.Text('_' *
                                         (self.width-18), font=self.bodyFont)]]

        # Defines the Instructions framed element
        # instructions_layout = [
        #     [sg.T('Text inside of a frame')],
        #     [sg.CB('Check 1'), sg.CB('Check 2')],
        # ]

        # This defines the layout of the main window
        layout = [[sg.Text(self.recipe.title, font=self.titleFont)]]
        layout += summary_layout
        layout += ingredients_layout
        layout += instructions_layout
        layout += [[sg.Button('Close')]]

        # create the "Window"
        return sg.Window(self.recipe.title, layout, finalize=True)

    def make_timer_gui(self) -> sg.Window:
        """This function makes the GUI for the timer

        Returns:
            sg.Window: The timer window object
        """
        layout = [
            [sg.Text('Food timer:', font=('Arial', 20))],
            [sg.Text(font=('Arial', 45), size=(10, 1),
                     key='--time--', justification='center')],
            [sg.Button("+5 min"), sg.Button("+1 min"), sg.Button("+30 sec"), sg.VerticalSeparator() ,sg.Button("-5 min"), sg.Button("-1 min"), sg.Button("-30 sec")],
            [sg.Button('Start'),  sg.Button('Pause')]
        ]
       
        self.time_count = datetime.now() + timedelta(minutes=5)
        self.time_timr = True
        return sg.Window('FOOD TIME!', layout, finalize=True)

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

    def run(self):
        """ This function Runs the GUI

        """

        SYMBOL_UP = '▲'
        SYMBOL_DOWN = '▼'

        time_window = self.make_timer_gui()
        rec_window = self.make_rec_gui()


        while True:
            event, values = rec_window.read(timeout=100)
            tw_event, tw_values = time_window.Read(timeout=100)
            print(event)


            if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
                break
            elif event == 'New Timer':
                print("Make a new Timer")

            for step in range(len(self.list_col_instructions)):
                if event == '--Step:'+str(step)+':SYM--' or event == '--Step:'+str(step)+':TITLE--':

                    if self.state_of_instructions[step]:
                        self.state_of_instructions[step] = False

                        print("Hide Step " + str(step))
                        rec_window['--Step:'+str(step)+':SYM--'](SYMBOL_UP)
                        rec_window['--Step:'+str(step)+':TEXT--'](visible=False)
                        rec_window.Refresh()

                    else:
                        self.state_of_instructions[step] = True
                        print("Expand Step " + str(step))
                        rec_window['--Step:'+str(step)+':SYM--'](SYMBOL_DOWN)
                        rec_window['--Step:'+str(step)+':TEXT--'](visible=True)
                        rec_window.Refresh()

            if tw_event == 'Start':
                self.time_timr = True
                self.time_count = datetime.now() + self.timeLeft

            elif tw_event == 'Pause':
                self.time_timr = False
                
                print(self.timeLeft)



            if  self.time_timr == True:         
                if tw_event == '+5 min':
                    self.time_count += timedelta(minutes=5)

                elif tw_event == '+1 min':
                    self.time_count += timedelta(minutes=1)

                elif tw_event == '+30 sec':
                    self.time_count +=  timedelta(seconds=30)

                elif tw_event == '-5 min':
                    self.time_count -=  timedelta(minutes=5)

                elif tw_event == '-1 min':
                    self.time_count -=  timedelta(minutes=1)

                elif tw_event == '-30 sec':
                    self.time_count -= timedelta(seconds=30)


                self.timeLeft = self.time_count - datetime.now()
                time_formated = self.format_time(self.timeLeft.seconds)
                time_window['--time--'](time_formated)
            

                print(self.time_count - datetime.now())
            else:
                if tw_event == '+5 min':
                    self.timeLeft += timedelta(minutes=5)

                elif tw_event == '+1 min':
                    self.timeLeft += timedelta(minutes=1)

                elif tw_event == '+30 sec':
                    self.timeLeft +=  timedelta(seconds=30)

                elif tw_event == '-5 min':
                    self.timeLeft -=  timedelta(minutes=5)

                elif tw_event == '-1 min':
                    self.timeLeft -=  timedelta(minutes=1)

                elif tw_event == '-30 sec':
                    self.timeLeft -= timedelta(seconds=30)
            
                time_formated = self.format_time(self.timeLeft.seconds)
                time_window['--time--'](time_formated)
        rec_window.close()
        time_window.close()
