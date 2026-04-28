a = 0
b = 0
c = 0
respuesta = ""

def menu():
    print("CALCULADORA EN PYTHON")
    print("Elegí una operación:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
    respuesta = input("")

    if respuesta == "1":
        suma()

    if respuesta == "2":
        resta()

    if respuesta == "3":
        multiplicacion()

    if respuesta == "4":
        division()

def suma():
    print("SUMA")
    a = float(input("Escribí el primero número: "))
    b = float(input("Escribí el segundo número: "))
    c = a + b
    print(f"El resultado de {a:g} + {b:g} es {c:g}")

def resta():
    print("RESTA")
    a = float(input("Escribí el primero número: "))
    b = float(input("Escribí el segundo número: "))
    c = a - b
    print(f"El resultado de {a:g} - {b:g} es {c:g}")

def multiplicacion():
    print("MULTIPLICACIÓN")
    a = float(input("Escribí el primero número: "))
    b = float(input("Escribí el segundo número: "))
    c = a * b
    print(f"El resultado de {a:g} * {b:g} es {c:g}")

def division():
    print("DIVISIÓN")
    a = float(input("Escribí el primero número: "))
    b = float(input("Escribí el segundo número: "))
    c = a / b
    print(f"El resultado de {a:g} / {b:g} es {c:g}")

menu()
