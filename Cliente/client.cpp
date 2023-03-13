#include "client.h"
#include "report.h"
#include <iostream>
#include <thread>
#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;
using namespace XmlRpc;

client::client(){}

void client::connectoServer()
{
    this->c = new XmlRpcClient(this->IP, this->port);
    thread hilo(this->sound);
    hilo.detach();
}

void client::setIP(const char* IP)
{
    this->IP = IP;
}

void client::setPort(const char* port)
{
    int _port;
    _port = atoi(port);
    this->port = _port;
}

void client::disconnectFromServer()
{
    c->close();
}

string client::robot(string estado)
{

    XmlRpcValue Args, result;
    Args[0] = estado;
    if (c->execute("Robot", Args, result))
        return result;
    else
        return "Error en la llamada a 'robot'";
}

string client::Motores(string estado)
{
    XmlRpcValue Args, result;
    Args[0] = estado;
    if (c->execute("Motores", Args, result))
        return result;
    else
        return "Error en la llamada a 'Motores'";
}

string client::ListaAcciones()
{
    XmlRpcValue noArgs, result;
    if (c->execute("ListaAcciones", noArgs, result))
        return result;
    else
        return "Error en la llamada a 'ListaAcciones'";
}

string client::MovimientoCircular(string parametros)
{
    XmlRpcValue Args, result;
    Args[0] = parametros;
    if (c->execute("MovimientoCircular", Args, result))
        return result;
    else
        return "Error en la llamada a 'MovimientoCircular'";
}

string client::MovimientoLineal(string parametros)
{
    XmlRpcValue Args, result;
    Args[0] = parametros;
    if (c->execute("MovimientoLineal", Args, result))
        return result;
    else
        return "Error en la llamada a 'MovimientoLineal'";
}

string client::Efector(string estado)
{
    XmlRpcValue Args, result;
    Args[0] = estado;
    if (c->execute("Efector", Args, result))
        return result;
    else
        return "Error en la llamada a 'Efector'";
}

string client::ConfigurarParametros()
{
    XmlRpcValue noArgs, result;
    if (c->execute("ConfigurarParametros", noArgs, result))
        return result;
    else
        return "Error en la llamada a 'ConfigurarParametros'";
}

void client::Reporte(bool flag)
{
    XmlRpcValue noArgs, result;
    if (c->execute("Reporte", noArgs, result)){
        report reporte("reporte");
        if (flag){
            reporte.do_report("ESTADO DE LA CONEXION: ON");
        }
        else{
            reporte.do_report("ESTADO DE LA CONEXION: OFF");
        }
        reporte.do_report(result);
    }
    else
        cout << "Error en la llamada a 'Reporte'";
}

string client::GUI()
{
    XmlRpcValue noArgs, result;
    if (c->execute("GUI", noArgs, result))
        return result;
    else
        return "Error en la llamada a 'GUI'";
}

bool client::ProbarConexion()
{
    XmlRpcValue noArgs, result;
    if (c->execute("ProbarConexion", noArgs, result))
        return result;
    else
        return false;
}

string client::Origen()
{
    XmlRpcValue noArgs, result;
    if (c->execute("Origen", noArgs, result))
        return result;
    else
        return "Error en la llamada a 'Origen'";
}

string client::Actual()
{
    XmlRpcValue noArgs, result;
    if (c->execute("Actual", noArgs, result))
        return result;
    else
        return "Error en la llamada a 'actual'";
}

string client::Aprendizaje(string trayectoria)
{
    XmlRpcValue Args, result;
    Args[0] = trayectoria;
    if (c->execute("Aprendizaje", Args, result))
        return result;
    else
        return "Error en la llamada a 'actual'";
}

void client::sound(){
   client client1;
   cout << "asdfghjkl;'";
   client1.sound1();
}

void client::sound1(){
    string robot = "1", motores= "0", efector="0";
     XmlRpcValue args, results;
     while(true){
     if (c->execute("parametros",args,results)){
         if (results[0]=="0" && robot =="1"){
             robot = "0";
             system("mpg123 /home/vboxuser/Downloads/RobotON.mp3");
         }
         else if (results[0]=="1" && robot =="0"){
             system("mpg123 /home/vboxuser/Downloads/RobotOFF.mp3");
             robot = "1";
         }
         if (results[1]=="0" && motores =="1"){
             system("mpg123 /home/vboxuser/Downloads/MotorON.mp3");
             motores = "0";
         }
         else if (results[1]=="1" && motores =="0"){
             system("mpg123 /home/vboxuser/Downloads/MotorOFF.mp3");
             motores = "1";
         }
         if (results[2]=="1" && efector =="1"){
             system("mpg123 /home/vboxuser/Downloads/EfectorON.mp3");
             efector = "0";
         }
         else if (results[1]=="1" && motores =="0"){
             system("mpg123 /home/vboxuser/Downloads/EfectorON.mp3");
             efector = "1";
         }
     }
}

}

string client::Automatico(string AUT){
    XmlRpcValue Args, result;
    Args[0]= AUT;
    if (c->execute("Ejecutar", Args, result))
        return result;
    else
        return "error en modo automatico";
};

string client::Modo(string modo){
    XmlRpcValue Args, result;
    Args[0]= modo;
    if (c->execute("Modo", Args, result))
        return result;
    else
        return "Error en el cambio de modo";
}
