def planets(p):


    
    planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"] 

    total = 1
    for i in range(1,8):
        total = total + 1
        if p == planets[i]:
            return i + 1

    return p + " is not a planet" 

print(planets("mars"))
