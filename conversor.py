def conversor(tipo_peso, valor_dollar):
    pesos = input("¿Cuantos pesos " + tipo_peso + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dollar
    dolares = round(dolares, 2) #Redondeamos la cantidad a 2 decimales
    dolares = str(dolares)
    print("Tienes $" + dolares  + " dolares") 

menu = """
Bienvenido al conversor de monedaa ✔

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu)) #Dentro de la variable opcion guardo el numero que se valla a teclear

if opcion == 1:
    conversor('colombianos', 3875)
elif opcion == 2:
    conversor('cargentinos', 65)
elif opcion == 3:
    conversor('mexicanos', 24)
else:
    print('Ingresa una opción correcta por favor')


