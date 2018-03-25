
class Person:
    def __init__(self,name,age,favorite_foods):
        self.name = name
        self.age = age
        self.favorite_foods = favorite_foods
    def birth_year(self):
        return 2015 - self.age
    def __str__(self):
       # return "Name: " + self.name \
       # + " Age: " + str(self.age) \
       # + " Favorite food: " + str(self.favorite_foods[0])
        return "Name: {} Age: {} Favorite food: {}".format(self.name, self.age, self.favorite_foods[0])
