import Calculadora_indices as calc

def ejecutar_calcular_porcentaje_grasa () -> None:
    peso = float(input("ingrese su peso(kg): "))
    altura = float(input("ingrese su altura(m): "))
    edad = int(input("ingrese su edad (años): "))
    valor_genero = float(input("En caso de ser masculino ingrese el valor: 10.8 y en caso de ser femenino ingrese el valor: 0 aqui: "))
    porcentaje_grasa = calc.calcular_porcentaje_grasa (peso, altura, edad, valor_genero)
    print ("Su porcentaje de grasa es: ", porcentaje_grasa, "%")
    
def iniciar_aplicacion() -> None:
    ejecutar_calcular_porcentaje_grasa()
    
iniciar_aplicacion()