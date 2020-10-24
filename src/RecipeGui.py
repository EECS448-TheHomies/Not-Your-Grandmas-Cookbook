from tkinter.constants import TRUE
import PySimpleGUI as sg
import textwrap

from PySimpleGUI.PySimpleGUI import TabGroup
from Recipe import Recipe


class RecipeGui(object):
    """
    docstring
    """

    def __init__(self, theme):
        """Sets up the options for the GUI
        docstring
        """

        self.sectionFont = 'Helvetica 20'
        self.subSectionFont = 'Helvetica 12'
        self.bodyFont = 'Helvetica 10'
        self.width = 125

        self.theme = theme

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

    def run(self):
        """ Runs the GUI

        """

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
        list_col_instructions = []  # Holds the Instruction columns
        state_of_instructions = []  # If the text is hidden
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
            list_col_instructions.append([[elm_state, elm_name], [self.collapse([[elm_details]], '--Step:'+str(step)+':TEXT--') ]] )

            # set the default state to be hidden
            state_of_instructions.append(False)

        instructions_layout = [
            [sg.Text('Instructions', font=self.sectionFont)]]

        for col in list_col_instructions:
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
        window = sg.Window('Window Title', layout, finalize=True)

        while True:
            event, values = window()
            window.Refresh()
            print(event)

            if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
                break
            elif event == 'New Timer':
                print("Make a new Timer")

            for step in range(len(list_col_instructions)):
                if event == '--Step:'+str(step)+':SYM--' or event == '--Step:'+str(step)+':TITLE--':

                    if state_of_instructions[step]:
                        state_of_instructions[step] = False

                        print("Hide Step " + str(step))
                        window['--Step:'+str(step)+':SYM--'](SYMBOL_UP)
                        window['--Step:'+str(step)+':TEXT--'](visible=False)
                        window.Refresh()

                    else:
                        state_of_instructions[step] = True
                        print("Expand Step " + str(step))
                        window['--Step:'+str(step)+':SYM--'](SYMBOL_DOWN)
                        window['--Step:'+str(step)+':TEXT--'](visible=True)
                        window.Refresh()

        window.close()


def wrap(string, lenght=8):
    return '\n'.join(textwrap.wrap(string, lenght))
