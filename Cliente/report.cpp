#include "report.h"

report::report(string name){
    this->file.open("/home/vboxuser/Cliente/"+name+".txt");
    this->name = name;
    this->file.close();
}

void report::do_report(string text){
    this->file.open("/home/vboxuser/Cliente/"+this->name+".txt",ios::app);
    this->file<<text<<endl;
    this->file.close();
}
