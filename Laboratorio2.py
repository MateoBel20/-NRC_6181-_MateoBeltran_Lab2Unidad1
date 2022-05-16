'''Inicio del programa
Se define la función para la resolución de la operación arotmética.'''
def operacion(valor1,valor2):
    division=(valor1+valor2**2)/2.5
    print("La operación aritmética es= (valor1+valor2**2)/2.5 ")
    print("El resultado de la operación aritmética es: " , division)
    return division
'''Se pide y se transforma a valores enteros los string's'''
valor1=int(input("Ingrese la primera cantidad por favor: "))
valor2=int(input("Ingrese la segunda cantidad por favor: "))
'''Se llama a la función '''
operacion(valor1,valor2)
