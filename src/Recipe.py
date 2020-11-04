# Recipe.py
# Author: Caleb Bryant
# Date: 10-21-2020

# This class will store elements of recipes, will eventually be configured
# to grab data from an API
# Each individual recipe object will have its own directory stored in the recipes directory of our project folder

import os
import spoonacular
import yaml

class Recipe:
    
    """Recipe stores recipe elements
    Constructor count: 4
        def __init__(self): This sets variables within the class to be set to blank, when user wants to manually add ingredients
        def init0(....): is used for project 4 where we will add the integration of an API
        def init1(...): is used before the integration of the API, this will take 
        def init2(...): is a constructor used in serialization


    Setters:
        Setter methods to set id, time, servings, url, image, summary, ingredients and the instructions
 

    """
    def __init__(self):
        """This constructor starts a blank Recipe object, all variables set to blank
        These will be filled in by using the setter methods defined below the constructor, init methods
        
        Variables: 
            path (str): str holding a path name
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
        
    def init0(self, title, id, time, servings, URL, image, summary, ingredients, instructions):
    
        """This constructor is the post API integration, project 4 ready

        Arguments: 
            title (str): string that says title of recipe
            id (int):  int holding id number of recipe
            time(int): int holding the time it would take to cook
            servings (int): int that says servings made
            URL (str): string holding URL info
            image (str): holds string to path showing image of food
            summary (str): holds summary of food being made
            ingredients (str array): array holding the ingredients used in food 
            instructions (str array): array holding the instructions to make the food
        
        """
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

    def init1(self, title, time, servings, summary, ingredients, instructions):
        """This constructor takes in arguments from when object is made

        Arguments: 
            title (str): string that says title of recipe
            time(int): int holding the time it would take to cook
            servings (int): int that says servings made
            summary (str): holds summary of food being made
            ingredients (str array): array holding the ingredients used in food 
            instructions (str array): array holding the instructions to make the food
        
        """
    
    # initializer for when we only know some elements of the recipe (pre API)
        
        self.title = title
        self.time = time
        self.servings = servings
        self.summary = summary
        self.ingredients = ingredients
        self.instructions = instructions
        
    def init2(self, yml):        
        """This constructor takes in a Yaml object, serialization

        Constructor sets self.variables: 
            title (str): string that says title of recipe
            summary (str): holds summary of food being made
            servings (int): int that says servings made
            ingredients (str array): array holding the ingredients used in food 
            instructions (str array): array holding the instructions to make the food
        
        """                                          
    
    # Initializer that takes a yaml object
    # pass in the object that was read from the yaml file
    
        self.title = yml["title"]
        self.summary = yml["summary"]
        self.servings = yml["servings"]
        self.ingredients = yml["ingredients"]                              # a dictionary with the indexes of "name", "amount", & "unit"
        self.instructions = yml["instructions"]                            # a list of strings, each index is a separate step
        i = 1
        
    # Setter methods to assign values to member variables after construction
    
    def setTitle(self, title):
        """
        Argument: title (str)
        Action: title setter
        """
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
        """
        Argument: id (int)
        Action: function is a setter to set self.id = id (the argument passed in)
        """
        self.id = id
        
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
        
   


