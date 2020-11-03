def palindromo(palabra):
    palabra = palabra.replace(' ', '')#Reemplazo los caracteres vacios o espacios
    palabra = palabra.lower()#minusculas
    palabra_invert = palabra[::-1]#invierto la palabra
    if palabra == palabra_invert:
        return True
    else:
        return False

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')
            

if __name__ == "__main__": #PointEntry o punto de entrada de un programa de python
    run() #invocacion de la funcion