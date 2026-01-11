import Calculadora_indices as calc
def ejecutar_consumo_calorias_recomendado_para_adelgazar () -> None:
    peso = float(input("ingrese su peso(kg): "))
    altura = float(input("ingrese su altura(cm): "))
    edad = int(input("ingrese su edad(años): "))
    valor_genero = float(input("En caso de ser masculino ingrese el valor: 5 y en caso de ser femenino ingrese el valor: -161 aqui: "))
    calorias_adelgazar = calc.consumo_calorias_recomendado_para_adelgazar (peso, altura, edad, valor_genero)
    print (calorias_adelgazar)
    
def iniciar_aplicacion() -> None:
    ejecutar_consumo_calorias_recomendado_para_adelgazar ()
    
    
iniciar_aplicacion() 