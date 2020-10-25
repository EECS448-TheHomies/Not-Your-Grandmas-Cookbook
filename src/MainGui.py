import PySimpleGUI as sg

from RecipeGui import RecipeGui

from CookBook import CookBook
from Recipe import Recipe


class MainGUI(object):
    """
    docstring
    """

    def __init__(self, theme):
        """Sets up the options for the GUI
        docstring
        """

        self.setGUITheme(theme)

        # This prints the debug prints to a window
        # sg.Print(do_not_reroute_stdout=False)

        self.cookbook = CookBook()


        self.cookbook.loadFile(self.cookbook.recipeDir + "t1.yml")
        self.cookbook.loadFile(self.cookbook.recipeDir + "t2.yml")



    def setGUITheme(self, theme):
        """Set the GUI theme
        """
        self.theme = theme

        # Theme
        sg.theme(theme)

    # Make a list of the names of the recipes
    def getRecipeNameList(self, filter: str ) -> list:
        """Gets all the recipes in the Recipes list that contain the search term

        Args:
            filter: The string to search the recipes for. If empty string it will return all.

        Returns:
            The return value. True for success, False otherwise.


        """
        namesOfRecipes = []
        
        for rec in self.cookbook.recipeArr:
            if filter == '' or filter in rec.title:
                namesOfRecipes.append(rec.title)   

        return namesOfRecipes

    def run(self):
        """
        docstring
        """

        # get the recipes

        namesOfRecipes = self.getRecipeNameList('')

        # Make the recipe list element
        self.elmRecipe = sg.Listbox(values=namesOfRecipes, size=(
            60, 10), enable_events=True, key='-recSelect-')

        # Makes cols to justify buttons
        self.colButtons = [[sg.Button('Open'), sg.Button('Exit')]]

        # Defines the output filed
        self.output = sg.Text(size=(12, 1))  # key='-OUTPUT-'

        # This defines the layout of the main window
        layout = [[sg.Text('Your CookBook')],
                  [sg.InputText(key='-recSearch-'), sg.Button('Search'),
                   sg.Radio("local", "r1", default=True)],
                  [self.elmRecipe],
                  [self.output],
                  [sg.Column(self.colButtons, justification='right')]]

        # create the "Window"
        self.window = sg.Window('CookBook', layout, finalize=True)

        while True:
            event, values = self.window()
            self.window.Refresh()
            print(values)

            if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
                break
            elif event == 'Search':
                # window['-OUTPUT-'].update(values['-resSearch-'])
                filtered_recipes = self.getRecipeNameList(
                    values['-recSearch-'])
                print(filtered_recipes)
                self.elmRecipe(filtered_recipes)

            elif event == 'Open':
                print(values['-recSelect-'][0])
                r = Recipe()
                for rec in self.cookbook.recipeArr:
                    print(rec.title)
                    if values['-recSelect-'][0] == rec.title:
                        self.output(rec.title)
                        newGUI = RecipeGui(self.theme, rec)
                        newGUI.run()
                

                pass

        self.window.close()


winGUI = MainGUI('LightGrey1')

winGUI.run()
