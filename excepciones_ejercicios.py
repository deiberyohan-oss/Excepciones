# ============================================================
#   TALLER DE EXCEPCIONES EN PYTHON
#   Estudiante: Yoan Rodriguez Jimenez
# ============================================================
# EJERCICIO 1: VALIDADOR DE CORREO ELECTRÓNICO
# ============================================================

def validar_correo():
    try:
        correo = input("Ingrese su correo electrónico: ").strip()
        
        if not correo:
            raise ValueError("El campo de correo no puede estar vacío.")
        if "@" not in correo or "." not in correo:
            raise ValueError("Formato inválido. Faltan caracteres obligatorios ('@' o '.').")
            
        print("Correo registrado exitosamente.")
        
    except ValueError as e:
        print(f"Error de validación: {e}")

validar_correo()

# ============================================================
# EJERCICIO 2: INVENTARIO DE ZAPATOS
# ============================================================

inventario = {
    "deportivo": {"blanco": [38, 39, 40], "negro": [40, 41, 42]},
    "casual": {"cafe": [39, 40], "negro": [38, 39, 40, 41]}
}

def buscar_zapato():
    try:
        tipo = input("Ingrese tipo de zapato (deportivo/casual): ").lower().strip()
        color = input("Ingrese color: ").lower().strip()
        talla_str = input("Ingrese la talla: ")
        
        # Esto lanzará ValueError si escriben letras
        talla = int(talla_str) 
        
        # Esto lanzará KeyError si el tipo o color no existen en el diccionario
        tallas_disponibles = inventario[tipo][color] 
        
        if talla in tallas_disponibles:
            print("Sí tenemos ese zapato en inventario.")
        else:
            print("Tenemos el modelo y color, pero esa talla está agotada.")

    except KeyError:
        print("Error: El tipo de zapato o el color solicitado no existe en nuestro catálogo.")
    except ValueError:
        print("Error: La talla debe ser un valor numérico entero.")

buscar_zapato()

# ============================================================
# EJERCICIO 3: CALCULADORA DE EDAD
# ============================================================

from datetime import datetime

def calcular_edad():
    try:
        fecha = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
        nacimiento = datetime.strptime(fecha, "%Y-%m-%d")

        hoy = datetime.now()
        edad = hoy.year - nacimiento.year

        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

    except ValueError:
        print("Formato de fecha incorrecto")
    else:
        print(f"Tienes {edad} años")
    finally:
        print("Proceso terminado")

calcular_edad()

# ============================================================
# EJERCICIO 4: CÁLCULO DE NÓMINA (15 DÍAS)
# ============================================================

def calcular_nomina():
    try:
        sueldo = float(input("Ingrese su sueldo mensual: "))

        if sueldo <= 0:
            raise ValueError("El sueldo debe ser mayor a 0")

        pago_15_dias = sueldo / 2

        auxilio = 162000  # valor aproximado en Colombia
        if sueldo > 2 * 1300000:
            auxilio = 0

        total = pago_15_dias + auxilio

    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Pago 15 días: {pago_15_dias}")
        print(f"Auxilio: {auxilio}")
        print(f"Total a pagar: {total}")

calcular_nomina()
# ============================================================
# EJERCICIO 5: GUARDAR 10 PALABRAS EN UN ARCHIVO .TXT
# ============================================================
def guardar_palabras():
    palabras = []

    try:
        for i in range(10):
            palabra = input(f"Ingrese palabra {i+1}: ")
            palabras.append(palabra)

        archivo = open("palabras.txt", "w")

        for p in palabras:
            archivo.write(p + "\n")

    except FileNotFoundError:
        print("No se pudo crear el archivo")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Palabras guardadas correctamente")
    finally:
        try:
            archivo.close()
        except:
            pass

guardar_palabras()
