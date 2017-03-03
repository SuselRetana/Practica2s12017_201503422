class NodoCola(object):
	"""docstring for NodoCola"""
	def __init__(self):
		super(NodoCola, self).__init__()		
		self.Valor=""
		self.Siguiente=NodoCola

class Cola(object):
	"""docstring for NodoCola"""
	def __init__(self):
		super(Cola, self).__init__()		
		self.Cabeza = None
		self.Fin = None	
		self.tamano = 0

	def queue(self, valor):
		nuevo = NodoCola()
		nuevo.Valor = valor						
		if not self.tamano==0:
			self.Fin.Siguiente=nuevo
			self.Fin=nuevo
		else:
			self.Cabeza=nuevo
			self.Fin=nuevo
		self.tamano+=1

	def dequeue(self):
		if not self.tamano==0:
			val=self.Cabeza.Valor			
			if self.Cabeza==self.Fin:
				self.Fin=None
				self.Cabeza=None
			else:
				self.Cabeza=self.Cabeza.Siguiente
			self.tamano-=1
			return val
		else:
			return("Cola Vacia")

	def imprimir(self):
		aux = self.Cabeza
		while aux != None:
			print(aux.Valor, "_")
			aux = aux.Siguiente
p=Cola()
p.queue("Susel1")
print p.tamano
p.queue("Susel2")
print p.tamano
p.queue("Susel3")
print p.tamano
p.queue("Susel4")
print p.tamano
p.queue("Susel5")
print p.tamano
print p.dequeue()
print p.tamano
print p.dequeue()
print p.tamano
print p.dequeue()
print p.tamano
print p.dequeue()
print p.tamano
print p.dequeue()
print p.tamano