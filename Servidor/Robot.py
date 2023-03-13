import serial
from Archivar import Archivar
import os
import time
class Robot:


    def __init__(self, com, num, estado=True):
        self.Motores = True
        self.Efector = False
        self.Modo = True
        self.Archivo=Archivar()
        self.Serie = None
        if estado:
            try:
                self.Serie=serial.Serial(port='COM4', baudrate=9600, timeout=2, write_timeout=2)
                self.Archivo.setEstado(True)
                time.sleep(0.2)
                self.Serie.flushInput()
                self.Serie.flushOutput()
                self.Serie.flush()
                print("Estado de Robot: Conectado")
            except:
                print("Error de conexion serie inicial")
                pass
        else:
            self.Serie= None


    def ConectarRobot (self, orden):
        if orden.lower() == "on":
            if self.Serie is None:
                try:
                    self.Serie = serial.Serial(port='COM4', baudrate=9600, timeout=2, write_timeout=2)
                    self.Archivo.setEstado(True)
                    return "INFO: ROBOT CONNECTED"
                except:
                    return "INFO: SERIAL ERROR"
            else:
                return "INFO: ROBOT ALREADY CONNECTED"
        elif orden.lower() == "off":
            if self.Serie is not None:
                self.Serie.close()
                self.Serie = None
                self.Archivo.setEstado(False)
                return "INFO: ROBOT DISCONNECTED"
            else:
                return "INFO: NO ROBOT CONNECTED"
        else:
            return "INFO: INVALID COMMAND"


    def Enviar_a_Robot(self,Mensaje):

            if self.Serie is not None:
                self.Serie.flush()
                self.Serie.flushInput()
                self.Serie.flushOutput()
                self.Serie.write(Mensaje.encode())
                time.sleep(1)
                try:
                    while self.Serie.in_waiting > 0:
                        aux = self.Serie.readlines()
                    for x in range(len(aux)):
                        aux[x] = aux[x].decode()
                    aux = "".join(aux)
                    return aux
                except:
                    return "ERROR: SERIAL ERROR"
            else:
                return "No hay un Robot conectado"
    

    def ModificarMotores(self, orden,pedido):
        if self.Serie is not None:
            if orden.lower()=="on" :
                if self.Motores == True:
                    # self.Enviar_a_Robot("")
                    return "INFO: MOTORS ALREADY ON"
                else:
                    self.Archivo.Guardar_Accion("Encender Motores",pedido,str(orden))
                    self.Motores = True
                    return "INFO: MOTORS ON"
            elif orden.lower()=="off":
                if self.Motores == True:
                    # self.Enviar_a_Robot("")
                    self.Archivo.Guardar_Accion("Apagar Motores",pedido,str(orden))
                    self.Motores = False
                    return "INFO: MOTORS OFF"
                else:
                    return "INFO: MOTORS ALREADY OFF"
            else:
                return "INFO: INVALID COMMAND"
        else:
            return "INFO: NO ROBOT CONNECTED"
        

    def setModo(self, modo,pedido):
        if self.Serie is not None:
            if modo.lower() == "manual" and self.Modo == False:
                self.Modo = True
                self.Archivo.Guardar_Accion("Cambio a modo Manual",pedido)
                return "INFO: MANUAL MODE"
            elif modo.lower() == "manual" and self.Modo == True:
                return "INFO: ALREADY IN MANUAL MODE"
            elif modo.lower() == "automatico" and self.Modo == True:
                self.Modo = False
                self.Archivo.Guardar_Accion("Cambio a modo Automatico",pedido)
                return "INFO: AUTOMATIC MODE"
            elif modo.lower() == "automatico" and self.Modo == True:
                return "INFO: ALREADY IN AUTOMATIC MODE"
            else:
                return "INFO: INVALID MODE"
        else:
            return "INFO: NO ROBOT CONNECTED"


    def Manual_Mov_Circular(self,pedido,articulacion,velocidad,sentido,angulo):
        try:
            articulacion = int(articulacion)
            velocidad = float(velocidad)
            angulo = float(angulo)
        except:
            return "INFO: INVALID PARAMETERS"
        if sentido.lower() != "horario" and sentido.lower() != "antihorario":
            return "INFO: INVALID PARAMETERS"
        if articulacion == 1 or articulacion == 2 or articulacion == 3:
            if self.Modo == True:    
                if self.Serie is not None and self.Motores == True:
                    self.Archivo.Guardar_Accion("Movimiento Circular ",pedido,"Articulacion: "+str(articulacion),"Velocidad: "+str(velocidad)+" mm/s","Sentido: "+str(sentido),"Angulo: "+str(angulo)+"°")
                    return (f"INFO: CIRCULAR MOVE: [ART: {articulacion} VEL: {velocidad} mm/s SENT: {sentido}, ANG: {angulo}°]")
                elif self.Serie is None:
                    return "INFO: NO ROBOT CONNECTED"
                elif self.Motores == False:
                    return "INFO: MOTORS OFF"
            else:
                return "INFO: ROBOT IN AUTOMATIC MODE"
        else:
            return "INFO: INVALID JOINT"


    def Manual_Mov_Lineal(self,pedido,x,y,z,velocidad):
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            velocidad = float(velocidad)
        except:
            return "INFO: INVALID PARAMETERS"
        if self.Modo == True:
            if self.Serie is not None and self.Motores == True:
                aux =self.Enviar_a_Robot((f"G1 X{str(x)} Y{str(y)} Z{str(z)} F{str(velocidad)}\r\n"))
                if list(aux[0]) == "E":
                    return aux
                else:
                    self.Archivo.Guardar_Accion("Movimiento Lineal",pedido," X: "+str(x)," Y: "+str(y)," Z: "+str(z)," Velocidad: "+str(velocidad))
                    return aux
            elif self.Serie is None:
                return "INFO: NO ROBOT CONNECTED"
            elif self.Motores == False:
                return "INFO: MOTORS OFF"
        else:
            return "INFO: ROBOT IN AUTOMATIC MODE"


    def Manual_Efector(self,pedido ,modo):
        if self.Modo == True:
            
            if self.Serie is not None:
                
                if modo.lower()=="on":
                    if self.Efector == False:
                        self.Efector = True
                        self.Archivo.Guardar_Accion("Activacion Efector",pedido)
                        
                        return self.Enviar_a_Robot("M3\r\n")
                    elif self.Efector==True:
                        return "INFO: GRIPPER ALREADY ON"
                elif modo.lower()=="off":
                    if self.Efector==True:
                        self.Efector=False
                        self.Archivo.Guardar_Accion("Desacrivar Efector",pedido)
                        return self.Enviar_a_Robot("M5\r\n")
                    elif self.Efector==False:
                        return "INFO: GRIPPER ALREADY OFF"
                else:
                    return "INFO: INVALID COMMAND"
            else:
                return "INFO: NO ROBOT CONNECTED"
        else:
            return "INFO: ROBOT IN AUTOMATIC MODE"


    def Manual_Origen(self,pedido):
        if self.Modo == True:
            if self.Serie is not None and self.Motores == True:
                self.Descanso = True
                self.Archivo.Guardar_Accion("Movimiento Lineal a posicion de Reposo",pedido)
                return self.Enviar_a_Robot("G28\n\r")
            elif self.Serie is None and self.Motores == True:
                return "INFO: NO ROBOT CONNECTED"
            elif self.Motores == False and self.Serie is not None:
                return "INFO: MOTORS OFF"
        else:
            return "INFO: ROBOT IN AUTOMATIC MODE"


    def Aprendizaje(self,pedido ,Acciones, nombrearchivo):
        if self.Series is not None:
            if self.Modo == True:
                if nombrearchivo == "Reporte":
                    return "INFO: INVALID NAME"
                if os.path.exists(f'{nombrearchivo}.txt') == False:
                    Archivo = open(f'{nombrearchivo}.txt','a')
                    for x in Acciones:
                        Archivo.write(x+"\n")
                    Archivo.close()
                    self.Archivo.Guardar_Accion("Aprendizaje del archivo: ",pedido,nombrearchivo)
                    return "INFO: LEARNING COMPLETE"
                else:
                    return "INFO: FILE ALREADY EXISTS"
            else:
                return "INFO: ROBOT IN AUTOMATIC MODE"
        else:
            return "INFO: NO ROBOT CONNECTED"

    def Automatico_Ejecucion(self,pedido, nombrearchivo):
        if self.Series is not None:
            if self.Modo == False:
                try:
                    Archivo = open(f'{nombrearchivo}.txt','r')
                    Acciones = Archivo.readlines()
                    Acciones = [x.strip() for x in Acciones]
                    Archivo.close()
                    for x in range(len(Acciones)):
                        aux = Acciones[x].split()
                        if aux[0].lower() == "g34":
                            print(self.ModificarMotores("on",pedido))
                        if aux[0].lower() == "g35":
                            print(self.ModificarMotores("off",pedido))
                        if aux[0].lower() == "g36":
                            print(self.setModo("manual",pedido))
                        if aux[0].lower() == "g37":
                            print(self.setModo("automatico",pedido))
                        if aux[0].lower() == "g0":
                            print(self.Manual_Mov_Circular(pedido,aux[1],aux[2],aux[3],aux[4]))
                        if aux[0].lower() == "g1":
                            print(self.Manual_Mov_Lineal(pedido,aux[1],aux[2],aux[3],aux[4]))
                        if aux[0].lower() == "g3":
                            print(self.Manual_Efector(pedido,"on"))
                        if aux[0].lower() == "g5":
                            print(self.Manual_Efector(pedido,"off"))
                        if aux[0].lower() == "g28":
                            print(self.Manual_Origen(pedido))
                        if aux[0].lower() == "g10":
                            print(self.Automatico_Ejecucion(pedido,{aux[1]}))

                    self.Archivo.Guardar_Accion("Ejecucion automatica del archivo: ",pedido,nombrearchivo)
                    return "INFO: PROGRAM FINISHED"
                except FileNotFoundError:
                    return "INFO: INVALID FILE"
            else:
                return "INFO: ROBOT IN MANUAL MODE"
        else:
            return "INFO: NO ROBOT CONNECTED"


    def actual(self):
        return self.Enviar_a_Robot("M114\n\r")