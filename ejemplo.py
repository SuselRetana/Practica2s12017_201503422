__author__ = "Mac"

#Si mientras trabajan en Python alguna vez les arroja un "IndentationError" es porque en alguna linea, los tabs al inicio de la sentencia estan erroneos, por ejemplo:
#Esto es valido:
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#		self.password = password
#Esto NO es valido y arroja un "IndentationError":
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#	   self.password = password
#	   ^
#	   Esto no deberia de estar ahi, sino que tiene que estar igual de indentado que las demas sentencias.
#
#
#Recomiendo Sublime Text como IDE
#

from flask import Flask, request, Response
app = Flask("EDD_codigo_ejemplo")
#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
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
			return "DATO SE ENCUENTRA EN EL INDICE : " + str(indice)
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
				while indiceAct==indice:					
					aux=aux.Siguiente
					indiceAct+=1
				sig=aux.Siguiente.Siguiente
				aux.Siguiente=sig
				self.tamano-=1
#Lista clase creada, instancia de lista:
lista=Lista()

class NodoCola(object):
	"""docstring for NodoCola"""
	def __init__(self):
		super(NodoCola, self).__init__()		
		self.Valor=0
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
#Cola clase creada, instancia de Cola:
Cola=Cola()

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
				return("Pila Vacia")
#Pila clase creada, instancia de Pila:
Pila=Pila()


@app.route('/metodoWeb',methods=['POST']) 
def hello():
	parametro = str(request.form['dato'])
	dato2 = str(request.form['dato2'])
	return "Hola User " + str(parametro) + "!"

@app.route('/agregarLista',methods=['POST']) 
def insertarLista():
	parametro = str(request.form['dato'])
	lista.insertar(parametro)
	return "insertado"

@app.route('/BuscarLista',methods=['POST']) 
def BuscarLista():
	parametro = str(request.form['dato'])	
	return lista.buscar(parametro)

@app.route('/EliminarLista',methods=['POST']) 
def EliminarLista():
	parametro = int(request.form['dato'])	
	lista.eliminar(parametro)
	return "Eliminado"


@app.route('/Queue',methods=['POST']) 
def Queue():
	parametro = int(request.form['dato'])	
	Cola.queue(parametro)
	return "insertado"

@app.route('/Dequeue',methods=['POST']) 
def Dequeue():
	parametro = str(request.form['dato'])		
	return "Dato Eliminado : "+str(Cola.dequeue())

@app.route('/Push',methods=['POST']) 
def Push():
	parametro = str(request.form['dato'])	
	Pila.push(parametro)
	return "insertado"

@app.route('/Pop',methods=['POST']) 
def Pop():
	parametro = str(request.form['dato'])		
	return "Dato Eliminado : "+str(Pila.pop())

@app.route("/e")
def hellof():
	return "Hello World2!"
@app.route("/")
def helloa():
	return "Hello World2!"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
