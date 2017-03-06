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

class NodoMatriz(object):
	"""docstring for NodoMatriz"""
	def __init__(self):
		super(NodoMatriz, self).__init__()
		self.Nombre=""
		self.Correo=""
		self.Derecha=None
		self.Izquierda=None
		self.Arriba=None
		self.Abajo=None
		self.ArribaP=None
		self.AbajoP=None

class Matriz(object):
	"""docstring for Matriz"""
	def __init__(self):
		super(Matriz, self).__init__()
		self.Inicio=NodoMatriz()
		self.Inicio.Nombre="0"
		self.Inicio.Correo="0"
	def insertar(self,Nombre,Correo,Letra):
		correo=self.buscar(Correo)
		letra=self.buscar(Letra)
		if correo==None and letra==None:
			self.caso1(Nombre,Correo,Letra)
		elif correo!=None and letra==None:			
			self.caso2(Nombre,correo,Letra)
		elif correo==None and letra!=None:			
			self.caso3(Nombre,Correo,letra)
		elif correo!=None and letra!=None:			
			self.caso4(Nombre,correo,letra)
	
	def buscar(self,Valor):
		encontrado=False
		actual=self.Inicio
		if len(Valor)>1:
			while actual!=None and encontrado==False:
				if actual.Nombre!=Valor:
					actual=actual.Derecha
				else :					
					encontrado=True					
		else :
			while actual!=None and encontrado==False:
				if actual.Nombre!=Valor:
					actual=actual.Abajo
				else :					
					encontrado=True
		return actual

	def caso1(self,Nombre,Correo,Letra):
		correo=NodoMatriz()
		letra=NodoMatriz()
		anadir=NodoMatriz()
		correo.Nombre=Correo
		letra.Nombre=Letra
		anadir.Nombre=Nombre
		anadir.Correo=Correo
		#Anadiendo Correo no Existente
		if self.Inicio.Derecha==None:
			self.Inicio.Derecha=correo
			correo.Izquierda=self.Inicio
		else:	
			aux=self.Inicio
			while aux.Nombre<Correo and aux.Derecha!=None:	
				aux=aux.Derecha			
			if aux.Nombre<Correo:								
				aux.Derecha=correo
				correo.Izquierda=aux
			else :	
				aux.Izquierda.Derecha=correo
				correo.Izquierda=aux.Izquierda
				correo.Derecha=aux
				aux.Izquierda=correo
		#Anadiendo Letra no Existente
		if self.Inicio.Abajo==None:
			self.Inicio.Abajo=letra
			letra.Arriba=self.Inicio
		else:	
			aux=self.Inicio
			while aux.Nombre<Letra and aux.Abajo!=None:	
				aux=aux.Abajo			
			if aux.Nombre<Letra:								
				aux.Abajo=letra
				letra.Arriba=aux
			else :	
				aux.Arriba.Abajo=letra
				letra.Arriba=aux.Arriba
				letra.Abajo=aux
				aux.Arriba=letra
		#Anadiendo Nombre
		correo.Abajo=anadir
		letra.Derecha=anadir
		anadir.Izquierda=letra
		anadir.Arriba=correo

	def caso2(self,Nombre,correo,Letra):		
		letra=NodoMatriz()
		anadir=NodoMatriz()		
		letra.Nombre=Letra
		anadir.Nombre=Nombre
		anadir.Correo=correo.Nombre		
		#Anadiendo Letra no Existente
		if self.Inicio.Abajo==None:
			self.Inicio.Abajo=letra
			letra.Arriba=self.Inicio
		else:	
			aux=self.Inicio
			while aux.Nombre<Letra and aux.Abajo!=None:	
				aux=aux.Abajo			
			if aux.Nombre<Letra:								
				aux.Abajo=letra
				letra.Arriba=aux
			else :	
				aux.Arriba.Abajo=letra
				letra.Arriba=aux.Arriba
				letra.Abajo=aux
				aux.Arriba=letra
			aux=self.Inicio
		#Anadiendo Nombre		
		letra.Derecha=anadir
		anadir.Izquierda=letra		
		#Anadiendo Nodo a Correo correspondiente
		aux=correo.Abajo
		while aux.Nombre<Nombre and aux.Abajo!=None:	
				aux=aux.Abajo		
		if aux.Nombre<Nombre:								
				aux.Abajo=anadir
				anadir.Arriba=aux
		else :	
				aux.Arriba.Abajo=anadir
				anadir.Arriba=aux.Arriba
				anadir.Abajo=aux
				aux.Arriba=anadir		

	def caso3(self,Nombre,Correo,letra):		
		correo=NodoMatriz()
		anadir=NodoMatriz()		
		correo.Nombre=Correo
		anadir.Nombre=Nombre
		anadir.Correo=correo.Nombre		
		#Anadiendo Correo no Existente
		if self.Inicio.Derecha==None:
			self.Inicio.Derecha=correo
			correo.Izquierda=self.Inicio
		else:	
			aux=self.Inicio
			while aux.Nombre<Correo and aux.Derecha!=None:	
				aux=aux.Derecha			
			if aux.Nombre<Correo:								
				aux.Derecha=correo
				correo.Izquierda=aux
			else :	
				aux.Izquierda.Derecha=correo
				correo.Izquierda=aux.Izquierda
				correo.Derecha=aux
				aux.Izquierda=correo
		#Anadiendo Nombre		
		correo.Abajo=anadir		
		anadir.Arriba=correo	
		#Anadiendo Nodo a Letra correspondiente
		aux=letra.Derecha
		while aux.Correo<Correo and aux.Derecha!=None:	
				aux=aux.Derecha		
		if aux.Correo<Correo:								
				aux.Derecha=anadir
				anadir.Izquierda=aux
		else :	
				aux.Izquierda.Derecha=anadir
				anadir.Izquierda=aux.Izquierda
				anadir.Derecha=aux
				aux.Izquierda=anadir
	def caso4(self,Nombre,correo,letra) :				
		anadir=NodoMatriz()
		anadir.Nombre=Nombre
		anadir.Correo=correo.Nombre
		aux3=letra					
		while aux3.Correo<anadir.Correo and aux3.Derecha!=None:
			aux3=aux3.Derecha				
		if aux3.Correo==correo.Nombre :	
			if(aux3!=None) :
				while aux3.AbajoP!=None :	
					aux3=aux3.AbajoP
			aux3.AbajoP=anadir
			anadir.ArribaP=aux3		
		else : 
			if aux3.Correo>anadir.Correo:												
				aux3=aux3.Izquierda
			anadir.Izquierda=aux3
			if(aux3.Derecha!=None):	
				aux3.Derecha.Izquierda=anadir
				anadir.Derecha=aux3.Derecha			
			aux3.Derecha=anadir			
			aux=correo.Abajo
			while aux.Nombre<Nombre and aux.Abajo!=None:	
				aux=aux.Abajo		
			if aux.Nombre<Nombre:								
				aux.Abajo=anadir
				anadir.Arriba=aux
			else :	
				aux.Arriba.Abajo=anadir
				anadir.Arriba=aux.Arriba
				anadir.Abajo=aux
				aux.Arriba=anadir	

	def imprimirL(self,letra) :	
		dominio=""
		act=self.buscar(letra)
		if act!=None:			
			while act.Derecha!=None:
				dominio=dominio+ "["+act.Nombre+"]->"
				if act.AbajoP!=None :	
					dominio=dominio+self.imprimirP(act)
				act=act.Derecha
			dominio=dominio+ "["+act.Nombre+"]->"
			if act.AbajoP!=None :	
				dominio=dominio+self.imprimirP(act)
		else :
			dominio="Letra no Existente"
		return dominio

	def imprimirC(self,correo) :
		dominio=""		
		act=self.buscar(correo)
		if act!=None :			
			while act.Abajo!=None:
				dominio=dominio+ "["+act.Nombre+"]->"
				if act.AbajoP!=None :	
					dominio=dominio+self.imprimirP(act)
				act=act.Abajo
			dominio=dominio+ "["+act.Nombre+"]->"
			if act.AbajoP!=None :	
				dominio=dominio+self.imprimirP(act)			
		else:
			dominio="Correo No Existente"
		return dominio	

	def imprimirP(self,letra) :	
		act=letra.AbajoP		
		encontrado=False
		dominio=""
		while act.AbajoP!=None:			
			dominio=dominio+ "["+act.Nombre+"]->"
			act=act.AbajoP
		dominio=dominio+ "["+act.Nombre+"]->"	
		return dominio	

	def eliminar(self,Nombre,Correo,Letra):
		Eliminar=self.buscar(Letra)
		encontrado=False
		while Eliminar!=None and encontrado==False:
			if Eliminar.Correo==Correo:
				encontrado=True
			else:
				Eliminar=Eliminar.Derecha
		encontrado=False
		if Eliminar.Nombre==Nombre :						
			if Eliminar.AbajoP!=None:							
				Aux2=Eliminar.AbajoP
				Aux2.ArribaP=None				
				Aux2.Arriba=Eliminar.Arriba				
				Aux2.Izquierda=Eliminar.Izquierda
				Eliminar.Izquierda.Derecha=Aux2
				Eliminar.Arriba.Abajo=Aux2
				if Eliminar.Derecha!=None:
					Aux2.Derecha=Eliminar.Derecha
					Eliminar.Derecha.Izquierda=Aux2
				if Eliminar.Abajo!=None:
					Aux2.Abajo=Eliminar.Abajo
					Eliminar.Abajo.Arriba=Aux2	
			else :
				if Eliminar.Derecha!=None:
					Eliminar.Derecha.Izquierda=Eliminar.Izquierda
					Eliminar.Izquierda.Derecha=Eliminar.Derecha
				else :
					Eliminar.Izquierda.Derecha=None
				if Eliminar.Abajo!=None:
					Eliminar.Abajo.Arriba=Eliminar.Arriba
					Eliminar.Arriba.Abajo=Eliminar.Abajo
				else :
					Eliminar.Arriba.Abajo=None
					self.EliminarComp(self.buscar(Letra),self.buscar(Correo))	
			Eliminar=None
		else :	
			while Eliminar.AbajoP!=None and encontrado==False:
				Eliminar=Eliminar.AbajoP
				if Eliminar.Nombre==Nombre:
					encontrado=True
			if Eliminar.AbajoP!=None:
				Eliminar.ArribaP.AbajoP=Eliminar.AbajoP
				Eliminar.AbajoP.ArribaP=Eliminar.ArribaP
			else:	
				Eliminar.ArribaP.AbajoP=None
				Eliminar.ArribaP=None
			Eliminar=None				
	
	def EliminarComp(self,Letra,Correo):
		if Letra.Derecha==None:
			if Letra.Abajo!=None:
				Letra.Arriba.Abajo=Letra.Abajo
				Letra.Abajo.Arriba=Letra.Arriba
			else:	
				Letra.Arriba.Abajo=None			
			Letra=None
		if Correo.Abajo==None:
			if Correo.Derecha!=None:
				Correo.Izquierda.Derecha=Correo.Derecha
				Correo.Derecha.Izquierda=Correo.Izquierda
			else:	
				Correo.Izquierda.Derecha=None			
			Correo=None

#Matriz clase creada, instancia de Matriz:
Matriz=Matriz()


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


@app.route('/InsertarMatriz',methods=['POST']) 
def InsertarMatriz():
	parametro = str(request.form['dato'])		
	nombre, correo=parametro.split("@")
	letra=nombre[0]
	Matriz.insertar(nombre,correo,letra)
	return "insertado"

@app.route('/EliminarMatriz',methods=['POST']) 
def EliminarMatriz():
	parametro = str(request.form['dato'])		
	nombre, correo=parametro.split("@")
	letra=nombre[0]
	Matriz.eliminar(nombre,correo,letra)
	return "Eliminado"

@app.route('/BuscarLetra',methods=['POST']) 
def BuscarLetra():
	parametro = str(request.form['dato'])		
	return Matriz.imprimirL(parametro)

@app.route('/BuscarDominio',methods=['POST']) 
def BuscarDominio():
	parametro = str(request.form['dato'])		
	return Matriz.imprimirC(parametro)


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
