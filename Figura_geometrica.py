# CLASE BASE

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        raise NotImplementedError("Debe implementarse en la subclase")

    def __str__(self):
        return f"Figura -> Ancho: {self.ancho}, Alto: {self.alto}"

# CLASE CUADRADO
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)

    @property
    def lado(self):
        return self.ancho

    @lado.setter
    def lado(self, valor):
        self.ancho = valor
        self.alto = valor

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def __str__(self):
        return f"Cuadrado -> Lado: {self.lado}"

# CLASE RECTANGULO
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def __str__(self):
        return f"Rectángulo -> Ancho: {self.ancho}, Alto: {self.alto}"

# FUNCIONES POLIMÓRFICAS

def sumar_areas(figuras):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras):
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total

# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    print("=== CREANDO FIGURAS ===")
    c1 = Cuadrado(4)
    c2 = Cuadrado(5)

    r1 = Rectangulo(3, 6)
    r2 = Rectangulo(2, 7)

    figuras = [c1, c2, r1, r2]

    print("\n=== MOSTRAR DATOS ===")
    for f in figuras:
        print(f)
        print("Área:", f.area())
        print("Perímetro:", f.perimetro())
        print("-----")

    print("\n=== SUMATORIAS (POLIMORFISMO) ===")
    print("Suma de áreas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))

    print("\n=== PRUEBA DE VALIDACIÓN ===")
    try:
        c1.lado = -3
    except ValueError as e:
        print("Error detectado:", e)
