import math

#crear una clase
class Vector:

    #metodo que recibe parametros, facilita inicializacion 
    def inicializa(self,x,y):
        #self variable de instancia
        #colocamos atributos
        self.x = x
        self.y = y

    #creamos otro metodo
    def muestra(self):
        print(self.x, self.y)
    
    #metodo que devuelve un valor
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)


#creamos la instancia}
v1 = Vector()

#llamada al metodo
v1.inicializa(2,5)
v1.muestra()

#obterner magnitud
magnitude = v1.magnitud()
print(magnitude)
