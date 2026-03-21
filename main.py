import sys
# ESTRUCTURA COMPLETA DEL PROGRAMA

def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9 #OPERACIÓN PARA CONVERTIR DE FARENHEIT A CELSIUS

def clasificar(celsius): #FUNCIÓN PARA CLASIFICAR EL TIPO DE TEMPERATURA
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"

def main():
    # Leer y descartar encabezado de entrada
    primera_linea = True
    
    # IMPRIMIR EL ENCABEZADO DE LA SALIDAD
    print("ciudad,temperatura_celsius,clasificacion")
    
    for linea in sys.stdin:
        linea = linea.strip()
        
        # CODIGO PARA SALTARSE LAS LINEAS DEL ENCABEZADO
        if primera_linea:
            primera_linea = False
            continue
        
        # Saltar lineas vacias
        if not linea:
            continue
        
        # DIVIDIR LOS 3 CAMPOS
        partes = linea.split(',')
        if len(partes) != 3:
            continue  # Ignorar linea invalida
        
        ciudad = partes[0]
        temp_str = partes[1]
        unidad = partes[2].strip().upper()
        
        # VALIDAR SI ES UN C O UN F
        if unidad not in ['C', 'F']:
            continue  # Ignorar
        
        # CONVERTIR LA TEMPERATURA
        try:
            temp = float(temp_str)
        except ValueError:
            continue  # Ignorar si no es numero
        
        # UTILIZAR LA FUNCION PARA CONVERTIR A CELSIUS
        if unidad == 'F':
            celsius = fahrenheit_a_celsius(temp)
        else:
            celsius = temp
        
        # CLASIFICAR LOS DATOS E IMPRIMIRLOS
        clasificacion = clasificar(celsius)
        print(f"{ciudad},{celsius:.1f},{clasificacion}")

if __name__ == "__main__":
    main()
