
// This file is generated by src/Tools/generateTemaplates/templateClassPyExport.py out of the XML file
// Every change you make here get lost at the next full rebuild!
#ifndef BASE_UNITPY_H
#define BASE_UNITPY_H

#include "PyObjectBase.h"
#include "Unit.h"
#include <string>

namespace Base
{

//===========================================================================
// UnitPy - Python wrapper
//===========================================================================

/** The python export class for Unit
 */
class BaseExport UnitPy : public Base::PyObjectBase
{
public:
    static PyTypeObject   Type;
    static PyMethodDef    Methods[];
    static PyNumberMethods Number[];
    static PyObject * richCompare(PyObject *v, PyObject *w, int op);
    static PyGetSetDef    GetterSetter[];
    virtual PyTypeObject *GetType(void) {return &Type;};

public:
    UnitPy(Unit *pcObject, PyTypeObject *T = &Type);
    static PyObject *PyMake(struct _typeobject *, PyObject *, PyObject *);
    virtual int PyInit(PyObject* args, PyObject*k);
    ~UnitPy();

    typedef Unit* PointerType ;

    virtual PyObject *_repr(void);        // the representation
    std::string representation(void) const;

    /** @name callbacks and implementers for the python object methods */
    //@{
    //@}

    /** @name callbacks and implementers for the python object number protocol */
    //@{
    /// callback for the number_add_handler
    static PyObject * number_add_handler (PyObject *self, PyObject *other);
    /// callback for the number_subtract_handler
    static PyObject * number_subtract_handler (PyObject *self, PyObject *other);
    /// callback for the number_multiply_handler
    static PyObject * number_multiply_handler (PyObject *self, PyObject *other);
    /// callback for the number_divide_handler
    static PyObject * number_divide_handler (PyObject *self, PyObject *other);
    /// callback for the number_remainder_handler
    static PyObject * number_remainder_handler (PyObject *self, PyObject *other);
    /// callback for the number_divmod_handler
    static PyObject * number_divmod_handler (PyObject *self, PyObject *other);
    /// callback for the number_power_handler
    static PyObject * number_power_handler (PyObject *self, PyObject *other, PyObject *modulo);
    /// callback for the number_negative_handler
    static PyObject * number_negative_handler (PyObject *self);
    /// callback for the number_positive_handler
    static PyObject * number_positive_handler (PyObject *self);
    /// callback for the number_absolute_handler
    static PyObject * number_absolute_handler (PyObject *self);
    /// callback for the number_nonzero_handler
    static int number_nonzero_handler (PyObject *self);
    /// callback for the number_invert_handler
    static PyObject * number_invert_handler (PyObject *self);
    /// callback for the number_lshift_handler
    static PyObject * number_lshift_handler (PyObject *self, PyObject *other);
    /// callback for the number_rshift_handler
    static PyObject * number_rshift_handler (PyObject *self, PyObject *other);
    /// callback for the number_and_handler
    static PyObject * number_and_handler (PyObject *self, PyObject *other);
    /// callback for the number_xor_handler
    static PyObject * number_xor_handler (PyObject *self, PyObject *other);
    /// callback for the number_or_handler
    static PyObject * number_or_handler (PyObject *self, PyObject *other);
    /// callback for the number_coerce_handler
    static int number_coerce_handler (PyObject **self, PyObject **other);
    /// callback for the number_int_handler
    static PyObject * number_int_handler (PyObject *self);
    /// callback for the number_long_handler
    static PyObject * number_long_handler (PyObject *self);
    /// callback for the number_float_handler
    static PyObject * number_float_handler (PyObject *self);
    /// callback for the number_oct_handler
    static PyObject * number_oct_handler (PyObject *self);
    /// callback for the number_hex_handler
    static PyObject * number_hex_handler (PyObject *self);
    //@}

    /** @name callbacks and implementers for the python object attributes */
    //@{
    ///getter callback for the Type attribute
    static PyObject * staticCallback_getType (PyObject *self, void *closure);
    /// getter for the Type attribute
    Py::String getType(void) const;
    /// setter callback for the Type attribute
    static int staticCallback_setType (PyObject *self, PyObject *value, void *closure);
    // no setter method,  Type is read only!
    //@}

    /// getter method for special attributes (e.g. dynamic ones)
    PyObject *getCustomAttributes(const char* attr) const;
    /// setter for special attributes (e.g. dynamic ones)
    /// Output: Success=1, Failure=-1, Ignore=0
    int setCustomAttributes(const char* attr, PyObject *obj);
    PyObject *_getattr(char *attr);              // __getattr__ function
    int _setattr(char *attr, PyObject *value);        // __setattr__ function

    /// getter for the object handled by this class
    Unit *getUnitPtr(void) const;

    /** @name additional declarations and methods for the wrapper class */
    //@{

    //@}
};

}  //namespace Base

#endif  // BASE_UNITPY_H


