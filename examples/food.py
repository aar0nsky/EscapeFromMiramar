
class Food:
    
    def __init__(self, name, carbs, fat, prot):
        self.name = name
        self.carbs = carbs
        self.fat = fat
        self.prot = prot
        
    def calories(self):
        carbs = int(self.carbs) * 4
        fat = int(self.fat) * 9
        prot = int(self.prot) * 4
        return carbs + fat + prot

    def __str__(self):
        return self.name


# banana = Food('Banana',25,0,1)
# grapes = Food('Grapes',10,0,0)
# grapesCalories = grapes.calories()
# bananaCalories = banana.calories()
# print("Name\tCalories\tFat\tCarbs\tProtein")
# print("{}\t{}\t\t{}\t{}\t{}".format(banana.name,bananaCalories,banana.fat,banana.carbs,banana.prot))
# print("{}\t{}\t\t{}\t{}\t{}".format(grapes.name,grapesCalories,grapes.fat,grapes.carbs,grapes.prot))
