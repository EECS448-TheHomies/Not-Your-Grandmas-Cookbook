# Ingredient.py
# Author: Caleb Bryant
# Date: 10-21-2020

# This class will store information on individual ingredients

class Ingredient:
    
    """Ingredients class that sets info for meals
    Constructor count: 3
        def __init__(self): This sets variables within the class to be set to blank, when user wants to manually add ingredients
        def init(....): is used for project 4 where we will add the integration of an API
        def init1(...): is used before the integration of the API, this will take 

    Setters:
        Setter methods to set id, aisle, name, amount, unit. 

    """
    def __init__(self):
        """
        This constructor starts an Ingredient object with all variables blank.
        These will be filled in by using the setter methods defined below the constructor, init methods
        
        Variables: 
            id (int): ingredients have a unique integer value
            aisle (string): string that says where ingredient is found
            name (string): name of the ingredient
            amount (int): int that says the amounts being added
            unit (string): indicates what unit of measure is being utilized

        
        """
    
    # Constructor for when we want to manually create an ingredient
    # without pre-existing information
    
        self.id = ""                                    # specific to the Spoontacular API, all ingredients have a unique ID number
        
        self.aisle = ""                                 # where you would find the ingredient in a grocery store e.g. "dairy" or "produce"
        
        self.name = ""                                  # name of ingredient e.g. "milk"
        
        self.amount = ""                                # this will be just a number, e.g. 3 cups of butter -> self.amount = 3
        
        self.unit = ""                                  # e.g. tablespoon, teaspoon, cup, etc.
    
    def init(self, id, aisle, name, amount, unit):
    
        """
        This constructor starts an Ingredient object with variables passed in.
        This constructor is used with the API, for project 4

        Arguments:
            id (int): ingredients have a unique integer value
            aisle (string): string that says where ingredient is found
            name (string): name of the ingredient
            amount (int): int that says the amounts being added
            unit (string): indicates what unit of measure is being utilized
        """
    # Post API initializer
    
        self.id = id
        self.aisle = aisle
        self.name = name
        self.amount = amount
        self.unit = unit
        
    def init1(self, name, amount, unit):
    
        """
        This constructor starts an Ingredient object with variables passed in.
      
        Arguments:
            name (string): name of the ingredient
            amount (int): int that says the amounts being added
            unit (string): indicates what unit of measure is being utilized

        """
    # Pre API initializer
        
        self.name = name
        self.amount = amount
        self.unit = unit
    
    # Setter methods
    
    def setID(self, id):
        """
        Argument: id (int)
        Action: function is a setter to set self.id = id (the argument passed in)
        """
        self.id = id
        
    def setAisle(self, aisle):
        """
        Argument: aisle (int)
        Action: function is a setter to set self.aisle = aisle (the argument passed in)
        """
        self.aisle = aisle
        
    def setName(self, name):
        """
        Argument: name (str)
        Action: function is a setter to set self.name = name (the argument passed in)
        """
        self.name = name
    
    def setAmount(self, amount):
        """
        Argument: amount (str)
        Action: function is a setter to set self.amount = amount (the argument passed in)
        """
        self.amount = amount
    
    def setUnit(self, unit):
        """
        Argument: unit (str)
        Action: function is a setter to set self.unit = unit (the argument passed in)
        """
        self.unit = unit
    
    
    
    
    
    
    
    
    
    