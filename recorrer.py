# def run():
#     nombre = input('Escribe tu nombre: ')
#     for letra in nombre: #recorre la variable nombre
#         print(letra)

def run():
    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())

if __name__ == "__main__":
    run()