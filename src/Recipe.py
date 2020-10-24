# Recipe.py
# Author: Caleb Bryant
# Date: 10-21-2020

# This class will store elements of recipes, will eventually be configured
# to grab data from an API
# Each individual recipe object will have its own directory stored in the recipes directory of our project folder

import os
from Ingredient import Ingredient
import yaml

class Recipe:
    
    def __init__(self):
    
    # Constructor that creates an empty recipe
    
        self.parentDir = os.path.dirname(os.getcwd())           # e.g. C:\\Users\Username\ProgramFiles\Project3Folder
        self.recipeDir = self.parentDir + "/recipes/"           # e.g. C:\\Users\Username\ProgramFiles\Project3Folder\recipes
        self.path = ""                                          # e.g. C:\\Users\Username\ProgramFiles\Project3Folder\recipes\"cake recipe"
        self.title = ""
        self.id = ""
        self.time = ""
        self.servings = ""
        self.URL = ""
        self.image = ""
        self.summary = ""
        self.ingredients = []                                   # this will be a list of dictionaries that will contain details on the ingredients
        self.instructions = []                                  # this will be a list of strings
        
        i = 1
        while (1):                                                          # Here we are checking if there is a directory in existance, if not make one
            if not os.path.isdir(self.recipeDir + "new_recipe"):
                os.makedirs(self.recipeDir + "new_recipe")
                self.path = self.recipeDir + "new_recipe"
                break
            elif not os.path.isdir(self.recipeDir + "new_recipe" + "(" + str(i) + ")"):
                os.makedirs(self.recipeDir + "new_recipe" + "(" + str(i) + ")")
                self.path = self.recipeDir + "new_recipe" + "(" + str(i) + ")"
                break
            i = i+1
        
    def init0(self, title, id, time, servings, URL, image, summary, ingredients, instructions):
    
    # initializer for when we know all elements of the recipe (post API)
    
        self.title = title
        self.id = id
        self.time = time
        self.servings = servings
        self.URL = URL
        self.image = image
        self.summary = summary
        self.ingredients = ingredients
        self.instructions = instructions
        i = 1
        while (1):
            if not os.path.isdir(self.recipeDir + title):
                os.rename(r"" + self.path, r"" + self.recipeDir + title)
                self.path = self.recipeDir + title
                break
            elif not os.path.isdir(self.recipeDir + title + "(" + str(i) + ")"):
                os.rename(r"" + self.path, r"" + self.recipeDir + title + "(" + str(i) + ")")
                self.path = self.recipeDir + title + "(" + str(i) + ")"
                break
            i = i+1

    def init1(self, title, time, servings, summary, ingredients, instructions):
    
    # initializer for when we only know some elements of the recipe (pre API)
        
        self.title = title
        self.time = time
        self.servings = servings
        self.summary = summary
        self.ingredients = ingredients
        self.instructions = instructions
        i = 1
        while (1):
            if not os.path.isdir(self.recipeDir + title):
                os.rename(r"" + self.path, r"" + self.recipeDir + title)
                self.path = self.recipeDir + title
                break
            elif not os.path.isdir(self.recipeDir + title + "(" + str(i) + ")"):
                os.rename(r"" + self.path, r"" + self.recipeDir + title + "(" + str(i) + ")")
                self.path = self.recipeDir + title + "(" + str(i) + ")"
                break
            i = i+1
        
    def init2(self, yml):                                                  # pass in the object that was read from the yaml file
        self.title = yml["title"]
        self.summary = yml["summary"]
        self.servings = yml["servings"]
        self.ingredients = yml["ingredients"]                              # a dictionary with the indexes of "name", "amount", & "unit"
        self.instructions = yml["instructions"]                            # a list of strings, each index is a separate step
        
    # Setter methods to assign values to member variables after construction
    
    def setTitle(self, title):
        self.title = title
        i = 1
        while (1):
            if not os.path.isdir(self.recipeDir + title):
                os.rename(r"" + self.path, r"" + self.recipeDir + title)
                self.path = self.recipeDir + title
                break
            elif not os.path.isdir(self.recipeDir + title + "(" + str(i) + ")"):
                os.rename(r"" + self.path, r"" + self.recipeDir + title + "(" + str(i) + ")")
                self.path = self.recipeDir + title + "(" + str(i) + ")"
                break
            i = i+1
    
    def setID(self, id):
        self.id = id
        
    def setTime(self, time):
        self.time = time
        
    def setServings(self, servings):
        self.servings = servings
        
    def setURL(self, url):
        self.url = url
        
    def setImage(self, image):
    # contains the path to the image file
        self.image = image
        
    def setSummary(self, summary):
        self.summary = summary
        
    # needs to be passed a list
    def setIngredients(self, ingredients):
        self.ingredients = ingredients
        
    # needs to be passed a list
    def setInstructions(self, instructions):
        self.instructions = instructions
        
    def addIngredient(ingr):
        self.ingredients.append(ingr)
        
    def removeIngredient(ingr):
        self.ingredients.remove(ingr)
        
    def addStep(pos, step):
        self.instructions.insert(pos, step)
        
    def removeStep(pos):
        self.instructions.delete(pos)
        
   


