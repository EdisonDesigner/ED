
// This file is generated by src/Tools/generateTemaplates/templateClassPyExport.py out of the XML file
// Every change you make here get lost at the next full rebuild!
#ifndef PART_GEOMETRYSURFACEPY_H
#define PART_GEOMETRYSURFACEPY_H

#include <Mod/Part/App/GeometryPy.h>
#include <Mod/Part/App/Geometry.h>
#include <string>

namespace Part
{

//===========================================================================
// GeometrySurfacePy - Python wrapper
//===========================================================================

/** The python export class for GeomSurface
 */
class PartExport GeometrySurfacePy : public Part::GeometryPy
{
public:
    static PyTypeObject   Type;
    static PyMethodDef    Methods[];
    static PyGetSetDef    GetterSetter[];
    virtual PyTypeObject *GetType(void) {return &Type;};

public:
    GeometrySurfacePy(GeomSurface *pcObject, PyTypeObject *T = &Type);
    static PyObject *PyMake(struct _typeobject *, PyObject *, PyObject *);
    virtual int PyInit(PyObject* args, PyObject*k);
    ~GeometrySurfacePy();

    typedef GeomSurface* PointerType ;

    virtual PyObject *_repr(void);        // the representation
    std::string representation(void) const;

    /** @name callbacks and implementers for the python object methods */
    //@{
    /// callback for the toShape() method
    static PyObject * staticCallback_toShape (PyObject *self, PyObject *args);
    /// implementer for the toShape() method
    PyObject*  toShape(PyObject *args);
    /// callback for the value() method
    static PyObject * staticCallback_value (PyObject *self, PyObject *args);
    /// implementer for the value() method
    PyObject*  value(PyObject *args);
    /// callback for the tangent() method
    static PyObject * staticCallback_tangent (PyObject *self, PyObject *args);
    /// implementer for the tangent() method
    PyObject*  tangent(PyObject *args);
    /// callback for the bounds() method
    static PyObject * staticCallback_bounds (PyObject *self, PyObject *args);
    /// implementer for the bounds() method
    PyObject*  bounds(PyObject *args);
    /// callback for the isUPeriodic() method
    static PyObject * staticCallback_isUPeriodic (PyObject *self, PyObject *args);
    /// implementer for the isUPeriodic() method
    PyObject*  isUPeriodic(PyObject *args);
    /// callback for the isVPeriodic() method
    static PyObject * staticCallback_isVPeriodic (PyObject *self, PyObject *args);
    /// implementer for the isVPeriodic() method
    PyObject*  isVPeriodic(PyObject *args);
    /// callback for the isUClosed() method
    static PyObject * staticCallback_isUClosed (PyObject *self, PyObject *args);
    /// implementer for the isUClosed() method
    PyObject*  isUClosed(PyObject *args);
    /// callback for the isVClosed() method
    static PyObject * staticCallback_isVClosed (PyObject *self, PyObject *args);
    /// implementer for the isVClosed() method
    PyObject*  isVClosed(PyObject *args);
    /// callback for the UPeriod() method
    static PyObject * staticCallback_UPeriod (PyObject *self, PyObject *args);
    /// implementer for the UPeriod() method
    PyObject*  UPeriod(PyObject *args);
    /// callback for the VPeriod() method
    static PyObject * staticCallback_VPeriod (PyObject *self, PyObject *args);
    /// implementer for the VPeriod() method
    PyObject*  VPeriod(PyObject *args);
    /// callback for the parameter() method
    static PyObject * staticCallback_parameter (PyObject *self, PyObject *args);
    /// implementer for the parameter() method
    PyObject*  parameter(PyObject *args);
    /// callback for the toBSpline() method
    static PyObject * staticCallback_toBSpline (PyObject *self, PyObject *args);
    /// implementer for the toBSpline() method
    PyObject*  toBSpline(PyObject *args);
    //@}


    /** @name callbacks and implementers for the python object attributes */
    //@{
    ///getter callback for the Continuity attribute
    static PyObject * staticCallback_getContinuity (PyObject *self, void *closure);
    /// getter for the Continuity attribute
    Py::String getContinuity(void) const;
    /// setter callback for the Continuity attribute
    static int staticCallback_setContinuity (PyObject *self, PyObject *value, void *closure);
    // no setter method,  Continuity is read only!
    //@}

    /// getter method for special attributes (e.g. dynamic ones)
    PyObject *getCustomAttributes(const char* attr) const;
    /// setter for special attributes (e.g. dynamic ones)
    /// Output: Success=1, Failure=-1, Ignore=0
    int setCustomAttributes(const char* attr, PyObject *obj);
    PyObject *_getattr(char *attr);              // __getattr__ function
    int _setattr(char *attr, PyObject *value);        // __setattr__ function

    /// getter for the object handled by this class
    GeomSurface *getGeomSurfacePtr(void) const;

    /** @name additional declarations and methods for the wrapper class */
    //@{

    //@}
};

}  //namespace Part

#endif  // PART_GEOMETRYSURFACEPY_H


