#CookBookClass
#handles interfacing
#contains recipe objects

import os
import spoonacular as sp
import yaml
from Recipe import Recipe
class CookBook:

#Function to look up recipes(Project 4)
#Has Recipes
#Loads recipes from files
    def __init__(self):
        self.api = sp.API('79cd1cbf518f4039988fd991e9977bd8')
        self.recipeArr = []
        self.recipeDir = os.path.expanduser('~') + '\\Documents\\Recipes'          # e.g. C:\\Users\Username\Documents\Recipes
        if not os.path.isdir(self.recipeDir):
            os.makedirs(self.recipeDir)

    def loadFile(self,fileLoc):
    
    # loadFile takes the location to a .yaml file in the form of a string
    
        with open(fileLoc) as file:
            yml = yaml.full_load(file)
            recipeName = Recipe(yml)
            file.close()

        self.recipeArr.append(recipeName)
        
    def loadAllRecipes(self):
        for filename in os.listdir(self.recipeDir):
            try:
                with open(self.recipeDir + '\\' + filename) as file:
                    yml = yaml.full_load(file)
                    self.recipeArr.append(Recipe(yml))
                    file.close()
            except:
                os.remove(self.recipeDir + '\\' + filename)
            
        
    def find_recipes(self, query):
        """
        Searches for a given query and saves results to an array with 10 entries, each entry contains a recipe related 
        to the query with an ID, a title, a link to an image, and the image type located at index 0, 1, 2, and 3, respectively
        Then it loops through the array and makes a call to the API for each index's ID.
        
        Arguments: 
            query (str): Query passed to the API to be searched for
        """
        response = self.api.search_recipes_complex(query)
        results = response.json()['results']
        for i in range(len(results)):
            id = str(results[i]['id'])
            path = 'recipes/' + id + '/information'
            response = self.api._make_request(path)
            res = response.json()
            title = res['title'].replace('/','')
            with open(self.recipeDir + '\\' + title + '.yml', 'w') as file:
                doc = yaml.dump(res, file) 
                file.close()
                


