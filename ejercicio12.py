# Pida al usuario un número entero, diga si es par o impar,y repita todo lo anterior
#  hasta que el número que se introduzca sea 0.
# (Nota: para saber si un número es par, se mira si el resto de su división entre 2 es 0)

a = int(input("Ingrese un numero "))

if a % 2 == 0:
    print('El número', a, 'es par.')
else:
    print('El número', a, 'es impar.')