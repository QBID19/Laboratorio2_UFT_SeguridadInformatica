import Cesar, RailFence
import hashlib

TextoACifrar = open('mensajedeentrada.txt','r') #Txt que contiene el texto plano
TextoPlano = TextoACifrar.readlines()[0] #Extrae el texto plano del archivo
TextoACifrar.close()

#Aplicación del Hash md5 al texto plano
TextoHash = hashlib.md5()
textoAHashear = TextoPlano
TextoHash.update(textoAHashear.encode())
HashTextoPlano = TextoHash.hexdigest()


N_Cesar = 5 #Nro de veces de Cesar
TextoCesar = Cesar.Rot(N_Cesar)(TextoPlano) #Texto cifrado con Cesar


archivoHashear = open('mensajeseguro.txt','w')
archivoHashear.write(TextoCesar)
archivoHashear.close()
