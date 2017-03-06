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

lista=Lista()
lista.insertar("1l")
lista.insertar("2l")
lista.insertar("3l")
lista.insertar("4l")
lista.insertar("5l")
class reportes(object):
	def txtlista(self):
		archi=open('lista.txt','w')
		archi.close
		self.reporteLista()
		print "Sale Fin"
		pass
	
	def reporteLista(self):
		archi=open('lista.txt','a')
		archi.write("digraph G {")
		aux=lista.Inicio
		while aux.Siguiente!=None :
			archi.write('"'+aux.Valor+'"->"'+aux.Siguiente.Valor+'" ')    	
			aux=aux.Siguiente
		archi.write("}")
		archi.close()
		self.ejecutar("lista")
		print"Sale Fin1"
		pass	
	def ejecutar(self,nombre):    
		import os		
		dotPath = "C:\\Graphviz2.38\\bin\\dot.exe"
		fileInputPath = "C:\\Users\\freni_000\\Desktop\\Semestre5\\EstructurasdeDatos\\Practica2s12017_201503422\\Practica2s12017_201503422\\"+nombre+".txt"
		fileOutputPath = "C:\\Users\\freni_000\\Desktop\\Semestre5\\EstructurasdeDatos\\Practica2s12017_201503422\\Practica2s12017_201503422\\"+nombre+".jpg"
		tParam = " -Tjpg "
		tOParam = " -o "
		tuple = (dotPath +tParam+ fileInputPath+tOParam+fileOutputPath)
		os.system(tuple)	
		print"Sale Fin2"
#Reportes clase creada, instancia de reportes:
reportes=reportes()
reportes.txtlista()