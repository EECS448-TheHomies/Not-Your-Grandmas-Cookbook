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
    
    def setTitle(self, title):
        """
        Argument: title (str)
        Action: title setter
        """
        title = str(title)
        i = 1
        while (1):
            if not os.path.isdir(self.recipeDir + '\\' + title + '.yml'):
                os.rename(self.recipeDir + '\\' + self.title, self.recipeDir + '\\' + title + '.yml')
                self.recipeDir = self.recipeDir + + '\\' + title + '.yml'
                break
            elif not os.path.isdir(self.recipeDir + title + "(" + str(i) + ").yml"):
                os.rename(self.recipeDir + '\\' + self.title, self.recipeDir + '\\' + title + "(" + str(i) + ").yml")
                self.recipeDir = self.recipeDir + '\\' + title + "(" + str(i) + ").yml"
                break
            i = i+1
        
    def setTime(self, time):
        """
        Argument: time (int)
        Action: function is a setter to set self.time = time (the argument passed in)
        """
        self.time = time
        
    def setServings(self, servings):
        """
        Argument: servings (int)
        Action: function is a setter to set self.servings = servings (the argument passed in)
        """
        self.servings = servings
        
    def setURL(self, url):
        """
        Argument: url (str)
        Action: function is a setter to set self.url = url (the argument passed in)
        """
        self.url = url
        
    def setImage(self, image):
        """
        Argument: image (str)
        Action: function is a setter to set self.image = image (the argument passed in)
        """
    # contains the path to the image file
        self.image = image
        
    def setSummary(self, summary):
        """
        Argument: summary (str)
        Action: function is a setter to set self.summary = summary (the argument passed in)
        """
        self.summary = summary
        
    # needs to be passed a list
    def setIngredients(self, ingredients):
        """
        Argument: ingredients (str)
        Action: function is a setter to set self.ingredients = ingredients (the argument passed in)
        """
        self.ingredients = ingredients
        
    # needs to be passed a list
    def setInstructions(self, instructions):
        """
        Argument: instructions (str)
        Action: function is a setter to set self.instructions = instructions (the argument passed in)
        """
        self.instructions = instructions
        
    def addIngredient(ingr):
        """
        Argument: ingr (id)
        Action: function that adds ingredient
        """
        self.ingredients.append(ingr)
        
    def removeIngredient(ingr):
        """
        Argument: ingr (int)
        Action: function that removes ingredient
        """
        self.ingredients.remove(ingr)
        
    def addStep(pos, step):
        """
        Arguments: pos (int), step (int)
        Action: function that takes position number and step number of where the new instruction should be added
        """
        self.instructions.insert(pos, step)
        
    def removeStep(pos):
        """
        Argument: pos (int)
        Action: function that removes a step in the instructions
        """
        self.instructions.delete(pos)
        
     
    def printIngredientsPDF(self):
        """
        Argument: none
        Action: function that is meant to export a list of ingredients to a PDF.
                A grocery list.
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
        pdf.output(self.recipeDir+"\\"+self.title+" Grocery List.pdf")

                
        #Needs "pip install fpdf" 

