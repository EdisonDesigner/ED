/****************************************************************************
** Meta object code from reading C++ file 'SpinBox.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "SpinBox.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'SpinBox.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__UnsignedValidator[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       2,   14, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // properties: name, type, flags
      28,   23, 0x03095103,
      35,   23, 0x03095103,

       0        // eod
};

static const char qt_meta_stringdata_Gui__UnsignedValidator[] = {
    "Gui::UnsignedValidator\0uint\0bottom\0"
    "top\0"
};

void Gui::UnsignedValidator::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::UnsignedValidator::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::UnsignedValidator::staticMetaObject = {
    { &QValidator::staticMetaObject, qt_meta_stringdata_Gui__UnsignedValidator,
      qt_meta_data_Gui__UnsignedValidator, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::UnsignedValidator::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::UnsignedValidator::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::UnsignedValidator::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__UnsignedValidator))
        return static_cast<void*>(const_cast< UnsignedValidator*>(this));
    return QValidator::qt_metacast(_clname);
}

int Gui::UnsignedValidator::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QValidator::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    
#ifndef QT_NO_PROPERTIES
     if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< uint*>(_v) = bottom(); break;
        case 1: *reinterpret_cast< uint*>(_v) = top(); break;
        }
        _id -= 2;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setBottom(*reinterpret_cast< uint*>(_v)); break;
        case 1: setTop(*reinterpret_cast< uint*>(_v)); break;
        }
        _id -= 2;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 2;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}
static const uint qt_meta_data_Gui__UIntSpinBox[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      24,   18,   17,   17, 0x05,

 // slots: signature, parameters, type, tag, flags
      43,   18,   17,   17, 0x0a,
      58,   18,   17,   17, 0x08,
      75,   17,   17,   17, 0x08,
      97,   17,   17,   17, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__UIntSpinBox[] = {
    "Gui::UIntSpinBox\0\0value\0valueChanged(uint)\0"
    "setValue(uint)\0valueChange(int)\0"
    "finishFormulaDialog()\0openFormulaDialog()\0"
};

void Gui::UIntSpinBox::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        UIntSpinBox *_t = static_cast<UIntSpinBox *>(_o);
        switch (_id) {
        case 0: _t->valueChanged((*reinterpret_cast< uint(*)>(_a[1]))); break;
        case 1: _t->setValue((*reinterpret_cast< uint(*)>(_a[1]))); break;
        case 2: _t->valueChange((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->finishFormulaDialog(); break;
        case 4: _t->openFormulaDialog(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::UIntSpinBox::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::UIntSpinBox::staticMetaObject = {
    { &QSpinBox::staticMetaObject, qt_meta_stringdata_Gui__UIntSpinBox,
      qt_meta_data_Gui__UIntSpinBox, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::UIntSpinBox::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::UIntSpinBox::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::UIntSpinBox::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__UIntSpinBox))
        return static_cast<void*>(const_cast< UIntSpinBox*>(this));
    if (!strcmp(_clname, "ExpressionBinding"))
        return static_cast< ExpressionBinding*>(const_cast< UIntSpinBox*>(this));
    return QSpinBox::qt_metacast(_clname);
}

int Gui::UIntSpinBox::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSpinBox::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void Gui::UIntSpinBox::valueChanged(uint _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
static const uint qt_meta_data_Gui__IntSpinBox[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      17,   16,   16,   16, 0x08,
      39,   16,   16,   16, 0x08,
      59,   16,   16,   16, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__IntSpinBox[] = {
    "Gui::IntSpinBox\0\0finishFormulaDialog()\0"
    "openFormulaDialog()\0onChange()\0"
};

void Gui::IntSpinBox::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        IntSpinBox *_t = static_cast<IntSpinBox *>(_o);
        switch (_id) {
        case 0: _t->finishFormulaDialog(); break;
        case 1: _t->openFormulaDialog(); break;
        case 2: _t->onChange(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::IntSpinBox::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::IntSpinBox::staticMetaObject = {
    { &QSpinBox::staticMetaObject, qt_meta_stringdata_Gui__IntSpinBox,
      qt_meta_data_Gui__IntSpinBox, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::IntSpinBox::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::IntSpinBox::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::IntSpinBox::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__IntSpinBox))
        return static_cast<void*>(const_cast< IntSpinBox*>(this));
    if (!strcmp(_clname, "ExpressionBinding"))
        return static_cast< ExpressionBinding*>(const_cast< IntSpinBox*>(this));
    return QSpinBox::qt_metacast(_clname);
}

int Gui::IntSpinBox::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSpinBox::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}
static const uint qt_meta_data_Gui__DoubleSpinBox[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      20,   19,   19,   19, 0x08,
      42,   19,   19,   19, 0x08,
      62,   19,   19,   19, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__DoubleSpinBox[] = {
    "Gui::DoubleSpinBox\0\0finishFormulaDialog()\0"
    "openFormulaDialog()\0onChange()\0"
};

void Gui::DoubleSpinBox::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DoubleSpinBox *_t = static_cast<DoubleSpinBox *>(_o);
        switch (_id) {
        case 0: _t->finishFormulaDialog(); break;
        case 1: _t->openFormulaDialog(); break;
        case 2: _t->onChange(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::DoubleSpinBox::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::DoubleSpinBox::staticMetaObject = {
    { &QDoubleSpinBox::staticMetaObject, qt_meta_stringdata_Gui__DoubleSpinBox,
      qt_meta_data_Gui__DoubleSpinBox, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::DoubleSpinBox::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::DoubleSpinBox::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::DoubleSpinBox::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__DoubleSpinBox))
        return static_cast<void*>(const_cast< DoubleSpinBox*>(this));
    if (!strcmp(_clname, "ExpressionBinding"))
        return static_cast< ExpressionBinding*>(const_cast< DoubleSpinBox*>(this));
    return QDoubleSpinBox::qt_metacast(_clname);
}

int Gui::DoubleSpinBox::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDoubleSpinBox::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

