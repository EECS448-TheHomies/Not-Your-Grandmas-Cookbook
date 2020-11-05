#CookBookClass
#handles interfacing
#contains recipe objects

import yaml
import os
import spoonacular as sp
from Recipe import Recipe
class CookBook:

#Function to look up recipes(Project 4)
#Has Recipes
#Loads recipes from files
    def __init__(self):
        api = sp.API("79cd1cbf518f4039988fd991e9977bd8")
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
        
    def find_recipes(self, query):
        """
        Searches for a given query and returns an array with 10 entries, each entry contains a recipe related 
        to the query with an ID, a title, a link to an image, and the image type located at index 0, 1, 2, and 3, respectively
        
        Arguments: 
            query (str): Query passed to the API to be searched for
        """
        response = self.api.search_recipes_complex(query)
        data = response.json()["results"]
        return data
        
    def save_recipe(self, list, index):
        """
        Saves the given recipe to a yaml file
        
        Arguments: 
            data: A list of recipes that have an ID and title
            index: The index of the desired recipe in the recipe list
        """
        id = str(list[index]["id"])
        response = self.api._make_request("recipes/" + ID + "/information")
        data = response.json()
        with open(self.recipeDir + data["title"], 'w') as file:
            doc = yaml.dump(data, file)
        
        
        

    def printRecipes(self, recipeName):
        recipeName.printRecipe()
