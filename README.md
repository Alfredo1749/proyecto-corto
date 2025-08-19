# Calculadora de Ahorros

## Descripción del proyecto
Este proyecto es una **Calculadora Financiera de Ahorros** desarrollada en Python.  
Permite al usuario calcular cuánto dinero puede ahorrar en un determinado período de tiempo, considerando **ahorro mensual**, **años de ahorro** y **tasa de interés anual**.  
Además, muestra un **resumen de ahorro**, incluyendo la ganancia por intereses.

---

## Instrucciones de uso
1. Ejecuta el archivo `calculadora.py` con Python 3.
2. En el menú principal, selecciona la opción `1` para ingresar datos y calcular tu plan de ahorro.
3. Ingresa los datos solicitados:
   - Nombre
   - Ingreso mensual
   - Cantidad a ahorrar cada mes
   - Tasa de interés anual (puede ser 0)
   - Número de años que planeas ahorrar
4. Confirma que deseas continuar con el cálculo.
5. Revisa el **resumen de ahorro** que muestra:
   - Ingreso mensual
   - Ahorro mensual
   - Tasa de interés
   - Años de ahorro
   - Total ahorrado sin interés
   - Total ahorrado con interés
   - Ganancia por intereses
6. Para salir del programa, selecciona la opción `2`.

---

## Roles de los integrantes
- **Hervert Alfredo Sales Gomez**: Desarrollo del código y documentación del proyecto.

---

## Problemas encontrados y soluciones
1. **Entrada vacía o incorrecta**: 
   - Problema: El programa fallaba si el usuario ingresaba letras o dejaba campos vacíos.
   - Solución: Se agregaron validaciones con `try/except` para asegurar que solo se ingresen números válidos.

2. **Ahorro mayor al ingreso**: 
   - Problema: El usuario podía intentar ahorrar más de lo que gana.
   - Solución: Se muestra una advertencia y se solicita un ingreso correcto.

3. **Tasa de interés igual a cero**: 
   - Problema: La fórmula de interés compuesto falla si la tasa es 0.
   - Solución: Se agregó un condicional para calcular correctamente el ahorro sin intereses.

4. **Formato de salida desordenado**: 
   - Problema: Los resultados no se veían claros.
   - Solución: Se aplicó formato de columnas y separación de líneas para mejorar la lectura.
