class Asiento:
	colorValido = ["rojo","verde","amarillo","negro","blanco"]
	def __init__(self, color, precio, registro):
		self.color = color
		self.precio = precio
		self.registro = registro

	def cambiarColor(self, color):
		if color in self.colorValido:
			self.color = color

class Auto:
	cantidadCreados = 0
	def __init__(self, modelo, precio, asientos, marca, motor, registro):
		self.modelo = modelo
		self.precio = precio
		self.asientos = asientos
		self.marca = marca
		self.motor = motor
		self.registro = registro

	def cantidadAsientos(self):
		cantidad = 0
		for asiento in self.asientos:
			if (type(asiento) is Asiento):
				cantidad += 1
		return cantidad

	def verificarIntegridad(self):
		integridad = True
		if (self.registro != self.motor.registro):
			integridad = False
		for asiento in self.asientos:
			if (type(asiento) is Asiento):
				if (self.registro != asiento.registro):
					integridad = False

		if integridad:
			return "Auto original"
		else:
			return "Las piezas no son originales"

class Motor:
	def __init__(self, numeroCilindros, tipo, registro):
		self.numeroCilindros = numeroCilindros
		self.tipo = tipo
		self.registro = registro

	def cambiarRegistro(self, registro):
		self.registro = registro

	def asignarTipo(self, tipo):
		tipoValido = ["electrico", "gasolina"]
		if (tipo in self.tipoValido):
			self.tipo = tipo
