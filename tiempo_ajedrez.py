import time
tiempo_carlsen = 180
tiempo_nakamura = 180
tiempo_movimiento = 10
turno1 = "Carlsen"

def mostrartiempos():
    print(f"tiempo carlsen {tiempo_carlsen}")
    print(f"tiemmpo nakamura {tiempo_nakamura}")

def sintiempo():
    if tiempo_carlsen <= 0:
        print("¡Carlsen se ha quedado sin tiempo! Nakamura gana.") 
    elif tiempo_nakamura <= 0:
        print("¡Nakamura se ha quedado sin tiempo! Carlsen gana.")