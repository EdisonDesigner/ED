
// This file is generated by src/Tools/generateTemaplates/templateClassPyExport.py out of the .XML file
// Every change you make here get lost at the next full rebuild!
// This File is normaly build as an include in FacetPyImp.cpp! Its not intended to be in a project!

#include <boost/filesystem/path.hpp>
#include <boost/filesystem/operations.hpp>
#include <boost/filesystem/exception.hpp>
#include <Base/PyObjectBase.h>
#include <Base/Console.h>
#include <Base/Exception.h>
#include <CXX/Objects.hxx>

using Base::streq;
using namespace Mesh;

/// Type structure of FacetPy
PyTypeObject FacetPy::Type = {
    PyObject_HEAD_INIT(&PyType_Type)
    0,                                                /*ob_size*/
    "Mesh.Facet",     /*tp_name*/
    sizeof(FacetPy),                       /*tp_basicsize*/
    0,                                                /*tp_itemsize*/
    /* methods */
    PyDestructor,                                     /*tp_dealloc*/
    0,                                                /*tp_print*/
    __getattr,                                        /*tp_getattr*/
    __setattr,                                        /*tp_setattr*/
    0,                                                /*tp_compare*/
    __repr,                                           /*tp_repr*/
    0,                                                /*tp_as_number*/
    0,                                                /*tp_as_sequence*/
    0,                                                /*tp_as_mapping*/
    0,                                                /*tp_hash*/
    0,                                                /*tp_call */
    0,                                                /*tp_str  */
    0,                                                /*tp_getattro*/
    0,                                                /*tp_setattro*/
    /* --- Functions to access object as input/output buffer ---------*/
    0,                                                /* tp_as_buffer */
    /* --- Flags to define presence of optional/expanded features */
    Py_TPFLAGS_HAVE_CLASS,        /*tp_flags */
    "Facet in mesh\n"
    "This is a facet in a MeshObject. You can get it by e.g. iterating a\n"
    "mesh. The facet has a connection to its mesh and allows therefore\n"
    "topological operations. It is also possible to create an unbounded facet e.g. to create\n"
    "a mesh. In this case the topological operations will fail. The same is\n"
    "when you cut the bound to the mesh by calling unbound().\n"
    "		",           /*tp_doc */
    0,                                                /*tp_traverse */
    0,                                                /*tp_clear */
    0,                                                /*tp_richcompare */
    0,                                                /*tp_weaklistoffset */
    0,                                                /*tp_iter */
    0,                                                /*tp_iternext */
    Mesh::FacetPy::Methods,                     /*tp_methods */
    0,                                                /*tp_members */
    Mesh::FacetPy::GetterSetter,                     /*tp_getset */
    &Base::PyObjectBase::Type,                        /*tp_base */
    0,                                                /*tp_dict */
    0,                                                /*tp_descr_get */
    0,                                                /*tp_descr_set */
    0,                                                /*tp_dictoffset */
    __PyInit,                                         /*tp_init */
    0,                                                /*tp_alloc */
    Mesh::FacetPy::PyMake,/*tp_new */
    0,                                                /*tp_free   Low-level free-memory routine */
    0,                                                /*tp_is_gc  For PyObject_IS_GC */
    0,                                                /*tp_bases */
    0,                                                /*tp_mro    method resolution order */
    0,                                                /*tp_cache */
    0,                                                /*tp_subclasses */
    0,                                                /*tp_weaklist */
    0                                                 /*tp_del */
};

/// Methods structure of FacetPy
PyMethodDef FacetPy::Methods[] = {
    {"unbound",
        (PyCFunction) staticCallback_unbound,
        METH_VARARGS,
        "method unbound()\nCut the connection to a MeshObject. The facet becomes\nfree and is more or less a simple facet.\nAfter calling unbound() no topological operation will\nwork!\n			  "
    },
    {"intersect",
        (PyCFunction) staticCallback_intersect,
        METH_VARARGS,
        "intersect(Facet) -> list \nGet a list of intersection points with another triangle.\n			  "
    },
    {NULL, NULL, 0, NULL}		/* Sentinel */
};



