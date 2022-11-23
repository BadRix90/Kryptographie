#include <Python.h>

int main(int argc, char *argv[])
    {
    char *ergebnis;
    PyObject *modul, *funk, *prm, *ret;
    Py_Initialize();
    PySys_SetPath(L".");
    modul = PyImport_ImportModule("script");
    if(modul)
        {
        funk = PyObject_GetAttrString(modul, "entscheide");
        prm = Py_BuildValue("(yy)", "Hallo", "Welt");
        ret = PyObject_CallObject(funk, prm);
        ergebnis = PyBytes_AsString(ret);
        printf("Das Script hat sich fuer '%s' entschieden\n", ergebnis);
        Py_DECREF(prm);
        Py_DECREF(ret);
        Py_DECREF(funk);
        Py_DECREF(modul);
        }
    else
        printf("Fehler: Modul nicht gefunden\n");
    Py_Finalize();
    }
