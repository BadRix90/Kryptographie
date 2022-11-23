#include <Python.h>

static PyObject *testfunktion(PyObject *self, PyObject *args)
    {
    int a, b;
    if(!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    return Py_BuildValue("i", a + b);
    }

static PyMethodDef MethodTable[] =
    {
    {"testfunktion", testfunktion, METH_VARARGS, "Testfunktion"},
    {NULL, NULL, 0, NULL}
    };

static PyModuleDef APIModule =
    {
    PyModuleDef_HEAD_INIT,
    "api", NULL, -1, MethodTable
    };

static PyObject *PyInit_api()
    {
    return PyModule_Create(&APIModule);
    }

int main(int argc, char *argv[])
    {
    FILE *f;
    PyImport_AppendInittab("api", &PyInit_api);
    Py_Initialize();
    f = _Py_fopen("script.py", "r");
    PyRun_SimpleFile(f, "script.py");
    fclose(f);
    Py_Finalize();
    }
