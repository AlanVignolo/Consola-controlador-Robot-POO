#ifndef CLIENT_H
#define CLIENT_H

#include <iostream>
#include <stdlib.h>
#include <string>
#include <cstdlib>
using namespace std;
#include "XmlRpc.h"
using namespace XmlRpc;

class client{
public:

    client();
    void setIP(const char* IP);
    void setPort(const char* port);
    void connectoServer();
    void disconnectFromServer();
    // Funciones del servidor
    string robot(string);
    string Motores(string);
    string ListaAcciones();
    string MovimientoCircular(string);
    string MovimientoLineal(string);
    string Efector(string);
    string ConfigurarParametros();
    void Reporte(bool);
    string GUI();
    bool ProbarConexion();
    string Origen();
    string Actual();
    string Aprendizaje(string);
    static void sound();
    void sound1();
    string Automatico(string);
    string Modo(string);

private:
    XmlRpcClient *c;
    const char* IP = "192.168.1.38";
    int port = 8900;
};

#endif // CLIENT_H