/// Attribute structure of FacetPy
PyGetSetDef FacetPy::GetterSetter[] = {
    {"Index",
        (getter) staticCallback_getIndex,
        (setter) staticCallback_setIndex, 
        "The index of this facet in the MeshObject",
        NULL
    },
    {"Bound",
        (getter) staticCallback_getBound,
        (setter) staticCallback_setBound, 
        "Bound state of the facet",
        NULL
    },
    {"Normal",
        (getter) staticCallback_getNormal,
        (setter) staticCallback_setNormal, 
        "Normal vector of the facet.",
        NULL
    },
    {"Points",
        (getter) staticCallback_getPoints,
        (setter) staticCallback_setPoints, 
        "A list of points of the facet",
        NULL
    },
    {"PointIndices",
        (getter) staticCallback_getPointIndices,
        (setter) staticCallback_setPointIndices, 
        "The index tuple of point vertices of the mesh this facet is built of",
        NULL
    },
    {"NeighbourIndices",
        (getter) staticCallback_getNeighbourIndices,
        (setter) staticCallback_setNeighbourIndices, 
        "The index tuple of neighbour facets of the mesh this facet is adjacent with",
        NULL
    },
    {NULL, NULL, NULL, NULL, NULL}		/* Sentinel */
};

// unbound() callback and implementer
// PyObject*  FacetPy::unbound(PyObject *args){};
// has to be implemented in FacetPyImp.cpp
PyObject * FacetPy::staticCallback_unbound (PyObject *self, PyObject *args)
{
    // test if twin object not allready deleted
    if (!static_cast<PyObjectBase*>(self)->isValid()) {
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return NULL;
    }

    // test if object is set Const
    if (static_cast<PyObjectBase*>(self)->isConst()) {
        PyErr_SetString(PyExc_ReferenceError, "This object is immutable, you can not set any attribute or call a non const method");
        return NULL;
    }

    try { // catches all exceptions coming up from c++ and generate a python exception
        PyObject* ret = static_cast<FacetPy*>(self)->unbound(args);
        if (ret != 0)
            static_cast<FacetPy*>(self)->startNotify();
        return ret;
    }
    catch(const Base::Exception& e) // catch the EdisonDesigner exceptions
    {
        std::string str;
        str += "EdisonDesigner exception thrown (";
        str += e.what();
        str += ")";
        e.ReportException();
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(const boost::filesystem::filesystem_error& e) // catch boost filesystem exception
    {
        std::string str;
        str += "File system exception thrown (";
        //str += e.who();
        //str += ", ";
        str += e.what();
        str += ")\n";
        Base::Console().Error(str.c_str());
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(const Py::Exception&)
    {
        // The exception text is already set
        return NULL;
    }
    catch(const char* e) // catch simple string exceptions
    {
        Base::Console().Error(e);
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,e);
        return NULL;
    }
    // in debug not all exceptions will be catched to get the attention of the developer!
#ifndef DONT_CATCH_CXX_EXCEPTIONS 
    catch(const std::exception& e) // catch other c++ exceptions
    {
        std::string str;
        str += "ED++ exception thrown (";
        str += e.what();
        str += ")";
        Base::Console().Error(str.c_str());
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(...)  // catch the rest!
    {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,"Unknown C++ exception");
        return NULL;
    }
#endif
}

// intersect() callback and implementer
// PyObject*  FacetPy::intersect(PyObject *args){};
// has to be implemented in FacetPyImp.cpp
PyObject * FacetPy::staticCallback_intersect (PyObject *self, PyObject *args)
{
    // test if twin object not allready deleted
    if (!static_cast<PyObjectBase*>(self)->isValid()) {
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return NULL;
    }

    // test if object is set Const
    if (static_cast<PyObjectBase*>(self)->isConst()) {
        PyErr_SetString(PyExc_ReferenceError, "This object is immutable, you can not set any attribute or call a non const method");
        return NULL;
    }

    try { // catches all exceptions coming up from c++ and generate a python exception
        PyObject* ret = static_cast<FacetPy*>(self)->intersect(args);
        if (ret != 0)
            static_cast<FacetPy*>(self)->startNotify();
        return ret;
    }
    catch(const Base::Exception& e) // catch the EdisonDesigner exceptions
    {
        std::string str;
        str += "EdisonDesigner exception thrown (";
        str += e.what();
        str += ")";
        e.ReportException();
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(const boost::filesystem::filesystem_error& e) // catch boost filesystem exception
    {
        std::string str;
        str += "File system exception thrown (";
        //str += e.who();
        //str += ", ";
        str += e.what();
        str += ")\n";
        Base::Console().Error(str.c_str());
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(const Py::Exception&)
    {
        // The exception text is already set
        return NULL;
    }
    catch(const char* e) // catch simple string exceptions
    {
        Base::Console().Error(e);
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,e);
        return NULL;
    }
    // in debug not all exceptions will be catched to get the attention of the developer!
#ifndef DONT_CATCH_CXX_EXCEPTIONS 
    catch(const std::exception& e) // catch other c++ exceptions
    {
        std::string str;
        str += "ED++ exception thrown (";
        str += e.what();
        str += ")";
        Base::Console().Error(str.c_str());
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(...)  // catch the rest!
    {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,"Unknown C++ exception");
        return NULL;
    }
#endif
}

// Index() callback and implementer
// PyObject*  FacetPy::Index(PyObject *args){};
// has to be implemented in FacetPyImp.cpp
PyObject * FacetPy::staticCallback_getIndex (PyObject *self, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return NULL;
    }

    try {
        return Py::new_reference_to(static_cast<FacetPy*>(self)->getIndex());
    } catch (const Py::Exception&) {
        // The exception text is already set
        return NULL;
    } catch (...) {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError, "Unknown exception while reading attribute 'Index' of object 'Facet'");
        return NULL;
    }
}

