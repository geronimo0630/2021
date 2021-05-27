def validarArchivo (nombreArchivo,descripcion):
    try:
        archivo = open (nombreArchivo)
        return True
    except FileNotFoundError:
        archivo = open (nombreArchivo,'w',encoding='UTF-8')
        print ("2")
        archivo.writelines(descripcion)
        return False

def guardarLinea (nombreArchivo,lineaIn):
    archivo = open (nombreArchivo,'a')
    archivo.writelines(lineaIn)

nameFile = "Pacientes.txt"
isValidate = validarArchivo(nameFile,'Manejo de clientes')
if (isValidate):
    nombrePaciente = input ('ingrese el nombre del paciente: ')
    descPaciente = input ('ingrese descripcion enefermedad: ')
    precio = float(input('ingrese precio de la consulta'))
    linea = 'nombre paciente'+ nombrePaciente + '\ndescripcion'+ descPaciente + 'precio tratamiento' + str(precio)
else:
    print ('se creo el archivo')

