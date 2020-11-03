dolares = input("¿Cuantos dolares tienes?: ") #Pregunto en pantalla 
dolares = float(dolares) #Convierto de texto a doble
valor_peso_mex = 0.047 #Asigno el valor del peso mexicano
pesos = dolares / valor_peso_mex #Hago la conversin de moneda
pesos = round(pesos, 2) #Redondeamos la cantidad a 2 decimales
pesos = str(pesos) #Convertimos la cantidad de doble a string
print("Tienes $" + pesos  + " pesos mexicanos") 