from progress.bar import ChargingBar
import time, random
from pick import pick
import os

#Se borrará la pantalla al iniciar el programa y se pondrá en todas las opciones.
os.system('clear')

#Pantalla inicial del juego para la creación del rostro con 5 opciones.
titulo="""
  ______ .______    _______      ___       _______    ______   .______      
 /      ||   _  \  |   ____|    /   \     |       \  /  __  \  |   _  \     
|  ,----'|  |_)  | |  |__      /  ^  \    |  .--.  ||  |  |  | |  |_)  |    
|  |     |      /  |   __|    /  /_\  \   |  |  |  ||  |  |  | |      /     
|  `----.|  |\  \-.|  |____  /  _____  \  |  '--'  ||  `--'  | |  |\  \-.
 \______|| _| `.__||_______|/__/     \__\ |_______/  \______/  | _| `.__|

.______     ______       _______..___________..______     ______   
|   _  \   /  __  \     /       ||           ||   _  \   /  __  \  
|  |_)  | |  |  |  |   |   (----``---|  |----`|  |_)  | |  |  |  | 
|      /  |  |  |  |    \   \        |  |     |      /  |  |  |  | 
|  |\  \-.|  `--'  | .---)   |       |  |     |  |\  \-.|  `--'  | 
| _| `.__| \______/  |______/        |__|     | _| `.__| \______/  ****
                                                                          
"""
opciones = ['CREAR ROSTRO', 'CARGAR ROSTO', 'BORRAR ROSTRO', 'LISTA ROSTROS', 'SALIR']

opcion, index = pick(opciones, titulo, indicator='ᐅ', default_index=0)

#Este es el código para la creación del personaje
def imprimir_archivo(codigos,menu):
  i=1
  if menu ==0:
    print('\n','\n','\n')
  for linea_codigo in codigos:
    print(i, end='\t')
    for codigo in linea_codigo:
      imprimir_linea(codigo)
    i+=1  
    print("\t")

  if menu == 1:
     print("")
     opcion = int(input("Seleccione el pelo: "))
     habitante.append(codigos_pelo[opcion-1])
  elif menu == 2:
     print("")
     opcion = int(input("Seleccione los ojos: "))
     habitante.append(codigos_ojos[opcion-1])
  elif menu == 3:
     print("")    
     opcion = int(input("Seleccione la nariz: "))
     habitante.append(codigos_nariz[opcion-1])
  elif menu == 4:
     print("")    
     opcion = int(input("Seleccione la boca: "))
     habitante.append(codigos_boca[opcion-1])    
  elif menu == 5:
     print("")    
     opcion = int(input("Seleccione el cuello: "))
     habitante.append(codigos_cuello[opcion-1])
  elif menu ==0:
     print("")
     print("Rostro del personaje")
     print("\n")
     

def imprimir_linea(codigo):
  cadena = str(codigo[0])
  numero = int(cadena[0])
  caracter = cadena[1]
  
  for i in range (0, numero):
      print(caracter, end="")
  

def cargar_archivo(direccion):
  f = open(direccion)
  archivo = []
  for linea in f:
    codigos_linea = linea.rstrip().split(',')
    linea = []
    for codigo in codigos_linea:
        linea.append(codigo.split('\t'))
    archivo.append(linea)  
  return archivo  


def generar_rostro():
  imprimir_archivo(codigos_pelo,1)
  imprimir_archivo(habitante,0)
  imprimir_archivo(codigos_ojos,2)
  imprimir_archivo(habitante,0)
  imprimir_archivo(codigos_nariz,3)
  imprimir_archivo(habitante,0)
  imprimir_archivo(codigos_boca,4)
  imprimir_archivo(habitante,0)
  imprimir_archivo(codigos_cuello,5)
  imprimir_archivo(habitante,0)


def codifica_habitante(habitante):
  persona = ""
  for linea in habitante:
    for codigo in linea:
      for pedacito in codigo:
          persona = persona + str(pedacito) + ","
    persona = persona [:len(persona)-1]
    persona =  persona + "\n"
  return persona


