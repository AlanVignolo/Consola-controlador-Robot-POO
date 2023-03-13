from datetime import datetime 

class Archivar():
    def __init__(self):
        self.OrdenesCliente=0
        self.CantOrdenes=0
        self.Estado_de_Robot=False
        self.TiempoInicial = str(datetime.now().strftime('%H:%M'))
        self.FechaInicial = str(datetime.now().strftime('%Y-%m-%d'))

        Reporte= open("Reporte.txt",'w')
        Reporte.write(f"REPORTE ROBOT ABB IRB 460 \n")
        if self.Estado_de_Robot == True:
            Reporte.write("Robot Conectado\n")
        else:
            Reporte.write("Robot Desconectado\n")
        Reporte.write(f"Cantidad de ordenes: {self.OrdenesCliente}\n")
        Reporte.write(f"Cantidad de ordenes pedidas: {self.CantOrdenes}\n")
        Reporte.write(f"Inicio de Actividad\nFecha: {self.FechaInicial} Hora: {self.TiempoInicial} \n")
        Reporte.close()

    def Guardar_Accion(self,accion,pedido,param1="",param2="",param3="",param4="",param5=""):
        self.CantOrdenes += 1
        if pedido == 1:
            Reporte = open('Reporte.txt','a')
            Reporte.write(f"{accion}{param1}{param2}{param3}{param4}{param5} Ejecutado por Cliente. Hora: {datetime.now().strftime('%H:%M')}\n")
            Reporte.close()
            self.OrdenesCliente += 1
        else:
            Reporte = open('Reporte.txt','a')
            Reporte.write(f"{accion} {param1} {param2} {param3} {param4} {param5} Ejeceutado por Servidor. Hora: {datetime.now().strftime('%H:%M')}\n")
            Reporte.close()

        lines=""
        with open("Reporte.txt", 'r+') as Reporte:
            lines = Reporte.readlines()
            Reporte.seek(0)
            Reporte.truncate()

        Reporte=open("Reporte.txt",'w')
        Reporte.write(f"REPORTE ROBOT ABB IRB 460 \n")
        if self.Estado_de_Robot == True:
            Reporte.write("Robot Conectado\n")
        else:
            Reporte.write("Robot Desconectado\n")
        Reporte.write(f"Cantidad de ordenes: {self.CantOrdenes}\n")
        Reporte.write(f"Cantidad de ordenes pedidas: {self.OrdenesCliente}\n")
        Reporte.writelines(lines[4:])
        Reporte.close()


    def setEstado(self,estado):
        self.Estado_de_Robot=estado
        with open("Reporte.txt", 'r+') as Reporte:
                lines = Reporte.readlines()
                Reporte.seek(0)
                Reporte.truncate()
        
        Reporte=open("Reporte.txt",'w')
        Reporte.write(f"REPORTE ROBOT ABB IRB 460 \n")
        if estado == True:
            Reporte.write("Robot Conectado\n")
        else:
            Reporte.write("Robot Desconectado\n")
        Reporte.writelines(lines[2:])
        Reporte.close()