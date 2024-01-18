n = int(input("Introducir numero entero mayor a 1 para la pirámide: ").strip())
def escalera(n):
    if n >= 1:
        print("La longitud es válida")
        for i in range(1, n + 1, 2):
            print('#' * i)
    else:
        print("Longitud no válida")
        quit()

escalera(n)
