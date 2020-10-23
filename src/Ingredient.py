# Ingredient.py
# Author: Caleb Bryant
# Date: 10-21-2020

# This class will store information on individual ingredients

class Ingredient:
    
    def __init__(self):
    
    # Constructor for when we want to manually create an ingredient
    # without pre-existing information
    
        self.id = ""                                    # specific to the Spoontacular API, all ingredients have a unique ID number
        
        self.aisle = ""                                 # where you would find the ingredient in a grocery store e.g. "dairy" or "produce"
        
        self.name = ""                                  # name of ingredient e.g. "milk"
        
        self.amount = ""                                # this will be just a number, e.g. 3 cups of butter -> self.amount = 3
        
        self.unit = ""                                  # e.g. tablespoon, teaspoon, cup, etc.
    
    def __init__(self, id, aisle, name, amount, unit):
    
    # Constructor for when we already have info on the ingredient
    # Used with the API since this information will be given
    
        self.id = id
        self.aisle = aisle
        self.name = name
        self.amount = amount
        self.unit = unit
        
    # Setter methods
    
    def setID(self, id):
        self.id = id
        
    def setAisle(self, aisle):
        self.aisle = aisle
        
    def setName(self, name):
        self.name = name
    
    def setAmount(self, amount):
        self.amount = amount
    
    def setUnit(self, unit):
        self.unit = unit
    
    
    
    
    
    
    
    
    
    