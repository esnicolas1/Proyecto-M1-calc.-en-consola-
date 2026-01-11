'''
Proyecto M1 del curso "programacion en Python" (univ. de los Andes)
by: Esteban Meza
'''
#Modulo de variables

def calcular_IMC (peso:float, altura:float) -> float:
    return round(peso / altura**2, 2)

def calcular_porcentaje_grasa (peso:float, altura:float, edad:int, valor_genero:float ) -> float:
    return round(1.2 * (peso / (altura**2))+ 0.23 * edad - 5.4 - valor_genero, 2)

def calcular_calorias_en_reposo (peso:float, altura:float, edad:int, valor_genero:int) -> float:
    return round((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero,2)

def calcular_calorias_en_actividad (peso: float, altura:float, edad:int, valor_genero:float, valor_actividad:float) -> float:
    return round(((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero) * valor_actividad, 2)

def consumo_calorias_recomendado_para_adelgazar (peso:float, altura:float, edad:int, valor_genero:float) -> str:
    return "para adelgazar lo recomendado es que consumas un aproximado de: " + str(round(((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero) * 0.8, 2)) + " y " + str(round(((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero) * 0.85, 2)) + " calorias diariamente"