int FacetPy::staticCallback_setIndex (PyObject *self, PyObject * /*value*/, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return -1;
    }

    PyErr_SetString(PyExc_AttributeError, "Attribute 'Index' of object 'Facet' is read-only");
    return -1;
}

// Bound() callback and implementer
// PyObject*  FacetPy::Bound(PyObject *args){};
// has to be implemented in FacetPyImp.cpp
PyObject * FacetPy::staticCallback_getBound (PyObject *self, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return NULL;
    }

    try {
        return Py::new_reference_to(static_cast<FacetPy*>(self)->getBound());
    } catch (const Py::Exception&) {
        // The exception text is already set
        return NULL;
    } catch (...) {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError, "Unknown exception while reading attribute 'Bound' of object 'Facet'");
        return NULL;
    }
}

int FacetPy::staticCallback_setBound (PyObject *self, PyObject * /*value*/, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return -1;
    }

    PyErr_SetString(PyExc_AttributeError, "Attribute 'Bound' of object 'Facet' is read-only");
    return -1;
}

// Normal() callback and implementer
// PyObject*  FacetPy::Normal(PyObject *args){};
// has to be implemented in FacetPyImp.cpp
PyObject * FacetPy::staticCallback_getNormal (PyObject *self, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return NULL;
    }

    try {
        return Py::new_reference_to(static_cast<FacetPy*>(self)->getNormal());
    } catch (const Py::Exception&) {
        // The exception text is already set
        return NULL;
    } catch (...) {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError, "Unknown exception while reading attribute 'Normal' of object 'Facet'");
        return NULL;
    }
}

int FacetPy::staticCallback_setNormal (PyObject *self, PyObject * /*value*/, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return -1;
    }

    PyErr_SetString(PyExc_AttributeError, "Attribute 'Normal' of object 'Facet' is read-only");
    return -1;
}

// Points() callback and implementer
// PyObject*  FacetPy::Points(PyObject *args){};
// has to be implemented in FacetPyImp.cpp
PyObject * FacetPy::staticCallback_getPoints (PyObject *self, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return NULL;
    }

    try {
        return Py::new_reference_to(static_cast<FacetPy*>(self)->getPoints());
    } catch (const Py::Exception&) {
        // The exception text is already set
        return NULL;
    } catch (...) {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError, "Unknown exception while reading attribute 'Points' of object 'Facet'");
        return NULL;
    }
}

int FacetPy::staticCallback_setPoints (PyObject *self, PyObject * /*value*/, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return -1;
    }

    PyErr_SetString(PyExc_AttributeError, "Attribute 'Points' of object 'Facet' is read-only");
    return -1;
}

