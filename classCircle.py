class Circle:

    def __init__ (self, radius):
        self.radius = radius

    def circumference(self):
      pi = 3.14
      circumferenceValue = pi * self.radius * 2
      return circumferenceValue
    def printCircumference (self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

# Primera instancia de la clase Circle.
circle1 = Circle(4)
# Llame a la PrintCircumference para la clase circle1 instanciada.
circle1.printCircumference()
# Dos instancias más y llamadas a métodos para la clase Circle.
circle2 = Circle(6)
circle2.printCircumference()

circle3 = Circle(10)
circle3.printCircumference()
