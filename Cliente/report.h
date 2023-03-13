#ifndef REPORT_H
#define REPORT_H

#include <fstream>
#include <iostream>
#include <string>
using namespace std;
//clase report la cual abre un archivo txt y escribe en el

class report{
    public:
        report(string);
        void do_report(string);
    private:
        ofstream file;
        string name;
};

#endif // REPORT_H
