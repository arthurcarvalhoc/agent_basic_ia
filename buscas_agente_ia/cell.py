# A Cell object
class Cell():
    # A cell object knows about its location in the grid 
    # it also knows of its size with the variables x,y,w,h.
    def __init__(self, tempX, tempY, tempW, tempH, cor, type=None):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.h = tempH
        self.type = type
        self.cor = cor

    def display(self):
        #print("vamos preencher")
        #print(self.cor)
        #stroke(0)
        stroke(153, 153, 153)
        
        #stroke(255)
        fill(self.cor[0], self.cor[1], self.cor[2])
        rect(self.x, self.y, self.w, self.h)
