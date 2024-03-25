import random
import string 

from palabras import palabras 
from vidas_dicc_visual import vidas_dicc_visual

def obtener_palabra_valida(lista_palabras):
    # Seleccionar una palabra al azar de la lista de palabras válidas
    palabra = random.choice(lista_palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(lista_palabras)
        
    return palabra.upper()

def ahorcado():

    print("======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado!")
    print("======================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    
    letras_adivinadas = set() 

    abecedario = set(string.ascii_uppercase) # No 'Ñ'
    
    vidas = 7 

    while len(letras_por_adivinar) > 0 and vidas > 0:
        # Letras adivinadas
        # con método .join({'a', 'b', 'c'}) -> 'abc'
        print(f"Te quedan {vidas} intentos de vida.. Y utilizaste las letras: {''.join(letras_adivinadas)}")
        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        
        # Mostrar estado del juego
        print(vidas_dicc_visual[vidas])
        # Mostrar letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        # Si la letra escogida por el usuario está en el abecedario y no está en el
        # conjunto de letras que ya se han ingresado, se añade la letra al conjunto.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si la letra está en la palabra, quitar la letra del conjunto pendiente
            # por adivinar. Si no está en la palabra, quitar la vida al usuario 
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -=1
                print(f"\nTu letra, {letra_usuario} no está en la palabra..")

        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra.. Por favor, escoge una letra nueva..")
        else:
            print("\nEsta letra no es válida..")

    # El juego llega a esta línea cuando se adivinan todas las letras de la palabra o se agotan las vidas
    if vidas == 0:
         print(vidas_dicc_visual[vidas])
         print(f"¡AHORCADO! Perdiste. La palabra era: {palabra}")
    else:
        print(f"¡EXCELENTE! ¡Adivinaste la palabra! {palabra}")

ahorcado()
