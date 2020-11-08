# Recipe.py
# Author: Caleb Bryant
# Date: 10-21-2020

# This class will store elements of recipes, will eventually be configured
# to grab data from an API
# Each individual recipe object will have its own directory stored in the recipes directory of our project folder

import os
import spoonacular
import yaml
from bs4 import BeautifulSoup
import fpdf

class Recipe:
    
    """Recipe stores recipe elements
        def __init__(self): This sets variables within the class to be set to blank, when user wants to manually add ingredients

    Setters:
        Setter methods to set id, time, servings, url, image, summary, ingredients and the instructions
 

    """
    def __init__(self, yml):
        """This constructor takes in a Yaml object, serialization
        
        Variables: 
            recipeDir (str): str holding a path name
            title (str): string that says title of recipe
            id (int): int holding id number of recipe
            time(int): int holding the time it would take to cook
            servings (int): int that says servings made
            URL (str): string holding URL info
            image (str): holds string to path showing image of food
            summary (str): holds summary of food being made
            ingredients (str array): array holding the ingredients used in food 
            instructions (str array): array holding the instructions to make the food

        
        """

    # Constructor that creates an empty recipe
    
        self.recipeDir = os.path.expanduser('~') + '\\Documents\\Recipes'          # e.g. C:\\Users\Username\Documents\Recipes
        self.groceryListDir = os.path.expanduser('~') + '\\Documents\\GroceryLists'          # e.g. C:\\Users\Username\Documents\GroceryLists

        self.title = yml['title']
        self.id = yml['id']
        self.time = yml['readyInMinutes']
        self.servings = yml['servings']
        self.URL = yml['sourceUrl']
        self.image = yml['image']
        soup = BeautifulSoup(yml['summary'], features='html.parser')                    # the BeautifulSoup library removes HTML tags from text
        self.summary = soup.get_text()
        self.ingredients = []                                   # this will be a list of dictionaries that will contain details on the ingredients
        soup = BeautifulSoup(yml['instructions'], features='html.parser')
        instructions = soup.get_text('\n')
        self.instructions = instructions.splitlines()                                  # this will be a list of strings
        
        for i in range(len(yml['extendedIngredients'])):
            name = yml['extendedIngredients'][i]['name']
            amount = str(yml['extendedIngredients'][i]['measures']['us']['amount'])
            unit = yml['extendedIngredients'][i]['measures']['us']['unitShort']
            self.ingredients.append({"name":name, "amount":amount, "unit": unit})
        
    # Setter methods to assign values to member variables after construction
        
    def printIngredientsPDF(self):
        """
        Argument: none
        Action: function that is meant to export a list of ingredients to a PDF.
                A grocery list.
        Returns: The path to the new pdf
        """

        pdf=fpdf.FPDF(format='letter')
        pdf.add_page()
        pdf.set_font("Arial",'BU', size=30)
        pdf.write(20,str("Grocery List For: "+ self.title))
        pdf.ln()

        pdf.set_font("Arial", size=14)

        for i in range(len(self.ingredients)):
            
            pdf.cell(w=4,h=5,border=1)
            pdf.write(6,self.ingredients[i]['name'] + ":\t" +self.ingredients[i]['amount'] + " " +  self.ingredients[i]['unit'])

            # pdf.write(6,str(self.ingredients[i]))
            pdf.ln()

        if not os.path.isdir(self.groceryListDir):
            os.makedirs(self.groceryListDir)
        outputFile = self.groceryListDir+"\\"+self.title+" Grocery List.pdf"
        pdf.output(outputFile)
        return outputFile

