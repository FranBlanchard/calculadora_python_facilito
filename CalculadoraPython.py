#definimos la suma a es el primer numero y b es el segundo numero, devolvemos la suma de a y b
def sumar(a, b):
    return a + b

#definimos la resta a es el primer numero y b es el segundo numero, devolvemos la resta de a y b
def restar(a, b):
    return a - b

#definimos la multiplicación a es el primer numero y b es el segundo numero, devolvemos la multiplicación de a y b
def multiplicar(a, b):
    return a * b

#definimos la división a es el primer numero y b es el segundo numero, devolvemos la división de a y b
def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b

#definimos la potencia a es la base y b es el exponente, devolvemos a elevado a b
def potencia(a, b):
    return a ** b

#definimos la función principal donde mostramos un menú de opciones en un bucle, usando una variable "continuar" como bandera en vez de break, para que el while tenga una sola condición de salida clara
def main():
    continuar = True

    while continuar:
        print("\n=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Salir")

        #pedimos al usuario que elija una opción
        opcion = input("Elige una operación (1-6): ")

        #si elige salir, cambiamos la bandera a False, así el while deja de repetirse en la siguiente vuelta
        if opcion == "6":
            print("¡Hasta luego!")
            continuar = False
        #si la opción no es válida, avisamos y no pedimos números (el else de abajo no se ejecuta)
        elif opcion not in ("1", "2", "3", "4", "5"):
            print("Opción no válida")
        #si la opción es válida, pedimos los dos números y calculamos el resultado
        else:
            #los dejamos en float para poder hacer operaciones con decimales
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            #según la opción elegida, llamamos a la función correspondiente y mostramos el resultado
            if opcion == "1":
                print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado: {restar(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == "4":
                print(f"Resultado: {dividir(num1, num2)}")
            elif opcion == "5":
                print(f"Resultado: {potencia(num1, num2)}")

# llamamos a la función principal para que se ejecute el programa
if __name__ == "__main__":
    main()