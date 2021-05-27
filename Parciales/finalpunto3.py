def validateFloat (pregunta):
    iscorrectdata = False
    while (iscorrectdata==False):
        try:
            valor = float (input(pregunta))
            iscorrectdata = True 
        except ValueError:
            print ('ingrese de nuevo los datos')
    return valor

def validateString (pregunta):
    iscorrectdata = False
    while (iscorrectdata==False):
        try:
            valor = input(pregunta)
            assert(valor.isalpha())
            iscorrectdata = True
        except AssertionError:
            print ('ingrese nuevamente los datos')
    return valor

def pedirdatos():
    preguntaNombre = 'ingrese su nombre: '
    preguntaDolar = 'ingrese la cantidad de dolares que va a convertir en euros'
    nombre = validateString (preguntaNombre)
    dolares = validateFloat (preguntaDolar)
    return nombre,dolares



