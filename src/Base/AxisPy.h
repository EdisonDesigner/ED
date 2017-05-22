
// This file is generated by src/Tools/generateTemaplates/templateClassPyExport.py out of the XML file
// Every change you make here get lost at the next full rebuild!
#ifndef BASE_AXISPY_H
#define BASE_AXISPY_H

#include "PyObjectBase.h"
#include "Axis.h"
#include <string>

namespace Base
{

//===========================================================================
// AxisPy - Python wrapper
//===========================================================================

/** The python export class for Axis
 */
class BaseExport AxisPy : public Base::PyObjectBase
{
public:
    static PyTypeObject   Type;
    static PyMethodDef    Methods[];
    static PyGetSetDef    GetterSetter[];
    virtual PyTypeObject *GetType(void) {return &Type;};

public:
    AxisPy(Axis *pcObject, PyTypeObject *T = &Type);
    static PyObject *PyMake(struct _typeobject *, PyObject *, PyObject *);
    virtual int PyInit(PyObject* args, PyObject*k);
    ~AxisPy();

    typedef Axis* PointerType ;

    virtual PyObject *_repr(void);        // the representation
    std::string representation(void) const;

    /** @name callbacks and implementers for the python object methods */
    //@{
    /// callback for the copy() method
    static PyObject * staticCallback_copy (PyObject *self, PyObject *args);
    /// implementer for the copy() method
    PyObject*  copy(PyObject *args);
    /// callback for the move() method
    static PyObject * staticCallback_move (PyObject *self, PyObject *args);
    /// implementer for the move() method
    PyObject*  move(PyObject *args);
    /// callback for the multiply() method
    static PyObject * staticCallback_multiply (PyObject *self, PyObject *args);
    /// implementer for the multiply() method
    PyObject*  multiply(PyObject *args);
    /// callback for the reversed() method
    static PyObject * staticCallback_reversed (PyObject *self, PyObject *args);
    /// implementer for the reversed() method
    PyObject*  reversed(PyObject *args);
    //@}


    /** @name callbacks and implementers for the python object attributes */
    //@{
    ///getter callback for the Base attribute
    static PyObject * staticCallback_getBase (PyObject *self, void *closure);
    /// getter for the Base attribute
    Py::Object getBase(void) const;
    /// setter callback for the Base attribute
    static int staticCallback_setBase (PyObject *self, PyObject *value, void *closure);
    /// setter for the Base attribute
    void setBase(Py::Object arg);
    ///getter callback for the Direction attribute
    static PyObject * staticCallback_getDirection (PyObject *self, void *closure);
    /// getter for the Direction attribute
    Py::Object getDirection(void) const;
    /// setter callback for the Direction attribute
    static int staticCallback_setDirection (PyObject *self, PyObject *value, void *closure);
    /// setter for the Direction attribute
    void setDirection(Py::Object arg);
    //@}

    /// getter method for special attributes (e.g. dynamic ones)
    PyObject *getCustomAttributes(const char* attr) const;
    /// setter for special attributes (e.g. dynamic ones)
    /// Output: Success=1, Failure=-1, Ignore=0
    int setCustomAttributes(const char* attr, PyObject *obj);
    PyObject *_getattr(char *attr);              // __getattr__ function
    int _setattr(char *attr, PyObject *value);        // __setattr__ function

    /// getter for the object handled by this class
    Axis *getAxisPtr(void) const;

    /** @name additional declarations and methods for the wrapper class */
    //@{

    //@}
};

}  //namespace Base

#endif  // BASE_AXISPY_H

