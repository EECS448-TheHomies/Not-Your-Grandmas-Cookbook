# Recipe.py
# Author: Caleb Bryant
# Date: 10-21-2020

# This class will store elements of recipes, will eventually be configured
# to grab data from an API

class Recipe:
    
    def __init__(self):
    
    # Constructor for when we don't have info to put into the recipe at the time of creation
    
    # had a thought of potentially using the no param constructor to call the API
    # but the API call might be better off in a higher level we'll see
    
        self.title = ""
        self.id = ""
        self.time = ""
        self.servings = ""
        self.URL = ""
        self.image = ""
        self.summary = ""
        self.ingredients = []                                   # this will be a list of type ingredients
        self.instructions = []                                  # this will be a list of strings
        
    def __init__(self, title, id, time, servings, URL, image, summary, ingredients, instructions):
    
    # Constructor for when we know what will go in the recipe at time of creation
    
    # Will be used with the API or if we are reading in a recipe txt file before the
    # API is implemented
    
        self.title = title
        self.id = id
        self.time = time
        self.servings = servings
        self.URL = URL
        self.image = image
        self.summary = summary
        self.ingredients = ingredients
        self.instructions = instructions
        
    # Setter methods to assign values to member variables after construction
    
    def setTitle(self, title):
        self.title = title

    def setID(self, id):
        self.id = id
        
    def setTime(self, time):
        self.time = time
        
    def setServings(self, servings):
        self.servings = servings
        
    def setURL(self, url):
        self.url = url
        
    def setImage(self, image):
        self.image = image
        
    def setSummary(self, summary):
        self.summary = summary
        
    # needs to be passed a list
    def setIngredients(self, ingredients):
        self.ingredients = ingredients
    
    # needs to be passed a list
    def setInstructions(self, instructions):
        self.instructions = instructions
    
    
    
    
    
    
    
    
    
    
    