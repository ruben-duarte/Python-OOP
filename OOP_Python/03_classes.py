import math


class Vector:

    #metodo contstuctor se inicializa atutomaticamente, __new__ es avanzado; __init__ mas usado
    def __init__(self,x,y):
        self.x = x
        self.y = y

        #creamos otro metodo
    def muestra(self):
        print(self.x, self.y)
    
    #metodo que devuelve un valor
    def magnitud(self):
        return round(math.sqrt(self.x**2 + self.y**2),2)

v1 = Vector(8,5)
v1.muestra()
m = v1.magnitud()
print(m)