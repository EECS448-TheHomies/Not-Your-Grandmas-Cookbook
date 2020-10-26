#CookBookClass
#handles interfacing
#contains recipe objects
import yaml
import os
from .Recipe import Recipe
class CookBook:

#Function to look up recipes(Project 4)
#Has Recipes
#Loads recipes from files
    def __init__(self):
        self.recipeArr = []
        self.parentDir = (os.getcwd()) + "\\"          # e.g. C:\\Users\Username\ProgramFiles\Project3Folder\
        self.recipeDir = self.parentDir  +"Recipes\\"                 # e.g. C:\\Users\Username\ProgramFiles\Project3Folder\Recipes\


    def loadFile(self,fileLoc):
    
    # loadFile takes the location to a .yaml file in the form of a string
    
        with open(fileLoc) as file:
            yml = yaml.full_load(file)
        recipeName = Recipe()
        recipeName.init2(yml)
        # i = 1
        # while (1):                                                          # Here we are checking if there is a directory in existance, if not make one
        #     if not os.path.isdir(self.recipeDir + yml["title"]):
        #         os.makedirs(self.recipeDir + yml["title"])
        #         recipeName.path = self.recipeDir + yml["title"]
        #         break
        #     elif not os.path.isdir(self.recipeDir + yml["title"] + "(" + str(i) + ")"):
        #         os.makedirs(self.recipeDir + yml["title"] + "(" + str(i) + ")")
        #         recipeName.path = self.recipeDir + yml["title"] + "(" + str(i) + ")"
        #         break
        #     i = i+1
        # os.rename(fileLoc, self.recipeDir + "\\" + os.path.basename(recipeName.path) + "\\" + os.path.basename(fileLoc))
        
        # once the recipe has been created, we know there will be a directory for that recipe in \Recipes
        # so we can move the .yaml file into that directory
        
        

        self.recipeArr.append(recipeName)


    def printRecipes(self, recipeName):
        recipeName.printRecipe()
