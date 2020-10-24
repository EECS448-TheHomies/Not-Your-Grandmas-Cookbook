from math import e
import PySimpleGUI as sg
import datetime
import os


# Make a list of the names of the recipes
def getRecipeNameList(filter:str, Recipes:list) -> list:
    """Gets all the recipes in the Recipes list that contain the search term

    Args:
        filter: The string to search the recipes for. If empty string it will return all.
        Recipes: The List of recipe objects.

    Returns:
        The return value. True for success, False otherwise.


    """
    namesOfRecipes = []
    
    for recipe in listOfRecipes:
        if filter == '' or filter in recipe['name']:
            namesOfRecipes.append(recipe['name'])

    return namesOfRecipes







# This prints the debug prints to a window
sg.Print(do_not_reroute_stdout=False)

# Theme
sg.theme('Light grey 1')


# enable_events=True for the table

# get the recipes
listOfRecipes = [{'name':'r1 meat'},{'name':'r2 cheese'}]

namesOfRecipes = getRecipeNameList('', listOfRecipes)

# Make the recipe list element
elmRecipe = sg.Listbox(values=namesOfRecipes, size=(60, 10), enable_events=True, key='-recSelect-')
    
# Defines the output filed
output = sg.Text(size=(12,1) )#key='-OUTPUT-'

# This defines the layout of the main window
layout = [  [sg.Text('Your CookBook')],
            [sg.InputText(key='-recSearch-'), sg.Button('Search'),sg.Radio("local","r1",default=True)],
            [elmRecipe],
            [output],
            [sg.Button('Open') , sg.Button('Exit')] ]




# create the "Window"
window = sg.Window('Window Title', layout,finalize=True)


while True:
    event, values = window()
    window.Refresh() 
    print(values)

    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    elif event == 'Search':
        # window['-OUTPUT-'].update(values['-resSearch-'])
        filtered_recipes = getRecipeNameList(values['-recSearch-'],listOfRecipes)
        print(filtered_recipes)
        elmRecipe( filtered_recipes)

    elif event == 'Open':
        output(values['-recSelect-'])
        pass




window.close()



