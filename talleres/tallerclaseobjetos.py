#punto 1

class Torta ():
    def _init_(self,saborentrada,fromaentrada,alturaentrada):

        self.sabor = saborentrada
        self.forma = fromaentrada
        self.altura = alturaentrada
    def atributos (self):
        print(f'hola.mi sabor es {self.sabor} y mi forma es {self.forma} y pot ultimo tngo una altura de {self.altura')

torta1 = torta ('chocolate,','cuadrado',20)
torta1.atributos()

#punto2

class Estudiante ():
    def __init__(self,edadentrada,nombreentrada,identrada,carreraentrada,semestreentrada):
        self.edad = edadentrada
        self.nombre = nombreentrada
        self.id = identrada
        self.carrera = carreraentrada
        self.semestre = semestreentrada
    def queEstudiara (self,materiaentrada,tiempoentrada):
        self.materia = materiaentrada
        self.tiempo = tiempoentrada
        print (f'hola mi nombre es: {self.nombre},y estudiare {self.materia},por {self.tiempo} meses ')

estudiante1 = estudiante (19,'geronimo',1001370320,'ingenieria biomedica', 3)
estudiante1.queEstudiara ('medicina', 12)

#punto 4
class Canguro ():
    def _init_ (self,entradanombre,entradaedad,entradaid):
        self.nombre = entradanombre
        self.edad = entradaedad
        self.identificacion = entradaid
    def saltos (self,numsaltos):
        for i in range (numsaltos):
            print (f'mi nombre es : {self.nombre},hoy he brincado {i+1} saltos')

canguro1 = canguro ('kong',5,20427252)
canguro1 = saltos (5)

#punto 5
class Guitarra():
    def __init__ (self,tiempoentrada,colorentrada,tipoentrada):
        self.tiempo = tiempoentrada
        self. color = colorentrada
        self.tipo = tipoentrada
    def cancion (self,cancion):
        print (f'esta es la cancion {cancion}')

guitarra1 = Guitarra (5,'rojo','electrica')
guitarra1 = cancion ('november rain')
