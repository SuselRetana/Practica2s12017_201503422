class NodoPila(object):
	"""docstring for NodoCola"""
	def __init__(self):
		super(NodoPila, self).__init__()		
		self.Valor=""
		self.Siguiente=NodoPila

class Pila(object):
	"""docstring for NodoCola"""
	def __init__(self):
		super(Pila, self).__init__()		
		self.Cabeza = None
		self.Fin = None	
		self.tamano = 0

	def push(self, valor):
		nuevo = NodoPila()
		nuevo.Valor = valor						
		if not self.tamano==0:			
			self.Fin=self.Cabeza
			self.Cabeza=nuevo
			self.Cabeza.Siguiente=self.Fin						
		else:
			self.Fin=nuevo
			self.Cabeza=nuevo			
		self.tamano+=1

	def pop(self):
		if not self.tamano==0:
			val=self.Cabeza.Valor			
			self.tamano-=1
			if self.tamano==0:
				self.Fin=None
				self.Cabeza=None
			else:
				self.Cabeza=self.Cabeza.Siguiente			
			return val
		else:
				return("Cola Vacia")

	def imprimir(self):
		aux = self.Cabeza
		while aux != None:
			print(aux.Valor, "_")
			aux = aux.Siguiente
p=Pila()
print p.tamano
p.push("Susel1")
print p.tamano
p.push("Susel2")
print p.tamano
p.push("Susel3")
print p.tamano
p.push("Susel4")
print "_________"
print p.pop()
print p.pop()
print p.pop()
print p.pop()
print p.pop()




				