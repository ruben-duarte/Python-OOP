#crear una clase
class Vector:

    #metodo, siempre lleva self, que es una referencia al llamado del objeto; 
    def inicializa(self):
        #self variable de instancia
        #colocamos atributos
        self.x = 0
        self.y = 0

#creamos la instancia}
v1 = Vector()

#llamada al metodo
v1.inicializa()

#acceder a los atributos
print(v1.x, v1.y)

#cambiar  valor del atributo mediante una asignacion
v1.x = 8

print(v1.x, v1.y)

#crear segundo objeto
v2 = Vector()
v2.inicializa()
print(v2.x, v2.y)

v2.x, v2.y = 3, 7
print(v2.x, v2.y)
print(v1.x, v1.y)

#otra forma de adicionar atributo, usar con cuidado, el atributo no se comparte con la otra instancia
v2.z = 8

print(v2.x, v2.y, v2.z)
print(v1.x, v1.y)