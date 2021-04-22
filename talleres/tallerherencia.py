#punto 1 
class Persona ():
    def __init__ (self,nombreentrada,identrada,edadentrada):
        self.nombre = nombreentrada
        self.id = identrada
        self.edad = edadentrada
    def hablar (self,mensaje):
        print (f'tengo que decir algo',mensaje)
    def caminar (self,pasosentrada):
        self.pasos = pasosentrada
        print (f'he caminado{self.pasos} pasos ')

#punto 2 
class Doctor ():
    def __init__ (self,entradanombre,entradaid,entradaedad,entradaespecialidad):
        self.especialidad = entradaespecialidad
        self.nombre = entradanombre
        self.id = entradaid
        self.edad = entradaedad
    def tratamiento (self,enfermedad):
        print (f'hola soy {self.nombre},mi especialidad es {self.especialidad}, y voy a tratar tu enfermedad {enfermedad}')

geronimo = Doctor ('geronimo',1001370450,27,'neurologia')
geronimo.tratamiento ('neurisma')

#punto 3
class nutricionista (Persona):
    def __init__ (self,entradanombre,entradaid,entradaedad,entradauniversidad):
        persona _init_ (self,entradanombre,entradaid,entradaedad)
        self.universidad = entradauniversidad
    def IMC (self,entradapeso,entradaaltura):
        self.peso = entradapeso
        self.altura = entradaaltura
        IMC = self.peso / (self.altura**2)
        print (f'mi nombre es : {self.nombre},soy nutricionista de la universidad {self.universidad},tu peso es :{self.peso},y tu altura es de :{self.altura},y tu imc es : {IMC}')

#punto 4
class Abogado (Persona):
    def _init_ (self,entradanombre,entradaid,entradaespecialidad,entradaedad,entradauniversidad):
        persona __init__ (self,entradanombre,entradaid,entradaedad)
        self.universidad = entradauniversidad
        self.especialidad = entradaespecialidad
    def representante (self,nombrecliente,entradacaso):
        self.cliente = nombrecliente
        self.caso = entradacaso
        print (f'mi nombre {self.nombre},mi especialidad es {self.especialidad},me gradue {self.universidad},y voy a representar a {self.cliente},en el caso de {self.caso}')
