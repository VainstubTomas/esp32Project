import network
import utime

wifi = network.WLAN(network.STA_IF) #ESTACION DETECTORA DE CONEXION WLAN
wifi.active(True) #VERIFICA FUNCIONAMIENTO DE DETECCION

lista = wifi.scan() #MUESTRA POSIBLES REDES
for red in lista: #ORDENA LAS REDES ENCONTRADAS
    print(red)
    
#CANAL, POTENCIA, TIPO DE ENCRIPTACION, LIBRE/PRIVADA
    
print()
    
for red in lista: #ORDENA LAS REDES ENCONTRADAS SOLO MOSTRANDO EL NOMBRE
    print(red[0].decode()) #ESPECIFICANDO LA POSICION DEL ARRAY, SIMPLIFICAMOS LA INFORMACION, CON EL .DECODE, QUITAMOS LA INICIAL b
                            #LA CUAL ACLARA QUE ES UN ARRAY DE BYTES (CONJ.DE BYTES).
    
wifi.connect("Flia Grassino","48064032") #ID+PASSW
#HAY QUE ESPERAR QUE SE CONECTE (WHILE INTERACTIVO)
while not wifi.isconnected():
    print (".")
    utime.sleep(1)
    #A PARTIR DEL WIFI.CONNECT ES LA PARTE NECESARIA DEL CODIGO, LA PARTE DEL SCAN ES SOLO DEMOSTRATIVA
    
print(wifi.ifconfig()) #DIR.IP, NETMASK, GATEWAY Y DNS