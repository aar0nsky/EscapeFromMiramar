import food
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
        return ingredient_list



americanCheese = food.Food('American Cheese', 0, 12, 8)
whiteBread = food.Food('White Bread', 190, 2, 6)
butter = food.Food('Butter', 0, 10, 0)
pepperjackCheese = food.Food('PepperJack Cheese', 0, 12,8)

grilledCheese = Recipe('Grilled Cheese', americanCheese, whiteBread, butter)



print("Recipe Name\t\tCalories\tIngredient List")
print(str(grilledCheese) + "\t\t" + str(grilledCheese.calories()) + "\t\t" + str(grilledCheese.buildIngredientList()))