#include <Python.h>

const char *programm =
"import random\n"
"print('Guten Tag, die Zahl ist:', random.randint(0, 100))\n"
"print('Das war ... Python')\n";

int main(int argc, char *argv[])
    {
    Py_Initialize();
    PyRun_SimpleString(programm);
    Py_Finalize();
    }
