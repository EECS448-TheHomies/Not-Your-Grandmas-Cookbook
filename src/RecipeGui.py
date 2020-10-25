from tkinter.constants import TRUE
import PySimpleGUI as sg
import textwrap

from PySimpleGUI.PySimpleGUI import TabGroup
from Recipe import Recipe


class RecipeGui(object):
    """
    docstring
    """

    def __init__(self, theme:str, recipeOBJ: Recipe ):
        """Sets up the options for the GUI
        docstring
        """

        self.sectionFont = 'Helvetica 20'
        self.subSectionFont = 'Helvetica 12'
        self.bodyFont = 'Helvetica 10'
        self.width = 125

        self.theme = theme

        self.recipe = recipeOBJ


        # Theme
        sg.theme(theme)

        # This prints the debug prints to a window
        sg.Print(do_not_reroute_stdout=False)


    def collapse(self, layout, key):
        """
        Helper function that creates a Column that can be later made hidden, thus appearing "collapsed". Modified from pysimpleGUI cookbook
        :param layout: The layout for the section
        :param key: Key used to make this seciton visible / invisible
        :return: A pinned column that can be placed directly into your layout
        :rtype: sg.pin
        """
        return sg.pin(sg.Column(layout, key=key, visible=False))

    def make_rec_gui(self):
        SYMBOL_UP = '▲'
        SYMBOL_DOWN = '▼'

        
        longtext = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."""
        # Defines the summary framed element
        summary_layout = [
            [sg.Text('Summary', font=self.sectionFont, enable_events=True)],
            [sg.T(textwrap.fill(longtext, self.width), font=self.bodyFont)],
            [sg.Text('_'*(self.width-18), font=self.bodyFont)]
        ]

        # Defines the Ingredients framed element
        tree_ingredients = sg.TreeData()
        for i in range(10):
            tree_ingredients.Insert(
                '', str(i), "ingredient"+str(i), values=[i])

        ingredients_layout = [
            [sg.Text('Ingredients', font=self.sectionFont)],
            [sg.Tree(data=tree_ingredients,
                     headings=['Amount', ],
                     #    auto_size_columns=True,
                     num_rows=5,
                     col0_width=75,
                     show_expanded=False,)],
            [sg.Text('_'*(self.width-18), font=self.bodyFont)]

        ]

        # Defines the Ingredients framed element
        self.list_col_instructions = []  # Holds the Instruction columns
        self.state_of_instructions = []  # If the text is hidden
        for step in range(10):
            name = " Step " + str(step) + ":"
            details = textwrap.fill(longtext, self.width)

            elm_state = sg.Text(SYMBOL_UP, key='--Step:' +
                                str(step)+':SYM--', enable_events=True)
            elm_name = sg.Text(name, font=self.subSectionFont,
                               enable_events=True, key='--Step:'+str(step)+':TITLE--')

            elm_details = sg.Text(
                details, font=self.bodyFont)

            # Appended the step to steps list
            self.list_col_instructions.append([[elm_state, elm_name], [self.collapse([[elm_details]], '--Step:'+str(step)+':TEXT--') ]] )

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
        layout = [[sg.Text('Recipe')], [sg.Button('New Timer')]]
        layout += summary_layout
        layout += ingredients_layout
        layout += instructions_layout
        layout += [[sg.Button('Close')]]

        # create the "Window"
        return sg.Window('Window Title', layout, finalize=True)

    def make_timer_gui(self):
        layout = [  
            [  sg.Text('Food timer:', font=('Arial', 20)) ],                
            [  sg.Text( font=('Arial', 45), size=(10,1), key='OUTPUT1', justification = 'center') ],
 #         [   sg.Text('Food being cooked: '), sg.Output()],
 #           [  sg.Text('Type something in'), sg.Input()  ], 
            [  sg.Button('Start'),  sg.Button('Pause'), sg.Button('Exit'), sg.Button('Add 15mins'), 
            sg.Button('Subtract 15mins')]  ]                           

        self.time_count=0
        self.time_timr= True
        return sg.Window('FOOD TIME!', layout, finalize=True)
        



    def run(self):
        """ Runs the GUI

        """

        SYMBOL_UP = '▲'
        SYMBOL_DOWN = '▼'

        rec_window = self.make_rec_gui()
        time_window = self.make_timer_gui()

        while True:
            window, event, values = sg.read_all_windows()
            window.Refresh()
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
                        window['--Step:'+str(step)+':SYM--'](SYMBOL_UP)
                        window['--Step:'+str(step)+':TEXT--'](visible=False)
                        window.Refresh()

                    else:
                        self.state_of_instructions[step] = True
                        print("Expand Step " + str(step))
                        window['--Step:'+str(step)+':SYM--'](SYMBOL_DOWN)
                        window['--Step:'+str(step)+':TEXT--'](visible=True)
                        window.Refresh()

            if event in ('Start'):
                self.time_timr = True

            
            elif event in ('Pause'):
                self.time_timr= False


            elif event in ('Add 15mins'):
                if self.time_timr==False:
                    self.time_count=self.time_count+1500
                    window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((self.time_count // 100) // 60, (self.time_count // 100) % 60, self.time_count % 100))
                    
            
            elif event in ('Subtract 15mins'):
                if self.time_timr == False:
                    self.time_count=self.time_count-1500
                    window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((self.time_count // 100) // 60, (self.time_count // 100) % 60, self.time_count % 100))
                    

            if self.time_timr == True:
                window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((self.time_count // 100) // 60, (self.time_count // 100) % 60, self.time_count % 100))
                self.time_count = self.time_count+1

        window.close()


