from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
import socket
import re

class Server(object):
    serverXML = None
    def __init__(self, consola,ServidorIP):
        self.consola = consola
        while True:
            try:
                self.serverXML = SimpleXMLRPCServer((ServidorIP.ip, ServidorIP.port),allow_none = True, logRequests = False)
                break
            except socket.error as e:
                if e.errno == 98:
                    port += 1
                    continue
                else:
                    raise

        self.serverXML.register_function(self.Robot, 'Robot')
        self.serverXML.register_function(self.Motores, 'Motores')
        self.serverXML.register_function(self.ListaAcciones, 'ListaAcciones')
        self.serverXML.register_function(self.Modo, 'Modo')
        self.serverXML.register_function(self.MovimientoCircular, 'MovimientoCircular')
        self.serverXML.register_function(self.MovimientoLineal, 'MovimientoLineal')
        self.serverXML.register_function(self.Efector, 'Efector')
        self.serverXML.register_function(self.Origen, 'Origen')
        self.serverXML.register_function(self.Reporte, 'Reporte')
        self.serverXML.register_function(self.do_ProbarConexion, 'ProbarConexion')
        self.serverXML.register_function(self.Actual, 'Actual')
        self.serverXML.register_function(self.Ejecutar, 'Ejecutar')
        self.serverXML.register_function(self.Aprendizaje, 'Aprendizaje')

        self.thread = Thread(target = self.ServidorActivo)
        self.thread.start()
        print(f"Servidor iniciado en el puerto {str(self.serverXML.server_address)}")

    def ServidorActivo (self):
        self.serverXML.serve_forever()

    def ServidorDesactivado(self):
        self.serverXML.shutdown()
        self.thread.join()
        print("Servidor desactivado")

    def Robot(self, orden):
        return self.consola.do_robot(orden,1)

    def Motores(self, orden):
        return self.consola.do_motores(orden,1)

    def ListaAcciones(self):
        return self.consola.do_lista(1)

    def Modo(self, orden):
        return self.consola.do_modo(orden,1)

    def MovimientoCircular(self, parametros):
        return self.consola.do_movimientocircular(parametros,1)

    def MovimientoLineal(self, parametros):
        return self.consola.do_movimientolineal(parametros,1).rstrip()

    def Efector(self, parametros):
        aux = self.consola.do_efector(parametros,1)
        aux=aux.split('\n')
        aux[0] = aux[0].rstrip()
        return aux[0]

    def Origen(self):
        return self.consola.do_origen(1)

    def Actual(self):
        return self.consola.do_actual(1)

    def Reporte(self):
        Archivo=open("Reporte.txt","r")
        Reporte=Archivo.read()
        Archivo.close()
        return Reporte

    def Aprendizaje(self,orden):
        orden=orden.split('\n')
        return self.consola.do_aprendizaje(1,orden[2:],orden[1])

    def Ejecutar(self,nombre):
        return self.consola.do_ejecutar(nombre,1)

    def do_ProbarConexion(self):
        return True