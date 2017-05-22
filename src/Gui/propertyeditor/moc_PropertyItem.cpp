/****************************************************************************
** Meta object code from reading C++ file 'PropertyItem.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "PropertyItem.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'PropertyItem.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__PropertyEditor__PropertyItem[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

       0        // eod
};

static const char qt_meta_stringdata_Gui__PropertyEditor__PropertyItem[] = {
    "Gui::PropertyEditor::PropertyItem\0"
};

void Gui::PropertyEditor::PropertyItem::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::PropertyEditor::PropertyItem::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::PropertyEditor::PropertyItem::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_Gui__PropertyEditor__PropertyItem,
      qt_meta_data_Gui__PropertyEditor__PropertyItem, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::PropertyEditor::PropertyItem::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::PropertyEditor::PropertyItem::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::PropertyEditor::PropertyItem::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__PropertyEditor__PropertyItem))
        return static_cast<void*>(const_cast< PropertyItem*>(this));
    if (!strcmp(_clname, "Base::BaseClass"))
        return static_cast< Base::BaseClass*>(const_cast< PropertyItem*>(this));
    if (!strcmp(_clname, "ExpressionBinding"))
        return static_cast< ExpressionBinding*>(const_cast< PropertyItem*>(this));
    return QObject::qt_metacast(_clname);
}

int Gui::PropertyEditor::PropertyItem::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
static const uint qt_meta_data_Gui__PropertyEditor__PropertyVectorItem[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       3,   14, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // properties: name, type, flags
      47,   40, 0x06195103,
      49,   40, 0x06195103,
      51,   40, 0x06195103,

       0        // eod
};

static const char qt_meta_stringdata_Gui__PropertyEditor__PropertyVectorItem[] = {
    "Gui::PropertyEditor::PropertyVectorItem\0"
    "double\0x\0y\0z\0"
};

void Gui::PropertyEditor::PropertyVectorItem::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::PropertyEditor::PropertyVectorItem::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::PropertyEditor::PropertyVectorItem::staticMetaObject = {
    { &PropertyItem::staticMetaObject, qt_meta_stringdata_Gui__PropertyEditor__PropertyVectorItem,
      qt_meta_data_Gui__PropertyEditor__PropertyVectorItem, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::PropertyEditor::PropertyVectorItem::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::PropertyEditor::PropertyVectorItem::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::PropertyEditor::PropertyVectorItem::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__PropertyEditor__PropertyVectorItem))
        return static_cast<void*>(const_cast< PropertyVectorItem*>(this));
    return PropertyItem::qt_metacast(_clname);
}

int Gui::PropertyEditor::PropertyVectorItem::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = PropertyItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    
#ifndef QT_NO_PROPERTIES
     if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< double*>(_v) = x(); break;
        case 1: *reinterpret_cast< double*>(_v) = y(); break;
        case 2: *reinterpret_cast< double*>(_v) = z(); break;
        }
        _id -= 3;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setX(*reinterpret_cast< double*>(_v)); break;
        case 1: setY(*reinterpret_cast< double*>(_v)); break;
        case 2: setZ(*reinterpret_cast< double*>(_v)); break;
        }
        _id -= 3;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 3;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}
static const uint qt_meta_data_Gui__PropertyEditor__PropertyVectorDistanceItem[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       3,   14, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // properties: name, type, flags
      63,   48, 0x0019510b,
      65,   48, 0x0019510b,
      67,   48, 0x0019510b,

       0        // eod
};

static const char qt_meta_stringdata_Gui__PropertyEditor__PropertyVectorDistanceItem[] = {
    "Gui::PropertyEditor::PropertyVectorDistanceItem\0"
    "Base::Quantity\0x\0y\0z\0"
};

void Gui::PropertyEditor::PropertyVectorDistanceItem::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::PropertyEditor::PropertyVectorDistanceItem::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::PropertyEditor::PropertyVectorDistanceItem::staticMetaObject = {
    { &PropertyItem::staticMetaObject, qt_meta_stringdata_Gui__PropertyEditor__PropertyVectorDistanceItem,
      qt_meta_data_Gui__PropertyEditor__PropertyVectorDistanceItem, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::PropertyEditor::PropertyVectorDistanceItem::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::PropertyEditor::PropertyVectorDistanceItem::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::PropertyEditor::PropertyVectorDistanceItem::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__PropertyEditor__PropertyVectorDistanceItem))
        return static_cast<void*>(const_cast< PropertyVectorDistanceItem*>(this));
    return PropertyItem::qt_metacast(_clname);
}

int Gui::PropertyEditor::PropertyVectorDistanceItem::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = PropertyItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    
#ifndef QT_NO_PROPERTIES
     if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< Base::Quantity*>(_v) = x(); break;
        case 1: *reinterpret_cast< Base::Quantity*>(_v) = y(); break;
        case 2: *reinterpret_cast< Base::Quantity*>(_v) = z(); break;
        }
        _id -= 3;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setX(*reinterpret_cast< Base::Quantity*>(_v)); break;
        case 1: setY(*reinterpret_cast< Base::Quantity*>(_v)); break;
        case 2: setZ(*reinterpret_cast< Base::Quantity*>(_v)); break;
        }
        _id -= 3;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 3;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}
static const uint qt_meta_data_Gui__PropertyEditor__PropertyMatrixItem[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
      16,   14, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // properties: name, type, flags
      47,   40, 0x06195103,
      51,   40, 0x06195103,
      55,   40, 0x06195103,
      59,   40, 0x06195103,
      63,   40, 0x06195103,
      67,   40, 0x06195103,
      71,   40, 0x06195103,
      75,   40, 0x06195103,
      79,   40, 0x06195103,
      83,   40, 0x06195103,
      87,   40, 0x06195103,
      91,   40, 0x06195103,
      95,   40, 0x06195103,
      99,   40, 0x06195103,
     103,   40, 0x06195103,
     107,   40, 0x06195103,

       0        // eod
};

static const char qt_meta_stringdata_Gui__PropertyEditor__PropertyMatrixItem[] = {
    "Gui::PropertyEditor::PropertyMatrixItem\0"
    "double\0A11\0A12\0A13\0A14\0A21\0A22\0A23\0"
    "A24\0A31\0A32\0A33\0A34\0A41\0A42\0A43\0A44\0"
};

void Gui::PropertyEditor::PropertyMatrixItem::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::PropertyEditor::PropertyMatrixItem::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::PropertyEditor::PropertyMatrixItem::staticMetaObject = {
    { &PropertyItem::staticMetaObject, qt_meta_stringdata_Gui__PropertyEditor__PropertyMatrixItem,
      qt_meta_data_Gui__PropertyEditor__PropertyMatrixItem, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::PropertyEditor::PropertyMatrixItem::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::PropertyEditor::PropertyMatrixItem::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::PropertyEditor::PropertyMatrixItem::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__PropertyEditor__PropertyMatrixItem))
        return static_cast<void*>(const_cast< PropertyMatrixItem*>(this));
    return PropertyItem::qt_metacast(_clname);
}

int Gui::PropertyEditor::PropertyMatrixItem::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = PropertyItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    
#ifndef QT_NO_PROPERTIES
     if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< double*>(_v) = getA11(); break;
        case 1: *reinterpret_cast< double*>(_v) = getA12(); break;
        case 2: *reinterpret_cast< double*>(_v) = getA13(); break;
        case 3: *reinterpret_cast< double*>(_v) = getA14(); break;
        case 4: *reinterpret_cast< double*>(_v) = getA21(); break;
        case 5: *reinterpret_cast< double*>(_v) = getA22(); break;
        case 6: *reinterpret_cast< double*>(_v) = getA23(); break;
        case 7: *reinterpret_cast< double*>(_v) = getA24(); break;
        case 8: *reinterpret_cast< double*>(_v) = getA31(); break;
        case 9: *reinterpret_cast< double*>(_v) = getA32(); break;
        case 10: *reinterpret_cast< double*>(_v) = getA33(); break;
        case 11: *reinterpret_cast< double*>(_v) = getA34(); break;
        case 12: *reinterpret_cast< double*>(_v) = getA41(); break;
        case 13: *reinterpret_cast< double*>(_v) = getA42(); break;
        case 14: *reinterpret_cast< double*>(_v) = getA43(); break;
        case 15: *reinterpret_cast< double*>(_v) = getA44(); break;
        }
        _id -= 16;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setA11(*reinterpret_cast< double*>(_v)); break;
        case 1: setA12(*reinterpret_cast< double*>(_v)); break;
        case 2: setA13(*reinterpret_cast< double*>(_v)); break;
        case 3: setA14(*reinterpret_cast< double*>(_v)); break;
        case 4: setA21(*reinterpret_cast< double*>(_v)); break;
        case 5: setA22(*reinterpret_cast< double*>(_v)); break;
        case 6: setA23(*reinterpret_cast< double*>(_v)); break;
        case 7: setA24(*reinterpret_cast< double*>(_v)); break;
        case 8: setA31(*reinterpret_cast< double*>(_v)); break;
        case 9: setA32(*reinterpret_cast< double*>(_v)); break;
        case 10: setA33(*reinterpret_cast< double*>(_v)); break;
        case 11: setA34(*reinterpret_cast< double*>(_v)); break;
        case 12: setA41(*reinterpret_cast< double*>(_v)); break;
        case 13: setA42(*reinterpret_cast< double*>(_v)); break;
        case 14: setA43(*reinterpret_cast< double*>(_v)); break;
        case 15: setA44(*reinterpret_cast< double*>(_v)); break;
        }
        _id -= 16;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 16;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 16;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 16;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 16;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 16;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 16;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}
static const uint qt_meta_data_Gui__PropertyEditor__PlacementEditor[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      42,   38,   37,   37, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__PropertyEditor__PlacementEditor[] = {
    "Gui::PropertyEditor::PlacementEditor\0"
    "\0v,,\0updateValue(QVariant,bool,bool)\0"
};

void Gui::PropertyEditor::PlacementEditor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        PlacementEditor *_t = static_cast<PlacementEditor *>(_o);
        switch (_id) {
        case 0: _t->updateValue((*reinterpret_cast< const QVariant(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2])),(*reinterpret_cast< bool(*)>(_a[3]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::PropertyEditor::PlacementEditor::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::PropertyEditor::PlacementEditor::staticMetaObject = {
    { &Gui::LabelButton::staticMetaObject, qt_meta_stringdata_Gui__PropertyEditor__PlacementEditor,
      qt_meta_data_Gui__PropertyEditor__PlacementEditor, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::PropertyEditor::PlacementEditor::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::PropertyEditor::PlacementEditor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::PropertyEditor::PlacementEditor::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__PropertyEditor__PlacementEditor))
        return static_cast<void*>(const_cast< PlacementEditor*>(this));
    typedef Gui::LabelButton QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int Gui::PropertyEditor::PlacementEditor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::LabelButton QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
static const uint qt_meta_data_Gui__PropertyEditor__PropertyPlacementItem[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       3,   14, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // properties: name, type, flags
      58,   43, 0x0019510b,
      79,   64, 0x0019510b,
      84,   64, 0x0019510b,

       0        // eod
};

static const char qt_meta_stringdata_Gui__PropertyEditor__PropertyPlacementItem[] = {
    "Gui::PropertyEditor::PropertyPlacementItem\0"
    "Base::Quantity\0Angle\0Base::Vector3d\0"
    "Axis\0Position\0"
};

void Gui::PropertyEditor::PropertyPlacementItem::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::PropertyEditor::PropertyPlacementItem::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::PropertyEditor::PropertyPlacementItem::staticMetaObject = {
    { &PropertyItem::staticMetaObject, qt_meta_stringdata_Gui__PropertyEditor__PropertyPlacementItem,
      qt_meta_data_Gui__PropertyEditor__PropertyPlacementItem, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::PropertyEditor::PropertyPlacementItem::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::PropertyEditor::PropertyPlacementItem::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::PropertyEditor::PropertyPlacementItem::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__PropertyEditor__PropertyPlacementItem))
        return static_cast<void*>(const_cast< PropertyPlacementItem*>(this));
    return PropertyItem::qt_metacast(_clname);
}

int Gui::PropertyEditor::PropertyPlacementItem::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = PropertyItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    
#ifndef QT_NO_PROPERTIES
     if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< Base::Quantity*>(_v) = getAngle(); break;
        case 1: *reinterpret_cast< Base::Vector3d*>(_v) = getAxis(); break;
        case 2: *reinterpret_cast< Base::Vector3d*>(_v) = getPosition(); break;
        }
        _id -= 3;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setAngle(*reinterpret_cast< Base::Quantity*>(_v)); break;
        case 1: setAxis(*reinterpret_cast< Base::Vector3d*>(_v)); break;
        case 2: setPosition(*reinterpret_cast< Base::Vector3d*>(_v)); break;
        }
        _id -= 3;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 3;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 3;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}
static const uint qt_meta_data_Gui__PropertyEditor__LinkSelection[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      36,   35,   35,   35, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_Gui__PropertyEditor__LinkSelection[] = {
    "Gui::PropertyEditor::LinkSelection\0\0"
    "select()\0"
};

void Gui::PropertyEditor::LinkSelection::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        LinkSelection *_t = static_cast<LinkSelection *>(_o);
        switch (_id) {
        case 0: _t->select(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::PropertyEditor::LinkSelection::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::PropertyEditor::LinkSelection::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_Gui__PropertyEditor__LinkSelection,
      qt_meta_data_Gui__PropertyEditor__LinkSelection, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::PropertyEditor::LinkSelection::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::PropertyEditor::LinkSelection::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::PropertyEditor::LinkSelection::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__PropertyEditor__LinkSelection))
        return static_cast<void*>(const_cast< LinkSelection*>(this));
    return QObject::qt_metacast(_clname);
}

int Gui::PropertyEditor::LinkSelection::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
static const uint qt_meta_data_Gui__PropertyEditor__LinkLabel[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      32,   31,   31,   31, 0x05,

 // slots: signature, parameters, type, tag, flags
      57,   31,   31,   31, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_Gui__PropertyEditor__LinkLabel[] = {
    "Gui::PropertyEditor::LinkLabel\0\0"
    "linkChanged(QStringList)\0"
    "onLinkActivated(QString)\0"
};

void Gui::PropertyEditor::LinkLabel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        LinkLabel *_t = static_cast<LinkLabel *>(_o);
        switch (_id) {
        case 0: _t->linkChanged((*reinterpret_cast< const QStringList(*)>(_a[1]))); break;
        case 1: _t->onLinkActivated((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::PropertyEditor::LinkLabel::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::PropertyEditor::LinkLabel::staticMetaObject = {
    { &QLabel::staticMetaObject, qt_meta_stringdata_Gui__PropertyEditor__LinkLabel,
      qt_meta_data_Gui__PropertyEditor__LinkLabel, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::PropertyEditor::LinkLabel::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::PropertyEditor::LinkLabel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::PropertyEditor::LinkLabel::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__PropertyEditor__LinkLabel))
        return static_cast<void*>(const_cast< LinkLabel*>(this));
    return QLabel::qt_metacast(_clname);
}

int Gui::PropertyEditor::LinkLabel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QLabel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void Gui::PropertyEditor::LinkLabel::linkChanged(const QStringList & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_END_MOC_NAMESPACE