def pide_nombre():
  nombre=input("Ingrese el nombre del personaje: ")
  return nombre

habitante =[]
procesado=""
codigos_pelo = cargar_archivo('rostro/pelos.txt')
codigos_ojos = cargar_archivo('rostro/ojos.txt')
codigos_nariz = cargar_archivo('rostro/nariz.txt')
codigos_boca = cargar_archivo('rostro/bocas.txt')
codigos_cuello = cargar_archivo('rostro/cuellos.txt')  

#Acá empieza el menú
#Si elige la opción CREAR PERSONAJE empezará el programa con las opciones.
if opcion == 'CREAR ROSTRO':
  os.system('clear')
  #Barra de carga
  print("")
  bar2 = ChargingBar('CARGANDO LA CREACIÓN DE ROSTROS', max=100, color='white')
  for num in range(100):
    time.sleep(random.uniform(0, 0.04))
    bar2.next()
  bar2.finish()
  print("")
  generar_rostro()
  procesado = procesado + "\n" + pide_nombre() + "\n" + codifica_habitante(habitante)
  print("")
  print("Su personaje se creó satisfactoriamente \n")
  #Se guarda el rostro
  f = open("rostro/habitantes.txt","a")
  f.write(procesado)
  f.close()

  

#Se cargará el rostro cuando el usuario digite el nombre.
elif opcion == 'CARGAR ROSTO':
  os.system('clear')
  habitantes_procesados = cargar_archivo('rostro/habitantes.txt')
  id = input("Ingrese el personaje a cargar: ")
  indice = int(habitantes_procesados.index([[id]]))
  print(indice)
  imprimir_archivo(habitantes_procesados[indice + 1:indice + 6],0)


#Si se desea borrar el rostro registrado
elif opcion == 'BORRAR ROSTRO':
  os.system('clear')
  personaje=input("INGRESA EL NOMBRE DEL ROSTRO QUE DESEAS BORRAR: ")
  
  nose="""
       _______. _______   _______  __    __  .______        ______    ______   
      /       ||   ____| /  _____||  |  |  | |   _  \      /  __  \  |      \  
     |   (----`|  |__   |  |  __  |  |  |  | |  |_)  |    |  |  |  | `----)  | 
      \   \    |   __|  |  | |_ | |  |  |  | |      /     |  |  |  |     /  /  
  .----)   |   |  |____ |  |__| | |  `--'  | |  |\  \----.|  `--'  |    |__|   
  |_______/    |_______| \______|  \______/  | _| `._____| \______/      __    
                                                                        (__)   
  """
  sg = ['SI', 'NO']
  seguro, index = pick(sg, nose, indicator='ᐅ', default_index=0)
  
  #Barra de carga
  print("")
  bar2 = ChargingBar('Cargando ', max=100, color='white')
  for num in range(100):
    time.sleep(random.uniform(0, 0.02))
    bar2.next()
  bar2.finish()
  print("")

  if seguro == 'SI':
    print("ERROR, INTÉNTALO DE NUEVO MÁS TARDE.")
    
  else:
    print("IGUAL NO LO IBA A BORRAR (ง '̀-'́)ง ")

  
#Acá se mostrará toda lal ista de rostros registrada.
elif opcion == 'LISTA ROSTROS':
  os.system('clear')
  print("LISTA ROSTROS")
  print("")
  lp = open('rostro/habitantes.txt', 'r')
  for listapjs in lp:
    print(listapjs)
  lp.close()


#Si eligue la opción SALIR se le despedira con un dibujo.
elif opcion == 'SALIR':
  os.system('clear')  
  print("""     
  ¡HASTA LA PRÓXIMA!    
        
──────────────▄▀█▀█▀▄
─────────────▀▀▀▀▀▀▀▀▀
─────────────▄─░░░░░▄
───█──▄─▄───▐▌▌░░░░░▌▌
▌▄█▐▌▐█▐▐▌█▌█▌█░░░░░▌▌

  ༼つಠ_ಠ༽つ ─=≡ΣO))    
        """)

#FIN