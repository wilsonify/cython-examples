#define PY_SSIZE_T_CLEAN
#include <Python.h>

int main(void)
{
    setenv("PYTHONPATH", ".", 1); // Set PYTHONPATH TO working directory
    PyObject *pName, *pModule, *pFunc;
    PyObject *pArgs, *pValue;
    int i;

    Py_Initialize();
    pName = PyUnicode_DecodeFSDefault("arbitrary");

    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL)
    {
        pFunc = PyObject_GetAttrString(pModule, "multiply"); /* pFunc is a new reference */

        if (pFunc && PyCallable_Check(pFunc))
        {
            pArgs = PyTuple_New(2);
            PyTuple_SetItem(pArgs, 0, PyLong_FromLong(4));
            PyTuple_SetItem(pArgs, 1, PyLong_FromLong(5));
        }
        pValue = PyObject_CallObject(pFunc, pArgs);
        Py_DECREF(pArgs);
        if (pValue != NULL)
        {
            printf("Result of call: %ld\n", PyLong_AsLong(pValue));
            Py_DECREF(pValue);
        }
        else
        {
            Py_DECREF(pFunc);
            Py_DECREF(pModule);
            PyErr_Print();
            fprintf(stderr, "Call failed\n");
            return 1;
        }
    }
    else
    {
        if (PyErr_Occurred())
            PyErr_Print();
        fprintf(stderr, "Cannot find function \n");
    }
    Py_XDECREF(pFunc);
    Py_DECREF(pModule);

    if (Py_FinalizeEx() < 0)
    {
        return 120;
    }
    return 0;
}