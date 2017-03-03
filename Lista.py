class NodoLista(object):
	"""docstring for NodoCola"""
	def __init__(self):
		super(NodoLista, self).__init__()		
		self.Valor=""
		self.Siguiente=NodoLista
		self.Siguiente=None
class Lista(object):
	"""docstring for Lista"""
	def __init__(self):
		super(Lista, self).__init__()
		self.Inicio=None
		self.tamano=-1

	def esVacia(self):
		return self.Inicio==None

	def insertar(self,Valor):
		nuevo=NodoLista()
		nuevo.Valor=Valor
		if self.esVacia():
			self.Inicio=nuevo
		else:
			aux=self.Inicio
			while aux.Siguiente!=None:							
				aux=aux.Siguiente
			aux.Siguiente=nuevo
		self.tamano+=1

	def buscar(self,referencia):
		indice=0
		aux=self.Inicio
		encontrado=False
		while aux!=None and encontrado!=True:
			print aux.Valor, "__"
			if referencia.lower()==aux.Valor.lower():
				encontrado=True
			else:
				aux=aux.Siguiente
				indice+=1			
		if encontrado==True:
			return "DATO SE ENCUENTRA EN EL INDICE : ",indice
		else:
			return "NO SE ENCONTRO EL DATO"
	
	def eliminar(self,indice):
		indiceAct=0
		aux=self.Inicio
		if indice==0:
			self.Inicio=self.Inicio.Siguiente
			self.tamano-=1
		else:
			if indice==self.tamano:					
				while aux.Siguiente.Siguiente!=None:
					aux=aux.Siguiente					
				aux.Siguiente=None
				self.tamano-=1
			else:
				print"enmedio"
				while indiceAct==indice:					
					aux=aux.Siguiente
					indiceAct+=1
				sig=aux.Siguiente.Siguiente
				aux.Siguiente=sig
				self.tamano-=1