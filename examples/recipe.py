from food import Food
class Recipe:
    
    def __init__(self, name, *ingredients):
        self.name = name
        self.ingredients = ingredients

    def calories(self):
        totalCalories = 0
        for ingredient in self.ingredients:
            totalCalories = totalCalories + ingredient.calories()
        return totalCalories
        
    def __str__(self):
        return self.name

    def buildIngredientList(self):
        ingredient_list = []
        for ingredient in self.ingredients:
            ingredient_list.append(str(ingredient))
        ingredient_list.sort()
        return ingredient_list



americanCheese = Food('American Cheese', 0, 12, 8)
whiteBread = Food('White Bread', 190, 2, 6)
butter = Food('Butter', 0, 10, 0)
pepperjackCheese = Food('PepperJack Cheese', 0, 12,8)
ham = Food('Deli Ham', 2,0,10)

grilledCheese = Recipe('Grilled Cheese', americanCheese, whiteBread, butter)
hamSandwich = Recipe('Ham Sandwich', whiteBread, ham, pepperjackCheese)

recipes = [grilledCheese, hamSandwich]

def printRecipes(recipes):
    print("Recipe Name\t\tCalories\tIngredient List")
    for recipe in recipes:
        print(str(recipe) + "\t\t" + str(recipe.calories()) + "\t\t" + str(recipe.buildIngredientList()))


printRecipes(recipes)