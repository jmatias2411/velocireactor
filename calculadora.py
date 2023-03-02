num1 = 8
num2 = 34

def suma(numero1, numero2):
    total = numero1 * numero2
    return total

resultado = suma(num1, num2)
print('La respuesta es: ',resultado)

def notas(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3 
    return suma / 3

clase = int(notas(7, 9, 58))
print("Tu promedio es ", clase)