# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from vehicle import Vehicle
from food import Food

food = Food()

def setup():
    global v, count, img, f
    size(1024, 768)
    v = Vehicle(width / 2, height / 2)   
    count = 0   
    img = loadImage("pasta.jpg")
    f = createFont("Arial",26)
    
def draw():
    background(127)
    textFont(f,26)            
    fill(0)                       
    text("Comidas coletadas: " + str(v.count),30,30)


    text("Arthur Carvalho " ,800,650)
    text("Danilo Lucena " ,800,700)
    text("Diogenes Emidio " ,800,750)

    if v.is_collected:
       global food 
       food = Food()        
       v.is_collected = False

    # Draw an ellipse at the mouse position
    fill(127)
    #stroke(200)
    #strokeWeight(10)
    #ellipse(food.position.x, food.position.y, 48, 48)
    image(img, food.position.x - 50, food.position.y - 50)

    # Call the appropriate steering behaviors for our agents
    v.seek(food)
    v.update()
    v.display()
