import Calculadora_indices as calc 
def ejecutar_calcular_calorias_en_actividad () -> None:
    peso = float(input("ingrese su peso(kg): "))
    altura = float(input("ingrese su altura(cm): "))
    edad = int(input("ingrese su edad (años): "))
    valor_genero = float(input("En caso de ser masculino ingrese el valor: 5 y en caso de ser femenino ingrese el valor: -161 aqui: "))
    print ("1.2 si hace poco o ningun ejercicio")
    print ("1.375: ejercicio ligero (1 a 3 días a la semana)")
    print ("1.55: ejercicio moderado (3 a 5 días a la semana")
    print ("1.725: deportista (6 -7 días a la semana)")
    print ("1.9: atleta (entrenamientos mañana y tarde)")
    valor_actividad = float(input("Ingrese el valor correspondiente a su actividad fisica: "))
    calorias_actividad = calc.calcular_calorias_en_actividad (peso, altura, edad, valor_genero, valor_actividad)
    print ("tus quema de calorias semanal es: ", calorias_actividad, "cal.")
    
def iniciar_aplicacion () ->None:
    ejecutar_calcular_calorias_en_actividad ()
        
        
iniciar_aplicacion()