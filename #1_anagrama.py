'''
/*
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
'''

def anagrama(palabra1,palabra2):
    if palabra1==palabra2:
        return False
    letrasPalabra1={}
    letrasPalabra2={}
    
    for letra in palabra1:
        letrasPalabra1[letra] = 0
        letrasPalabra1[letra] = letrasPalabra1[letra]+1
    
    for letra in palabra2:
        letrasPalabra2[letra] = 0
        letrasPalabra2[letra]=letrasPalabra2[letra]+1
              
    if letrasPalabra1==letrasPalabra2:
        return True
    else:
        return False
    
    
print(anagrama("hola","hola"))