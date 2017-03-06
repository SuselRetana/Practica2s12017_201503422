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


	def imprimirCorreos(self):
		act=self.Inicio
		while act.Derecha!=None:
			print "["+act.Nombre+"]"
			act=act.Derecha
		print "["+act.Nombre+"]"
		print "I Z Q U I E R D A"
		while act!=None:
			print "["+act.Nombre+"]"
			act=act.Izquierda
	def imprimirLetras(self):
		act=self.Inicio
		while act.Abajo!=None:
			print "["+act.Nombre+"]"
			act=act.Abajo
		print "["+act.Nombre+"]"
		print "I Z Q U I E R D A"
		while act!=None:
			print "["+act.Nombre+"]"
			act=act.Arriba
	def imprimirL(self,letra) :	
		dominio=""
		act=self.buscar(letra)
		while act.Derecha!=None:
			dominio=dominio+ "["+act.Nombre+"]->"
			if act.AbajoP!=None :	
				dominio=dominio+self.imprimirP(act)
			act=act.Derecha
		dominio=dominio+ "["+act.Nombre+"]->"
		if act.AbajoP!=None :	
				dominio=dominio+self.imprimirP(act)
		return dominio

	def imprimirC(self,correo) :
		dominio=""		
		act=self.buscar(correo)
		while act.Abajo!=None:
			dominio=dominio+ "["+act.Nombre+"]->"
			if act.AbajoP!=None :	
				dominio=dominio+self.imprimirP(act)
			act=act.Abajo
		dominio=dominio+ "["+act.Nombre+"]->"
		if act.AbajoP!=None :	
				dominio=dominio+self.imprimirP(act)
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

#	def eliminar(self,Nombre,Correo,Letra):
#		Eliminar=self.buscar(Letra)
#		encontrado=False
#		while Eliminar!=None and encontrado==False:
#			if Eliminar.Correo==Correo:
#				encontrado=True
#			else:
#				Eliminar=Eliminar.Derecha
#		encontrado=False
#		if Eliminar.Nombre==Nombre :			
			
#			Aux=Eliminar

		
p=Matriz()
p.insertar("ana","gmail","a")
p.insertar("marco","gmail","m")
p.insertar("mama","gmail","m")
p.insertar("mono","gmail","m")
p.insertar("carlos","outlook","c")
p.insertar("amy","yahoo","a")
p.insertar("cesar","yahoo","c")
p.insertar("medrano","yahoo","m")
p.insertar("pedro","yahoo","p")
p.insertar("pablo","yahoo","p")
p.insertar("suselhot","hotmail","s")
p.insertar("anahot","hotmail","a")
p.insertar("suselby","by","s")
p.insertar("anaby","by","a")
print "L E T R A S:"
p.imprimirLetras()
print "C O R R E O S:"
p.imprimirCorreos()
print "L E T R A : A "
print p.imprimirL("a")
print "L E T R A : C"
print p.imprimirL("c")
print "L E T R A : M"
print p.imprimirL("m")
print "L E T R A : P"
print p.imprimirL("p")
print "L E T R A : S"
print p.imprimirL("s")
print "G M A I L"
print p.imprimirC("gmail")
print " O U T L O O K"
print p.imprimirC("outlook")
print "Y A H O O "
print p.imprimirC("yahoo")
print "H O T M A I L"
print p.imprimirC("hotmail")
print "B Y "
print p.imprimirC("by")