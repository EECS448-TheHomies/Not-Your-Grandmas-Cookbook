import PySimpleGUI as sg

from Recipe import Recipe


class RecipeGui(object):
    """
    docstring
    """

    def __init__(self, theme):
        """Sets up the options for the GUI
        docstring
        """

        self.setGUITheme(theme)

        # This prints the debug prints to a window
        sg.Print(do_not_reroute_stdout=False)

    def setGUITheme(self,theme):
        """Set the GUI theme
        """
        self.theme = theme

        # Theme
        sg.theme(theme)

    def run(self):
        """ Runs the GUI

        """

        # Defines the output filed
        frame_layout = [
            [sg.T('Text inside of a frame')],
            [sg.CB('Check 1'), sg.CB('Check 2')],
        ]

        frame = sg.Frame('My Frame Title', frame_layout,
                              font='Any 12', title_color='blue')

        # This defines the layout of the main window
        layout = [[sg.Text('Recipe')],
                  [sg.Button('New Timer')],
                  [frame],
                  [sg.Button('Close')]]

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
