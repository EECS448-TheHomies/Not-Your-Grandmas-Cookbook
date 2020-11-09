import os
import pytest
import yaml
from CookBook import CookBook
from Recipe import Recipe
from timergui import TimerGui
from datetime import date, datetime, timedelta

class Test:
        
    def test_1(self):
        """
        Testing init of Recipe
        """
        with open(os.getcwd() + '\\Recipes\\Chicken Burritos.yml') as file:
            yml = yaml.full_load(file)
            file.close()
        rec = Recipe(yml, fromAPI=True)
        assert rec.title == yml['title']
        assert rec.id == yml['id']
        assert rec.time == yml['readyInMinutes']
        assert rec.servings == yml['servings']
        assert rec.URL == yml['sourceUrl']
        assert rec.image == yml['image']
        assert rec.summary != ''
        assert rec.ingredients != []
        assert rec.instructions != ''
        
    def test_2(self):
        """
        Testing loadAllRecipes
        """
        cb = CookBook()
        cb.loadAllRecipes()
        assert len(cb.recipeArr) == len(os.listdir(os.path.expanduser('~') + '\\Documents\\Recipes')) + len(os.listdir(os.path.expanduser('~') + '\\Documents\\APIRecipes'))
    
    def test_3(self):
        """
        Testing loadFile
        """
        cb = CookBook()
        assert len(cb.recipeArr) == 0
        cb.loadFile(os.getcwd() + '\\Recipes\\Chicken Burritos.yml',fromAPI=True)
        assert len(cb.recipeArr) == 1
        
    def test_4(self):
        """
        Testing printIngredientsPDF
        """
        sz = len(os.listdir(os.path.expanduser('~') + '\\Documents\\GroceryLists'))
        with open(os.getcwd() + '\\Recipes\\Chicken Burritos.yml') as file:
            yml = yaml.full_load(file)
            file.close()
        rec = Recipe(yml,fromAPI=True)
        file = rec.printIngredientsPDF()
        assert sz+1 == len(os.listdir(os.path.expanduser('~') + '\\Documents\\GroceryLists'))
        if os.path.exists(file):
            os.remove(file)



    def test_5(self):
        """
        Testing the time function of the timer gui
        """
        timer = TimerGui("Black")
        assert timer.delta_from_event('+5 min') == timedelta(minutes=5)
        assert timer.delta_from_event('+1 min') == timedelta(minutes=1)
        assert timer.delta_from_event('+30 sec') == timedelta(seconds=30)
        assert timer.delta_from_event('-5 min') == timedelta(minutes=-5)
        assert timer.delta_from_event('-1 min') == timedelta(minutes=-1)
        assert timer.delta_from_event('-30 sec') == timedelta(seconds=-30)










