class Resturant():
    def __init__(self, name, food_served):
        self.name = name
        self.food_served = food_served

    def describe_resturant(self):
        print(f'{self.name} serves {self.food_served}.')