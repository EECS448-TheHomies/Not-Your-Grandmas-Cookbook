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

    def run(self):
        """ Runs the GUI

        """

        SYMBOL_UP = '▲'
        SYMBOL_DOWN = '▼'

        longtext = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."""
        # Defines the summary framed element
        summary_layout = [
            [sg.Text('Summary', font=self.sectionFont)],
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
        list_col_instructions = []
        for i in range(10):
            name =" Step " + str(i) + ":"
            details = textwrap.fill(longtext, self.width)

            list_col_instructions.append([sg.Column([ [sg.Button(SYMBOL_DOWN, key='--Step'+str(i)+'SYM--'), sg.Text(name, font=self.subSectionFont)], [
                sg.Text(details, font=self.bodyFont,visible=False)]])])

           

            # tmp_layout = [[sg.Text("t", font=self.subSectionFont)]]]
            # list_col_instructions.append(tmp_layout)

        instructions_layout = [
            [sg.Text('Instructions', font=self.sectionFont)]]

        for col in list_col_instructions:
            instructions_layout += [col]
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
            print(values)

            if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
                break
            elif event == 'New Timer':
                print("Make a new Timer")

        window.close()


def wrap(string, lenght=8):
    return '\n'.join(textwrap.wrap(string, lenght))
