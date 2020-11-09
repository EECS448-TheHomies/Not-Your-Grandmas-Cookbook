import PySimpleGUI as sg
import os
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
        
        self.cookbook.remove_APIrecipes
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
        if not (self.local):
            self.cookbook.find_recipes(filter)
            self.cookbook.loadAllRecipes()

        for rec in self.cookbook.recipeArr:
            filter = filter.casefold()
            tmpTitle = rec.title.casefold()
            if filter == '' or filter  in tmpTitle:
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
        self.colOpen = [[sg.Radio("Dark Mode", "r2",enable_events=True, key='-Dark-'),sg.Radio("Light Mode", "r2", default=True,enable_events=True, key='-Light-'), sg.Button('Open'), sg.Button('Exit')]]


        # This defines the layout of the main window
        layout = [[sg.Text('Your CookBook')],
                  [sg.InputText(key='-recSearch-'), 
                   sg.Radio("local", "r1", default=True,enable_events=True,key='-local-'),sg.Radio("Remote", "r1",enable_events=True, key='-remote-'),sg.Button('Search')],
                  [self.elmRecipe],
                  [sg.Column(self.colOpen, justification='right')],
                  [sg.Button("Test Functionality")]]

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
            # print(event)
            # print(values)

            if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
                break
            elif event == 'Test Functionality':
                os.system("pytest")
            elif event == '-local-':
                self.local = True
            elif event == '-remote-':
                self.local = False
            elif event == 'Search':
                filtered_recipes = self.getRecipeNameList(
                    values['-recSearch-'])
                # print(filtered_recipes)
                self.elmRecipe(filtered_recipes)
            elif event == '-Dark-':
                self.setGUITheme("DarkGrey2")
            elif event == '-Light-':
                self.setGUITheme("LightGrey1")
            elif event == 'Open':
                try:
                    for rec in self.cookbook.recipeArr:
                        # print(rec.title)
                        # print(values['-recSelect-'][0])
                        if values['-recSelect-'][0] == rec.title:
                            newGUI = RecipeGui(self.theme, rec)
                            newGUI.run()
                except:
                    pass                    
                    # r = Recipe()
                    


        self.window.close()


winGUI = MainGUI('LightGrey1')

winGUI.run()
