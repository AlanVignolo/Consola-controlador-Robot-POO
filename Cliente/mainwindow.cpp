#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QDebug>
#include <QFile>
#include <cstdlib>
using namespace std;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    //Se genera con los datos datos default en client.h
    user = new client();
    user->connectoServer();
    if(!user->ProbarConexion())
        qDebug() << "Conexion fallida";
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_Robot_2_clicked()
{
    QString aux = ui->lineEdit->text();
    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    try{
    string str = user->robot(aux.toStdString());
    ui->label_2->setText(QString::fromStdString(str));
    if (str == "INFO: ROBOT CONNECTED")
        system("mpg123 /home/vboxuser/Downloads/RobotON.mp3");
    else if(str == "INFO: ROBOT DISCONNECTED")
        system("mpg123 /home/vboxuser/Downloads/RobotOFF.mp3");
    } catch(...){
        ui->label_2->setText(QString::fromStdString("PARAMETROS INCORRECTOS"));
    }
}


void MainWindow::on_Motor_2_clicked()
{
    QString aux = ui->lineEdit->text();
    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    try{
    string str = user->Motores(aux.toStdString());
    ui->label_2->setText(QString::fromStdString(str));
    if (str == "INFO: MOTORS ON")
        system("mpg123 /home/vboxuser/Downloads/MotorON.mp3");
    else if(str == "INFO: MOTORS OFF")
        system("mpg123 /home/vboxuser/Downloads/MotorOFF.mp3");
    } catch(...){
        ui->label_2->setText(QString::fromStdString("PARAMETROS INCORRECTOS"));
    }
}


void MainWindow::on_Efector_2_clicked()
{
    QString aux = ui->lineEdit->text();
    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    try{
    string str = user->Efector(aux.toStdString());
    ui->label_2->setText(QString::fromStdString(str));
    if (str == "INFO: GRIPPER ON")
        system("mpg123 /home/vboxuser/Downloads/EfectorON.mp3");
    else if(str == "INFO: GRIPPER OFF")
        system("mpg123 /home/vboxuser/Downloads/EfectorON.mp3");
    } catch(...){
        ui->label_2->setText(QString::fromStdString("PARAMETROS INCORRECTOS"));
    }
}


void MainWindow::on_Lineal_2_clicked()
{
    QString aux = ui->lineEdit->text();
    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    try{
    string str = user->MovimientoLineal(aux.toStdString());
    ui->label_2->setText(QString::fromStdString(str));
    if (str == "ERROR: POINT IS OUTSIDE OF WORKSPACE")
        system("mpg123 /home/vboxuser/Downloads/error.mp3");
    } catch(...){
        ui->label_2->setText(QString::fromStdString("PARAMETROS INCORRECTOS"));
    }
}


void MainWindow::on_Circular_2_clicked()
{
    QString aux = ui->lineEdit->text();
    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    try{
    ui->label_2->setText(QString::fromStdString(user->MovimientoCircular(aux.toStdString())));
    } catch(...){
        ui->label_2->setText(QString::fromStdString("PARAMETROS INCORRECTOS"));
    }
}


void MainWindow::on_Reporte_2_clicked()
{
    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    user->Reporte(user->ProbarConexion());
    //Agregar la apertura del txt
    QFile txt;
    txt.setFileName("/home/vboxuser/Cliente/reporte.txt");
    if (!txt.exists())
        qDebug() << "El archivo no existe";
    txt.open(QIODevice::ReadOnly | QIODevice::Text);
    if (!txt.isOpen())
        qDebug() << "El archivo no se ha podido abrir";
    QString text = txt.readAll();
    ui->plainTextEdit->setPlainText(text);

}


void MainWindow::on_help_clicked()
{   string ayudastr;
            ayudastr= "En caso de no estar conectado con el servidor introduzca\n"
                      "IP: introduzca la direccion IP del SERVIDOR\n"
                      "Puerto: introduzca el puerto del SERVIDOR\n"
                    "-------------------------------------------------------------------------"
                      " Acciones: \n"
                      "Robot: introducir ON/OFF \n"
                    "Motor: introducir ON/OFF\n"
                    "Efector: introducir ON/OFF\n"
                    "Mov. Lineal: introducir [x] [y] [z] Velocidad \n"
                    "Mov. Circular: introducir numero de articulacion 1/2/3 Velocidad sentido: horario/antihorario y  angulo  \n"
                    "Posicion Actual: regresa la pos actual del robot\n"
                    "Posicion de Descanso: envia al robot a la pos de descanso\n"
                    "Reporte: devuelve el reporte y genera un archivo de texto \n"
                    "Cargar Trayectoria: introducir [x] [y] [z] Velocidad \n"
                    "Eliminar Trayectoria: elimina la trayectoria anterior\n"
                    "Enviar Trayectoria: envia la lista de acciones a ejecutar"
                      "\n"
                    "-------------------------------------------------------------------------";

    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    ui->plainTextEdit->setPlainText(QString::fromStdString(ayudastr));
}


void MainWindow::on_Conexion_clicked()
{
    QString aux = ui-> lineEdit_2 ->text();
    string ax = aux.toStdString();
    user->setIP(ax.c_str());
    aux = ui-> lineEdit_3 ->text();
    ax = aux.toStdString();
    user->setPort(ax.c_str());
    user->connectoServer();
    if (!user->ProbarConexion())
        ui->label_2->setText(QString::fromStdString("CONEXION FALLIDA"));
    else
        ui->label_2->setText(QString::fromStdString("CONECTADO"));

}


void MainWindow::on_Actual_clicked()
{
    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    ui->label_2->setText(QString::fromStdString(user->Actual()));
}


void MainWindow::on_Origen_clicked()
{
    if(!user->ProbarConexion())
        qDebug() << "No conectado con el servidor";
    ui->label_2->setText(QString::fromStdString(user->Origen()));
}


void MainWindow::on_Trayectoria_clicked()
{
    QString aux = ui-> lineEdit -> text();
    trayectoria += ("\n"+aux.toStdString());
    ui->plainTextEdit->setPlainText(QString::fromStdString(trayectoria));
}




void MainWindow::on_pushButton_2_clicked()
{
    try {
         ui->label_2->setText(QString::fromStdString(user->Aprendizaje(trayectoria)));
    }
    catch(...){
         ui->label_2->setText(QString::fromStdString("PARAMETROS INCORRECTOS"));
    }

}


void MainWindow::on_Eliminar_clicked()
{
    trayectoria = "";
    ui->plainTextEdit->setPlainText(QString::fromStdString("TRAYECTORIA ELIMINADA"));
}


void MainWindow::on_auto_2_clicked()
{
    try {
        QString aux = ui-> lineEdit ->text();
        ui->label_2->setText(QString::fromStdString(user->Automatico(aux.toStdString())));
    } catch (...) {
        ui->label_2->setText(QString::fromStdString("PARAMETROS INCORRECTOS"));
    }
}


void MainWindow::on_Modo_clicked()
{
    try {
        QString aux = ui-> lineEdit ->text();
        ui->label_2->setText(QString::fromStdString(user->Modo(aux.toStdString())));
    } catch (...) {
        ui->label_2->setText(QString::fromStdString("PARAMETROS INCORRECTOS"));
    }
}

