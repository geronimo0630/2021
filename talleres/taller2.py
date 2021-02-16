#----- constantes -----#
PREGUNTA_NUMERO_A = "ingrese numero A: "
PREGUNTA_NUMERO_B = "ingrese numero B: "
RESULTADO_FINAL = "A es mayor a B ?: "

#----- entrada codigo -----#
A = int (input (PREGUNTA_NUMERO_A))
B = int (input (PREGUNTA_NUMERO_B))
isAmayorB = A > B 
print (RESULTADO_FINAL,isAmayorB)
print ("-"*15,"la suma es: ","-"*15)
sumar = A + B
print (sumar)
print ("-"*15,"la resta es: ","-"*15)
restar = A - B
print (restar)
print ("-"*15,"la multiplicacion es: ","-"*15)
multiplicar = A * B
print (multiplicar)
print ("-"*15,"la division es: ","-"*15)
division = A / B
print(division)
print ("-"*15,"el exponente es: ","-"*15)
exponente = A ** B
print (exponente)