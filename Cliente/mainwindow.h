#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <string>
#include <iostream>
#include <QMainWindow>
using namespace std;

#include <QMainWindow>
#include "client.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_Motor_2_clicked();

    void on_Robot_2_clicked();

    void on_Efector_2_clicked();

    void on_Lineal_2_clicked();

    void on_Circular_2_clicked();

    void on_Reporte_2_clicked();

    void on_help_clicked();

    void on_Conexion_clicked();

    void on_Actual_clicked();

    void on_Origen_clicked();

    void on_Trayectoria_clicked();

    void on_pushButton_2_clicked();

    void on_Eliminar_clicked();

    void on_auto_2_clicked();

    void on_Modo_clicked();

private:
    Ui::MainWindow *ui;
    client *user;
    string trayectoria;
};
#endif // MAINWINDOW_H
