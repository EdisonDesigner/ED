
// This file is generated by src/Tools/generateTemaplates/templateClassPyExport.py out of the XML file
// Every change you make here get lost at the next full rebuild!
#ifndef BASE_BOUNDBOXPY_H
#define BASE_BOUNDBOXPY_H

#include "PyObjectBase.h"
#include "BoundBox.h"
#include <string>

namespace Base
{

//===========================================================================
// BoundBoxPy - Python wrapper
//===========================================================================

/** The python export class for BoundBox
 */
class BaseExport BoundBoxPy : public Base::PyObjectBase
{
public:
    static PyTypeObject   Type;
    static PyMethodDef    Methods[];
    static PyGetSetDef    GetterSetter[];
    virtual PyTypeObject *GetType(void) {return &Type;};

public:
    BoundBoxPy(BoundBox3d *pcObject, PyTypeObject *T = &Type);
    static PyObject *PyMake(struct _typeobject *, PyObject *, PyObject *);
    virtual int PyInit(PyObject* args, PyObject*k);
    ~BoundBoxPy();

    typedef BoundBox3d* PointerType ;

    virtual PyObject *_repr(void);        // the representation
    std::string representation(void) const;

    /** @name callbacks and implementers for the python object methods */
    //@{
    /// callback for the setVoid() method
    static PyObject * staticCallback_setVoid (PyObject *self, PyObject *args);
    /// implementer for the setVoid() method
    PyObject*  setVoid(PyObject *args);
    /// callback for the isValid() method
    static PyObject * staticCallback_isValid (PyObject *self, PyObject *args);
    /// implementer for the isValid() method
    PyObject*  isValid(PyObject *args);
    /// callback for the add() method
    static PyObject * staticCallback_add (PyObject *self, PyObject *args);
    /// implementer for the add() method
    PyObject*  add(PyObject *args);
    /// callback for the getPoint() method
    static PyObject * staticCallback_getPoint (PyObject *self, PyObject *args);
    /// implementer for the getPoint() method
    PyObject*  getPoint(PyObject *args);
    /// callback for the getEdge() method
    static PyObject * staticCallback_getEdge (PyObject *self, PyObject *args);
    /// implementer for the getEdge() method
    PyObject*  getEdge(PyObject *args);
    /// callback for the closestPoint() method
    static PyObject * staticCallback_closestPoint (PyObject *self, PyObject *args);
    /// implementer for the closestPoint() method
    PyObject*  closestPoint(PyObject *args);
    /// callback for the intersect() method
    static PyObject * staticCallback_intersect (PyObject *self, PyObject *args);
    /// implementer for the intersect() method
    PyObject*  intersect(PyObject *args);
    /// callback for the intersected() method
    static PyObject * staticCallback_intersected (PyObject *self, PyObject *args);
    /// implementer for the intersected() method
    PyObject*  intersected(PyObject *args);
    /// callback for the united() method
    static PyObject * staticCallback_united (PyObject *self, PyObject *args);
    /// implementer for the united() method
    PyObject*  united(PyObject *args);
    /// callback for the enlarge() method
    static PyObject * staticCallback_enlarge (PyObject *self, PyObject *args);
    /// implementer for the enlarge() method
    PyObject*  enlarge(PyObject *args);
    /// callback for the getIntersectionPoint() method
    static PyObject * staticCallback_getIntersectionPoint (PyObject *self, PyObject *args);
    /// implementer for the getIntersectionPoint() method
    PyObject*  getIntersectionPoint(PyObject *args);
    /// callback for the move() method
    static PyObject * staticCallback_move (PyObject *self, PyObject *args);
    /// implementer for the move() method
    PyObject*  move(PyObject *args);
    /// callback for the scale() method
    static PyObject * staticCallback_scale (PyObject *self, PyObject *args);
    /// implementer for the scale() method
    PyObject*  scale(PyObject *args);
    /// callback for the transformed() method
    static PyObject * staticCallback_transformed (PyObject *self, PyObject *args);
    /// implementer for the transformed() method
    PyObject*  transformed(PyObject *args);
    /// callback for the isCutPlane() method
    static PyObject * staticCallback_isCutPlane (PyObject *self, PyObject *args);
    /// implementer for the isCutPlane() method
    PyObject*  isCutPlane(PyObject *args);
    /// callback for the isInside() method
    static PyObject * staticCallback_isInside (PyObject *self, PyObject *args);
    /// implementer for the isInside() method
    PyObject*  isInside(PyObject *args);
    //@}


