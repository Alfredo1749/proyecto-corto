# Calculadora de ahorros

# Calcula el ahorro total sin intereses
def calcular_sin_interes(ahorro_mensual, años):
    return ahorro_mensual * 12 * años

# Calcula el ahorro total con intereses compuestos
def calcular_con_interes(ahorro_mensual, tasa_anual, años):
    if tasa_anual == 0:  # Si no hay interés, usar la fórmula simple
        return calcular_sin_interes(ahorro_mensual, años)
    r = tasa_anual / 100  # Convertir porcentaje a decimal
    n = 12  # Número de meses en un año
    t = años
    # Fórmula de anualidad para calcular el monto final
    monto = ahorro_mensual * ((1 + r/n) ** (n*t) - 1) / (r/n)
    return monto

# Menú principal del programa
def menu():
    while True:
        print(f"\nCalculadora Financiera de Ahorros\n1. Ingresar datos y calcular plan\n2. Salir")
        opcion = input("Seleccione una opción:\n")

        if opcion == "1":
            try:
                # Solicita el nombre del usuario
                while True:
                    nombre = input("Ingrese su nombre:\n").strip().capitalize()
                    if not nombre:
                        print("Error: Debe ingresar un nombre")
                    else:
                        break   

                # Solicita el ingreso mensual
                while True:
                    try:
                        ingreso = float(input("Ingrese su ingreso mensual:\n"))
                        if ingreso <= 0:
                            print("Error: El ingreso debe ser positivo")
                        else:
                            break
                    except ValueError:
                        print("Error: Debe ingresar un número válido")

                # Solicita el ahorro mensual
                while True:
                    try:
                        ahorro_mensual = float(input("¿Cuánto desea ahorrar cada mes?:\n"))
                        if ahorro_mensual > ingreso:
                            print("\n¡Advertencia!\nEstá intentando ahorrar más de lo que gana.")
                        elif ahorro_mensual == ingreso:
                            print("Está intentando ahorrar lo mismo que gana.")
                        else:
                            break
                    except ValueError:
                        print("Error: Debe ingresar un número válido")

                # Confirmación antes de continuar
                confirmacion = input("¿Está seguro que desea continuar? (s/n):\n").lower().strip()
                if confirmacion != 's':
                    continue  # Regresa al menú principal

                # Solicita la tasa de interés
                while True:
                    try:
                        tasa = float(input("Ingrese la tasa de interés anual (ej. 5 para 5%):\n"))

                        # Calcula el porcentaje del ingreso destinado al ahorro
                        porcentaje_ahorro = (ahorro_mensual / ingreso) * 100  
                        if porcentaje_ahorro > 35:
                            print(f"\nAdvertencia: Su ahorro es {porcentaje_ahorro:.1f}% del ingreso")
                            print("Recomendación: Ahorrar entre 10-30% es lo más saludable")
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número válido")

                # Solicita el número de años
                while True:
                    try:
                        años = int(input("Ingrese el número de años de ahorro:\n"))
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número válido")

                # Realiza los cálculos
                sin_interes = calcular_sin_interes(ahorro_mensual, años)
                con_interes = calcular_con_interes(ahorro_mensual, tasa, años)

                # Muestra los resultados
                print("\n" + "="*50)
                print(f"\tRESUMEN DE AHORRO PARA {nombre.upper()}")
                print("="*50)
                print(f"{'Ingreso mensual:':<25} Q{ingreso:>10,.2f}")
                print(f"{'Ahorro mensual:':<25} Q{ahorro_mensual:>10,.2f}")
                print(f"{'Tasa de interés anual:':<25} {tasa:>10.2f}%")
                print(f"{'Plazo:':<25} {años:>10} años\n")
                print("-"*50)
                print(f"{'Ahorro sin interés:':<25} Q{sin_interes:>10,.2f}")
                print(f"{'Ahorro con interés:':<25} Q{con_interes:>10,.2f}")
                print(f"{'Ganancia por intereses:':<25} Q{con_interes-sin_interes:>10,.2f}")
                print("="*50)

            except ValueError as e:
                print(f"Error: Entrada inválida - {str(e)}")
                continue

        elif opcion == "2":
            print("\nGracias por usar la Calculadora Financiera.\nHasta pronto!")
            break
        else:
            print("Opción inválida. Por favor ingrese 1 o 2")

# Inicia el programa
menu()
