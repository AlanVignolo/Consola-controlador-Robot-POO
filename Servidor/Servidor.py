from Consola import Consola
from Servidor_ip import Servidor_ip
from threading import Thread

if __name__ == '__main__':
    Consola1=Consola()
    thread = Thread(target = Consola1)
    Consola1.prompt = '>>'
    Consola1.cmdloop("VENTANA DE COMANDOS ROBOT ABB IRB 460")   