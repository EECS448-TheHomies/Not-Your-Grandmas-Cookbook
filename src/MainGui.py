import PySimpleGUI as sg

from RecipeGui import RecipeGui

from CookBook import CookBook
from Recipe import Recipe


class MainGUI(object):
    """MainGUI Does what it says, it's the main graphic user interface that users use when interacting with the program
    
    """

    def __init__(self, theme):
        """Sets up the options for the GUI
        
        Args:
            theme (str): The theme to set the GUI to  
        """

        self.setGUITheme(theme)

        # This prints the debug prints to a window
        # sg.Print(do_not_reroute_stdout=False)

        self.local = True
        
        self.cookbook = CookBook()
        

        self.cookbook.loadAllRecipes()



    def setGUITheme(self, theme):
        """Set the GUI theme
        
        Args:
            theme (str): The theme to set the GUI to 
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
        """Method that runs the GUI
        """

        # get the recipes

        namesOfRecipes = self.getRecipeNameList('')

        # Make the recipe list element
        self.elmRecipe = sg.Listbox(values=namesOfRecipes, size=(
            72, 10), enable_events=True, key='-recSelect-')

        # Makes cols to justify buttons
        self.colButtons = [[sg.Button('Open'), sg.Button('Exit')]]


        # This defines the layout of the main window
        layout = [[sg.Text('Your CookBook')],
                  [sg.InputText(key='-recSearch-'), sg.Button('Search'),
                   sg.Radio("local", "r1", default=True),sg.Radio("Remote", "r1")],
                  [self.elmRecipe],
                  [sg.Column(self.colButtons, justification='right')]]

        # create the "Window"
        self.window = sg.Window('CookBook', layout, finalize=True)

        while True:
            """While loop run will check for events

                Actions:
                    While Loop: runs until break is detected which is if window is closed or the event hits Exit
                            event in Exit or user closes window then break
                            event in Search, it will search for a recipe list
                            event in Open, opens said recipe list
            """
            event, values = self.window()
            self.window.Refresh()
            print(values)

            if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
                break
            elif event == 'Search':
                filtered_recipes = self.getRecipeNameList(
                    values['-recSearch-'])
                print(filtered_recipes)
                self.elmRecipe(filtered_recipes)

            elif event == 'Open':
                print(values['-recSelect-'][0])
                # r = Recipe()
                for rec in self.cookbook.recipeArr:
                    print(rec.title)
                    if values['-recSelect-'][0] == rec.title:
                        newGUI = RecipeGui(self.theme, rec)
                        newGUI.run()
                

                pass

        self.window.close()


winGUI = MainGUI('LightGrey1')

winGUI.run()