    /** @name callbacks and implementers for the python object attributes */
    //@{
    ///getter callback for the Center attribute
    static PyObject * staticCallback_getCenter (PyObject *self, void *closure);
    /// getter for the Center attribute
    Py::Object getCenter(void) const;
    /// setter callback for the Center attribute
    static int staticCallback_setCenter (PyObject *self, PyObject *value, void *closure);
    // no setter method,  Center is read only!
    ///getter callback for the XMax attribute
    static PyObject * staticCallback_getXMax (PyObject *self, void *closure);
    /// getter for the XMax attribute
    Py::Float getXMax(void) const;
    /// setter callback for the XMax attribute
    static int staticCallback_setXMax (PyObject *self, PyObject *value, void *closure);
    /// setter for the XMax attribute
    void setXMax(Py::Float arg);
    ///getter callback for the YMax attribute
    static PyObject * staticCallback_getYMax (PyObject *self, void *closure);
    /// getter for the YMax attribute
    Py::Float getYMax(void) const;
    /// setter callback for the YMax attribute
    static int staticCallback_setYMax (PyObject *self, PyObject *value, void *closure);
    /// setter for the YMax attribute
    void setYMax(Py::Float arg);
    ///getter callback for the ZMax attribute
    static PyObject * staticCallback_getZMax (PyObject *self, void *closure);
    /// getter for the ZMax attribute
    Py::Float getZMax(void) const;
    /// setter callback for the ZMax attribute
    static int staticCallback_setZMax (PyObject *self, PyObject *value, void *closure);
    /// setter for the ZMax attribute
    void setZMax(Py::Float arg);
    ///getter callback for the XMin attribute
    static PyObject * staticCallback_getXMin (PyObject *self, void *closure);
    /// getter for the XMin attribute
    Py::Float getXMin(void) const;
    /// setter callback for the XMin attribute
    static int staticCallback_setXMin (PyObject *self, PyObject *value, void *closure);
    /// setter for the XMin attribute
    void setXMin(Py::Float arg);
    ///getter callback for the YMin attribute
    static PyObject * staticCallback_getYMin (PyObject *self, void *closure);
    /// getter for the YMin attribute
    Py::Float getYMin(void) const;
    /// setter callback for the YMin attribute
    static int staticCallback_setYMin (PyObject *self, PyObject *value, void *closure);
    /// setter for the YMin attribute
    void setYMin(Py::Float arg);
    ///getter callback for the ZMin attribute
    static PyObject * staticCallback_getZMin (PyObject *self, void *closure);
    /// getter for the ZMin attribute
    Py::Float getZMin(void) const;
    /// setter callback for the ZMin attribute
    static int staticCallback_setZMin (PyObject *self, PyObject *value, void *closure);
    /// setter for the ZMin attribute
    void setZMin(Py::Float arg);
    ///getter callback for the XLength attribute
    static PyObject * staticCallback_getXLength (PyObject *self, void *closure);
    /// getter for the XLength attribute
    Py::Float getXLength(void) const;
    /// setter callback for the XLength attribute
    static int staticCallback_setXLength (PyObject *self, PyObject *value, void *closure);
    // no setter method,  XLength is read only!
    ///getter callback for the YLength attribute
    static PyObject * staticCallback_getYLength (PyObject *self, void *closure);
    /// getter for the YLength attribute
    Py::Float getYLength(void) const;
    /// setter callback for the YLength attribute
    static int staticCallback_setYLength (PyObject *self, PyObject *value, void *closure);
    // no setter method,  YLength is read only!
    ///getter callback for the ZLength attribute
    static PyObject * staticCallback_getZLength (PyObject *self, void *closure);
    /// getter for the ZLength attribute
    Py::Float getZLength(void) const;
    /// setter callback for the ZLength attribute
    static int staticCallback_setZLength (PyObject *self, PyObject *value, void *closure);
    // no setter method,  ZLength is read only!
    ///getter callback for the DiagonalLength attribute
    static PyObject * staticCallback_getDiagonalLength (PyObject *self, void *closure);
    /// getter for the DiagonalLength attribute
    Py::Float getDiagonalLength(void) const;
    /// setter callback for the DiagonalLength attribute
    static int staticCallback_setDiagonalLength (PyObject *self, PyObject *value, void *closure);
    // no setter method,  DiagonalLength is read only!
    //@}

    /// getter method for special attributes (e.g. dynamic ones)
    PyObject *getCustomAttributes(const char* attr) const;
    /// setter for special attributes (e.g. dynamic ones)
    /// Output: Success=1, Failure=-1, Ignore=0
    int setCustomAttributes(const char* attr, PyObject *obj);
    PyObject *_getattr(char *attr);              // __getattr__ function
    int _setattr(char *attr, PyObject *value);        // __setattr__ function

    /// getter for the object handled by this class
    BoundBox3d *getBoundBoxPtr(void) const;

    /** @name additional declarations and methods for the wrapper class */
    //@{

    //@}
};

}  //namespace Base

#endif  // BASE_BOUNDBOXPY_H

