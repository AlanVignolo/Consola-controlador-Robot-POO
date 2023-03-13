from cmd import Cmd
from Server import Server
from re import ASCII 
from Robot import Robot
import sys

class Consola(Cmd):
    
    def __init__(self,ServidorIP):
        Cmd.__init__(self)
        self.Server1 = None
        self.ServidorIP=ServidorIP
        self.Robot=Robot(None,None)
        try:
            self.Server1 = Server(self,self.ServidorIP)
        except:
            print("No se ha podido conectar el servidor")
            pass


    def do_servidor (self, orden):
        """Conecta/Desconecta el Servidor segun (on/off)"""
        if orden == "on":
            if self.Server1 is None:
                self.Server1 = Server(self,self.ServidorIP) 
        elif orden == "off":
            if self.Server1 is not None:
                self.Server1.ServidorDesactivado()
                self.Server1 = None
        else:
            print("Introduzca True o False")
    

    def do_robot(self, orden, arg1=0):
        """Conecta/Desconecta el Robot segun (on/off)"""
        aux =self.Robot.ConectarRobot(orden)
        if arg1 != 1:
            self.mostrar(aux)
        else:
            return aux


    def do_motores(self,orden,arg1=0):
        """Enciende/Apaga los motores segun (on/off)"""
        aux = self.Robot.ModificarMotores(orden,arg1)
        if arg1 != 1:
            self.mostrar(aux)
        else:
            return aux


    def do_lista(self, arg1=0):
        aux="Conectar/Desconectar Servidor --> servidor + on/off\nConectar/Desconectar Robot --> robot + on/off\nEncender/Apagar Motores --> motores + on/off\nAyuda --> help\nSi modo manual ON --> Movimiento Circular --> MovimientoCircular + Articulacion(1/2/3) + velocidad + horario/antihorario + angulo\nSi modo manual ON --> Movimiento lineal --> movimientolineal + X + Y + Z + velocidad\nSi modo manual ON --> Activar Efector Final --> efector on/off\nSi modo manual ON --> Volver a posicion original --> origen\nSi modo manual ON --> Aprendizaje de trayectoria --> aprendizaje\nSi modo automatico ON --> Ejecutar archivo --> ejecutar + nombre\n"
        if arg1 != 1:
            self.mostrar(aux)
        else:
            return aux
    

    def do_modo(self, modo, arg1=0):
        """Modo de ejecucion segun Modo (manual/automatico)"""
        aux = self.Robot.setModo(modo,arg1)
        if arg1 != 1:
            self.mostrar(aux)
        else:
            return aux


    def do_movimientocircular(self,parametros, arg1=0):
        """Movimiento circular independiente de una articulacion con: movimientocircular articulacion velocidad sentido angulo"""
        try:
            articulacion,velocidad,sentido,angulo=parametros.split()
            aux =self.Robot.Manual_Mov_Circular(arg1, articulacion,velocidad,sentido,angulo)
            if arg1 != 1:
                self.mostrar(aux)
            else:
                return aux
        except:
            print("Error en los parametros")

    def do_movimientolineal(self,parametros, arg1=0):
        """Movimiento lineal de efector con: movimientolineal X Y Z velocidad"""
        # try:
        x,y,z,velocidad=parametros.split()
        aux=self.Robot.Manual_Mov_Lineal(arg1,x,y,z,velocidad)
        if arg1 != 1:
            self.mostrar(aux)
        else:
            return aux
        # except:
            # print("Error en los parametros")

    def do_efector(self,parametro,arg1= 0):
        """Activar/Desactivar Efector final con: efector + on/off"""
        aux = self.Robot.Manual_Efector(arg1, parametro)
        if arg1 != 1:
            self.mostrar(aux)
        else:
            return aux
    

    def do_origen(self,arg1=0):
        """Volver a la posicion de origen"""
        aux = self.Robot.Manual_Origen(arg1)
        if arg1 != 1:
            self.mostrar(aux)
        else:
            return aux
    

    def do_aprendizaje(self,arg1=0,Lista=None,nombre1=None):
        """Realiza la carga de una serie de acciones"""
        if Lista is not None:
                self.Robot.Aprendizaje(arg1,Lista,nombre1)
                return "Aprendizaje realizado"
        Acciones = []
        nombre = input("Nombre del archivo: ")
        while True:
            aux = input ("Ingrese una accion  (motores | modo | movimientoCircular | movimientoLineal | efector | origen | carga | 0 para salir) :\n   ")
            if aux == "0":
                self.Robot.Aprendizaje(arg1,Acciones,nombre)
                print("Aprendizaje finalizado")
                break
            elif aux == "motores":
                param = input("Ingrese los parametros (on/off)  ")
                try:
                    if param.lower() == "on":
                        Acciones.append("g34")
                    elif param.lower() == "off":
                        Acciones.append("g35")
                except:
                    print("Parametros incorrectos")
                    pass
            elif aux == "modo":
                param = input("Ingrese los parametros (manual/automatico)  ")
                try:
                    if param.lower() == "manual":
                        Acciones.append("g36")
                    elif param.lower() == "automatico":
                        Acciones.append("g37")
                except:
                    print("Parametros incorrectos")
                    pass
            elif aux.lower() == "movimientocircular":
                try:
                    param = input ("Ingrese Articulacion Velocidad Sentido Angulo  ").split()
                    print(param)
                    Acciones.append(f"g0 {arg1} {int(param[0])} {float(param[1])} {str(param[2])} {float(param[3])}")
                except:
                    print("Error en los parametros")
                    pass
            elif aux.lower() == "movimientolineal":
                try:
                    param = input ("Ingrese X Y Z Velocidad  ").split()
                    Acciones.append(f"g1 {arg1} {float(param[0])} {float(param[1])} {float(param[2])} {float(param[3])}")
                except:
                    print("Error en los parametros")
                    pass
            elif aux.lower() == "efector":
                try:
                    param = input ("Ingrese on/off  ")
                    if param.lower() == "on":
                        Acciones.append(f"g3")
                    elif param.lower() == "off":
                        Acciones.append(f"g5")
                    else:
                        print("Error en los parametros")
                        pass
                except:
                    print("Error en los parametros")
                    pass
            elif aux.lower()== "origen":
                Acciones.append(f"g28 0 0 0")
            elif aux.lower() == "carga":
                param = input ("Ingrese el nombre del archivo  ")
                Acciones.append(f"g10 {param}")
            else:
                print("Comando incorrecto")
                pass


    def do_ejecutar(self, nombre, arg1=0):
        aux = self.Robot.Automatico_Ejecucion(arg1,nombre)
        if arg1 != 1:
            self.mostrar(aux)
        else:
            return aux


    def postcmd(self, stop,line):
        return False

    
    def do_Exit(self, arg1):
        self.Robot.ConectarRobot("off")
        self.do_servidor("off")
        return sys.exit()


    def mostrar(self,mensaje):
        sys.stdin.flush()
        print(mensaje)


    def do_actual(self, arg1=0):
        if arg1 != 1:
            self.mostrar(self.Robot.actual())
        else:
            return self.Robot.actual()