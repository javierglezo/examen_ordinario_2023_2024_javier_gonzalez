from planetas import Planeta, PlanetaConcordia, PlanetaIlum, PlanetaKamino

class EstrellaDeLaMuerte:
    def __init__(self):
        self.volumen = 1000

    def destruir_planeta(self, planeta, volumen):
        if planeta.volumen <= self.volumen:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.volumen -= planeta.volumen
        else:
            print(f"No se puede destruir el planeta {planeta.nombre}. La Estrella de la Muerte no tiene suficiente vida :( ).")


estrella_muerte = EstrellaDeLaMuerte()
planeta_concordia = PlanetaConcordia()
planeta_ilum = PlanetaIlum()
planeta_kamino = PlanetaKamino()


estrella_muerte.destruir_planeta(planeta_concordia)
estrella_muerte.destruir_planeta(planeta_ilum)
estrella_muerte.destruir_planeta(planeta_kamino)

"Faltan las interacciones entre Planetas"

"---------------------------------------------------"



from naves import NavePequena, NaveGrande

class Estrella_y_Aliadas(NaveGrande, NavePequena):
    def __init__(self, nombre, puntos_vida):
        super().__init__(nombre, puntos_vida)

"Falta crear posibilidad de destruir e interaccion con la Estrella"