// PointIndices() callback and implementer
// PyObject*  FacetPy::PointIndices(PyObject *args){};
// has to be implemented in FacetPyImp.cpp
PyObject * FacetPy::staticCallback_getPointIndices (PyObject *self, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return NULL;
    }

    try {
        return Py::new_reference_to(static_cast<FacetPy*>(self)->getPointIndices());
    } catch (const Py::Exception&) {
        // The exception text is already set
        return NULL;
    } catch (...) {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError, "Unknown exception while reading attribute 'PointIndices' of object 'Facet'");
        return NULL;
    }
}

int FacetPy::staticCallback_setPointIndices (PyObject *self, PyObject * /*value*/, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return -1;
    }

    PyErr_SetString(PyExc_AttributeError, "Attribute 'PointIndices' of object 'Facet' is read-only");
    return -1;
}

// NeighbourIndices() callback and implementer
// PyObject*  FacetPy::NeighbourIndices(PyObject *args){};
// has to be implemented in FacetPyImp.cpp
PyObject * FacetPy::staticCallback_getNeighbourIndices (PyObject *self, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return NULL;
    }

    try {
        return Py::new_reference_to(static_cast<FacetPy*>(self)->getNeighbourIndices());
    } catch (const Py::Exception&) {
        // The exception text is already set
        return NULL;
    } catch (...) {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError, "Unknown exception while reading attribute 'NeighbourIndices' of object 'Facet'");
        return NULL;
    }
}

int FacetPy::staticCallback_setNeighbourIndices (PyObject *self, PyObject * /*value*/, void * /*closure*/)
{
    if (!static_cast<PyObjectBase*>(self)->isValid()){
        PyErr_SetString(PyExc_ReferenceError, "This object is already deleted most likely through closing a document. This reference is no longer valid!");
        return -1;
    }

    PyErr_SetString(PyExc_AttributeError, "Attribute 'NeighbourIndices' of object 'Facet' is read-only");
    return -1;
}




//--------------------------------------------------------------------------
// Constructor
//--------------------------------------------------------------------------
FacetPy::FacetPy(Facet *pcObject, PyTypeObject *T)
    : PyObjectBase(static_cast<PyObjectBase::PointerType>(pcObject), T)
{
}


//--------------------------------------------------------------------------
// destructor
//--------------------------------------------------------------------------
FacetPy::~FacetPy()                                // Everything handled in parent
{
    // delete the handled object when the PyObject dies
    FacetPy::PointerType ptr = static_cast<FacetPy::PointerType>(_pcTwinPointer);
    delete ptr;
}

//--------------------------------------------------------------------------
// FacetPy representation
//--------------------------------------------------------------------------
PyObject *FacetPy::_repr(void)
{
    return Py_BuildValue("s", representation().c_str());
}

