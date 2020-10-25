#CookBookClass
#handles interfacing
#contains recipe objects
import yaml
from Recipe import Recipe
class CookBook:

#Function to look up recipes(Project 4)
#Has Recipes
#Loads recipes from files
	def _init_(self):
		recipeArr = []


def loadFile(self,recipeName,fileName):
	with open(fileName.yaml) as file:

		Recipe recipeName(yaml.load(file,Loader=yaml.FullLoarder))

	self.recipeArr.append(recipeName)


def printRecipes(recipeName):
	recipeName.printRecipe()
