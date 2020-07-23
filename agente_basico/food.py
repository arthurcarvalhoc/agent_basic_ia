class Food():

    def __init__(self):
        self.position = self.new_food()
   

    def new_food(self):
        x = random(800)
        y = random(600)

        return PVector(x,y)


