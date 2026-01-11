import Calculadora_indices as calc

def ejecutar_calcular_IMC () -> None:
    peso = float(input("Ingresa tu peso(Kg): "))
    altura = float(input("Ingresa tu altura(m): "))
    IMC = calc.calcular_IMC (peso, altura)
    print ("tu IMC es igual a: ", IMC)

def iniciar_aplicacion() -> None:
    ejecutar_calcular_IMC()
    
    
iniciar_aplicacion() 

print ("Si tu IMC posee un valor menor a 16 estas en delgadez severa")
print ("Si tu IMC posee un valor entre 16 y 16.99 estas en delgadez moderada")
print ("Si tu IMC posee un valor entre 17 y 18.49 estas en delgadez aceptable")
print ("Si tu IMC posee un valor entre 18.5 y 24.99 estas en peso normal")
print ("Si tu IMC posee un valor entre 25 y 29.99 estas en sobrepeso")
print ("Si tu IMC posee un valor entre 30 y 34.99 estas en obesidad tipo I")
print ("Si tu IMC posee un valor entre 35 y 39.99 estas en obesidad tipo II")
print ("Si tu IMC posee un valor entre 40 y 49.99 estas en obesidad tipo III o morbida")
print ("Si tu IMC posee un valor mayor a 50 estas en obesidad tipo IV o extrema")