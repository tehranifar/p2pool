#include <Python.h>

//#include "Lyra2Z.h"

static PyObject *lyra2_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
    PyStringObject *input;
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

    lyra2z_hash((char *)PyString_AsString((PyObject*) input), output);
    Py_DECREF(input);
    value = Py_BuildValue("s#", output, 32);
    PyMem_Free(output);
    return value;
}

static PyMethodDef Lyra2Methods[] = {
    { "getPoWHash", lyra2z_hash, METH_VARARGS, "Returns the proof of work hash using Lyra2" },
    { NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC initxzc_lyra2(void) {
    (void) Py_InitModule("xzc_lyra2", Lyra2Methods);
}