//--------------------------------------------------------------------------
// FacetPy Attributes
//--------------------------------------------------------------------------
PyObject *FacetPy::_getattr(char *attr)				// __getattr__ function: note only need to handle new state
{
    try {
        // getter method for special Attributes (e.g. dynamic ones)
        PyObject *r = getCustomAttributes(attr);
        if(r) return r;
    }
#ifndef DONT_CATCH_CXX_EXCEPTIONS 
    catch(const Base::Exception& e) // catch the EdisonDesigner exceptions
    {
        std::string str;
        str += "EdisonDesigner exception thrown (";
        str += e.what();
        str += ")";
        e.ReportException();
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(const std::exception& e) // catch other c++ exceptions
    {
        std::string str;
        str += "ED++ exception thrown (";
        str += e.what();
        str += ")";
        Base::Console().Error(str.c_str());
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(const Py::Exception&)
    {
        // The exception text is already set
        return NULL;
    }
    catch(...)  // catch the rest!
    {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,"Unknown C++ exception");
        return NULL;
    }
#else  // DONT_CATCH_CXX_EXCEPTIONS  
    catch(const Base::Exception& e) // catch the EdisonDesigner exceptions
    {
        std::string str;
        str += "EdisonDesigner exception thrown (";
        str += e.what();
        str += ")";
        e.ReportException();
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return NULL;
    }
    catch(const Py::Exception&)
    {
        // The exception text is already set
        return NULL;
    }
#endif  // DONT_CATCH_CXX_EXCEPTIONS

    PyObject *rvalue = Py_FindMethod(Methods, this, attr);
    if (rvalue == NULL)
    {
        PyErr_Clear();
        return PyObjectBase::_getattr(attr);
    }
    else
    {
        return rvalue;
    }
}

int FacetPy::_setattr(char *attr, PyObject *value) // __setattr__ function: note only need to handle new state
{
    try {
        // setter for  special Attributes (e.g. dynamic ones)
        int r = setCustomAttributes(attr, value);
        // r = 1: handled
        // r = -1: error
        // r = 0: ignore
        if (r == 1)
            return 0;
        else if (r == -1)
            return -1;
    }
#ifndef DONT_CATCH_CXX_EXCEPTIONS 
    catch(const Base::Exception& e) // catch the EdisonDesigner exceptions
    {
        std::string str;
        str += "EdisonDesigner exception thrown (";
        str += e.what();
        str += ")";
        e.ReportException();
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return -1;
    }
    catch(const std::exception& e) // catch other c++ exceptions
    {
        std::string str;
        str += "ED++ exception thrown (";
        str += e.what();
        str += ")";
        Base::Console().Error(str.c_str());
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return -1;
    }
    catch(const Py::Exception&)
    {
        // The exception text is already set
        return -1;
    }
    catch(...)  // catch the rest!
    {
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,"Unknown C++ exception");
        return -1;
    }
#else  // DONT_CATCH_CXX_EXCEPTIONS  
    catch(const Base::Exception& e) // catch the EdisonDesigner exceptions
    {
        std::string str;
        str += "EdisonDesigner exception thrown (";
        str += e.what();
        str += ")";
        e.ReportException();
        PyErr_SetString(Base::BaseExceptionEdisonDesignerError,str.c_str());
        return -1;
    }
    catch(const Py::Exception&)
    {
        // The exception text is already set
        return -1;
    }
#endif  // DONT_CATCH_CXX_EXCEPTIONS

    return PyObjectBase::_setattr(attr, value);
}

Facet *FacetPy::getFacetPtr(void) const
{
    return static_cast<Facet *>(_pcTwinPointer);
}

#if 0
/* From here on come the methods you have to implement, but NOT in this module. Implement in FacetPyImp.cpp! This prototypes 
 * are just for convenience when you add a new method.
 */

PyObject *FacetPy::PyMake(struct _typeobject *, PyObject *, PyObject *)  // Python wrapper
{
    // create a new instance of FacetPy and the Twin object 
    return new FacetPy(new Facet);
}

// constructor method
int FacetPy::PyInit(PyObject* /*args*/, PyObject* /*kwd*/)
{
    return 0;
}

// returns a string which represents the object e.g. when printed in python
std::string FacetPy::representation(void) const
{
    return std::string("<Facet object>");
}

PyObject* FacetPy::unbound(PyObject *args)
{
    PyErr_SetString(PyExc_NotImplementedError, "Not yet implemented");
    return 0;
}

PyObject* FacetPy::intersect(PyObject *args)
{
    PyErr_SetString(PyExc_NotImplementedError, "Not yet implemented");
    return 0;
}



Py::Int FacetPy::getIndex(void) const
{
    //return Py::Int();
    throw Py::AttributeError("Not yet implemented");
}

Py::Boolean FacetPy::getBound(void) const
{
    //return Py::Boolean();
    throw Py::AttributeError("Not yet implemented");
}

Py::Object FacetPy::getNormal(void) const
{
    //return Py::Object();
    throw Py::AttributeError("Not yet implemented");
}

Py::List FacetPy::getPoints(void) const
{
    //return Py::List();
    throw Py::AttributeError("Not yet implemented");
}

Py::Tuple FacetPy::getPointIndices(void) const
{
    //return Py::Tuple();
    throw Py::AttributeError("Not yet implemented");
}

Py::Tuple FacetPy::getNeighbourIndices(void) const
{
    //return Py::Tuple();
    throw Py::AttributeError("Not yet implemented");
}

PyObject *FacetPy::getCustomAttributes(const char* attr) const
{
    return 0;
}

int FacetPy::setCustomAttributes(const char* attr, PyObject *obj)
{
    return 0; 
}
#endif



