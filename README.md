- Contiene atributos privados:
  - "_ancho"
  - "_alto"
- Se implementa encapsulamiento mediante:
  - "@property"
  - "@setter"
- Incluye validaciones:
  - Los valores deben ser mayores que 0
- Métodos:
  - "area()"
  - "perimetro()" (no implementado, se define en las subclases)
  - "__str__()"

Cuadrado

Clase que hereda de "FiguraGeometrica".

- Recibe un solo valor (lado)
- Asigna el mismo valor a ancho y alto
- Sobrescribe:
  - "area()"
  - "perimetro()"
  - "__str__()"

 Rectangulo

Clase que también hereda de "FiguraGeometrica".

- Recibe ancho y alto
- Sobrescribe:
  - "area()"
  - "perimetro()"
  - "__str__()"

 Polimorfismo

Se implementan dos funciones:

- "sumar_areas(figuras)"
- "sumar_perimetros(figuras)"

Estas funciones reciben una lista de objetos y ejecutan los métodos sin importar el tipo de figura, demostrando el uso de polimorfismo.

Ejecución del Programa

El programa principal realiza lo siguiente:

- Crea:
  - 2 cuadrados
  - 2 rectángulos
- Muestra:
  - Área
  - Perímetro
  - Datos de cada objeto
- Realiza:
  - Suma total de áreas y perímetros
- Valida errores:
  - Se intenta asignar un valor inválido para comprobar el encapsulamiento

Ejemplo de Salida

CREANDO FIGURAS

MOSTRAR DATOS 
Cuadrado -> Lado: 4
Área: 16
Perímetro: 16
-----
Rectángulo -> Ancho: 3, Alto: 6
Área: 18
Perímetro: 18
SUMATORIAS (POLIMORFISMO) 
Suma de áreas: 87
Suma de perímetros: 74

PRUEBA DE VALIDACIÓN 
Error detectado: El ancho debe ser mayor que 0

Conclusión

Este taller nos permitió aplicar conceptos clave de la Programación Orientada a Objetos en colab, destacando:

- El uso de encapsulamiento para proteger datos
- La reutilización de código mediante herencia
- La flexibilidad del polimorfismo
- La importancia de validar datos para evitar errores


<img width="1366" height="679" alt="image" src="https://github.com/user-attachments/assets/d1bdea2e-f30b-4f1b-b969-3d21cb48e6a7" />
