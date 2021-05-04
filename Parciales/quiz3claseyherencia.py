#andres martinez, geronimo buitrago ,maria paula suarez
class ElementosDigitales ():
    def __init__ (self,entradanombre,entradacreador,entradafecha):
        self.nombre = entradanombre
        self.creador = entradacreador
        self.fecha = entradafecha
    def atributos (self):
        print (f'el nombre de la cancion es : {self.nombre}, fue creada por: {self.creador} y se estreno el: {self.fecha}')

elementos = ElementosDigitales ('callaita','bad bunny',2019)
elementos.atributos()


class Pagina ():
    def __init__ (self,TipodeContenidoIn,FormatoIn,FechadePublicacionIn):
        self.contenido = TipodeContenidoIn
        self.Formato = FormatoIn
        self.FechadePublicacion = FechadePublicacionIn
    def mostrar_atributos(self):
        print (f"El tipo de contenido es {self.contenido},en formato {self.Formato} y con fecha de publicacion el {self.FechadePublicacion} ")

pagina1 = Pagina ('musica clasica','MP3',23)
pagina1.mostrar_atributos ()

class Usuario():
    def __init__(self, Nombreentrada, edadentrada, sexoentrada,nacionalidadentrada):
        self.nombre = Nombreentrada
        self.edad = edadentrada
        self.sexo = sexoentrada
        self.nacionalidad = nacionalidadentrada
    

    def mostrarAtibutos(self):
        print(f''' Hola, mi nombre es {self.nombre}
                        Mi edad es {self.edad} años
                        soy del sexo {self.sexo}
                        y mi nacionalidad es {self.nacionalidad}
                        y estoy escuchando musica''')

Usuario1 = Usuario ('Daniel', 27, 'masculino', 'colombiano' )

Usuario1.mostrarAtibutos()


#herencia 
class Cancion (ElementosDigitales):
    def __init__ (self,entradanombre,entradacreador,entradafecha,entradagenero,entradaduracion):
        ElementosDigitales.__init__(self,entradanombre,entradacreador,entradafecha)
        self.duracion = entradaduracion
        self.genero = entradagenero
    def canciomNueva (self,cancionentrada):
        self.cancion = cancionentrada
        print (f'la nueva cancion fue: {self.cancion},fue creada en el 2020')
    def numeroReproducciones (self,numeroreproentrada):
        for i in range (numeroreproentrada):
            print(f'{self.nombre},sonando {i+1} veces')

cancion1 = Cancion ('gods plane ','drake',2018,'rap',4)
cancion1.canciomNueva('november rain')
cancion1.numeroReproducciones (5)

class Artista (Usuario):
    def __init__ (self,nombreentrada,edadentrada,sexoentrada,nacionalidadentrada,generoentrada,numerodecancionesentrada,numerodealbumentrada):
        Usuario.__init__ (self,nombreentrada,edadentrada,sexoentrada,nacionalidadentrada)
        self.genero = generoentrada
        self.numerocanciones = numerodecancionesentrada
        self.album = numerodealbumentrada
    def concierto (self,ciudadentrada):
        self.ciudad = ciudadentrada
        print (f'En la ciudad {self.ciudad},se realizara un concierto')

artista1 = Artista ('drake',34,'masculino','USA','rap',17,5)
artista1.concierto('miami')




