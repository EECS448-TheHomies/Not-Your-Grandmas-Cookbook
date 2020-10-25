#CookBookClass
#handles interfacing
#contains recipe objects
import yaml
from Recipe import Recipe
class CookBook:

#Function to look up recipes(Project 4)
#Has Recipes
#Loads recipes from files
    def __init__(self):
        self.recipeArr = []


    def loadFile(self,fileLoc):
        with open(fileLoc) as file:

            recipeName = Recipe()
            recipeName.init2(yaml.full_load(file))

        self.recipeArr.append(recipeName)


    def printRecipes(self, recipeName):
        recipeName.printRecipe()
