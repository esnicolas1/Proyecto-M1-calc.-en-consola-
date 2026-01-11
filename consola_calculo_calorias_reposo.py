import Calculadora_indices as calc

def ejecutar_calcular_calorias_en_reposo () -> None:
    peso = float(input("ingrese su peso(kg): "))
    altura = float(input("ingrese su altura(cm): "))
    edad = int(input("ingrese su edad (años): "))
    valor_genero = int(input("En caso de ser masculino ingrese el valor: 5 y en caso de ser femenino ingrese el valor: -161 aqui: "))
    calorias_reposo = calc.calcular_calorias_en_reposo (peso, altura, edad, valor_genero) 
    print ("la cantidad de calorías que quemas estando en reposo es: ", calorias_reposo, "cal.")
    
def iniciar_aplicacion () -> None:
    ejecutar_calcular_calorias_en_reposo()
    
    
iniciar_aplicacion()
