class Persona ():
    def __init__(self,nombreEntrada,sexoEntrada,edadEtrada):
        self.nombre = nombreEntrada
        self.id = sexoEntrada
        self.edad = edadEtrada
    def hablar (self,mensaje):
        print (f'tengo una noticia',{mensaje})
persona1 = Persona ('Geronimo','Masculino',20)
persona1.hablar ('hola')

class Doctor (Persona):
    def __init__(self,nombreEntrada, sexoEntrada,edadEtrada):
        Persona.__init__(self,nombreEntrada,sexoEntrada,edadEtrada)

    def IMC (self,entradapeso,entradaAltura):
        self.peso = entradapeso
        self.altura = entradaAltura
        imc = self.peso/self.altura**2
        print (f'mi nombre es {self.nombre} y tu imc es {imc}')

doctor1 = Doctor ('andres','masculino',60)
doctor1.IMC(78,1.80)
