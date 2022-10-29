'''
/*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
'''
def expresionesEquilibradas(string):
    simbolosApertura=['{','[','(']
    simbolosCerradura=['}',']',')']
    porCerrar=[]
    for caracter in string:
        if (caracter in simbolosApertura):
            porCerrar.append(caracter)
        if caracter in simbolosCerradura:
            if len(porCerrar)!=0:
                c = porCerrar.pop()
                if simbolosApertura.index(c)!=simbolosCerradura.index(caracter):
                    return False
            else:
                return False
                
    return True

print(expresionesEquilibradas('{ [ a * ( c + d ) ] - 5 }'))
print(expresionesEquilibradas('{ a * ( c + d ) ] - 5 }'))
print(expresionesEquilibradas('{{{{*))))'))
print(expresionesEquilibradas('(x+1)*{1+1}*{}{}{}{}/()'))
print(expresionesEquilibradas('(x+1)*{1+1}*{]}{}{}{}/()'))

