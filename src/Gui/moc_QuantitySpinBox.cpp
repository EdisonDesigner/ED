/****************************************************************************
** Meta object code from reading C++ file 'QuantitySpinBox.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "QuantitySpinBox.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'QuantitySpinBox.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__QuantitySpinBox[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       5,   54, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      22,   21,   21,   21, 0x05,
      51,   21,   21,   21, 0x05,

 // slots: signature, parameters, type, tag, flags
      76,   72,   21,   21, 0x0a,
     101,   21,   21,   21, 0x0a,
     123,  118,   21,   21, 0x09,
     142,   21,   21,   21, 0x09,
     162,   21,   21,   21, 0x09,
     184,   21,   21,   21, 0x09,

 // properties: name, type, flags
     203,  195, 0x0a095003,
     215,  208, 0x06095103,
     223,  208, 0x06095103,
     231,  208, 0x06095103,
     257,  242, 0x0059510b,

 // properties: notify_signal_id
       0,
       0,
       0,
       0,
       0,

       0        // eod
};

static const char qt_meta_stringdata_Gui__QuantitySpinBox[] = {
    "Gui::QuantitySpinBox\0\0"
    "valueChanged(Base::Quantity)\0"
    "valueChanged(double)\0val\0"
    "setValue(Base::Quantity)\0setValue(double)\0"
    "text\0userInput(QString)\0openFormulaDialog()\0"
    "finishFormulaDialog()\0onChange()\0"
    "QString\0unit\0double\0minimum\0maximum\0"
    "singleStep\0Base::Quantity\0value\0"
};

void Gui::QuantitySpinBox::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        QuantitySpinBox *_t = static_cast<QuantitySpinBox *>(_o);
        switch (_id) {
        case 0: _t->valueChanged((*reinterpret_cast< const Base::Quantity(*)>(_a[1]))); break;
        case 1: _t->valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 2: _t->setValue((*reinterpret_cast< const Base::Quantity(*)>(_a[1]))); break;
        case 3: _t->setValue((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 4: _t->userInput((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->openFormulaDialog(); break;
        case 6: _t->finishFormulaDialog(); break;
        case 7: _t->onChange(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::QuantitySpinBox::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::QuantitySpinBox::staticMetaObject = {
    { &QAbstractSpinBox::staticMetaObject, qt_meta_stringdata_Gui__QuantitySpinBox,
      qt_meta_data_Gui__QuantitySpinBox, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::QuantitySpinBox::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::QuantitySpinBox::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::QuantitySpinBox::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__QuantitySpinBox))
        return static_cast<void*>(const_cast< QuantitySpinBox*>(this));
    if (!strcmp(_clname, "ExpressionBinding"))
        return static_cast< ExpressionBinding*>(const_cast< QuantitySpinBox*>(this));
    return QAbstractSpinBox::qt_metacast(_clname);
}

int Gui::QuantitySpinBox::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractSpinBox::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    }
#ifndef QT_NO_PROPERTIES
      else if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< QString*>(_v) = unitText(); break;
        case 1: *reinterpret_cast< double*>(_v) = minimum(); break;
        case 2: *reinterpret_cast< double*>(_v) = maximum(); break;
        case 3: *reinterpret_cast< double*>(_v) = singleStep(); break;
        case 4: *reinterpret_cast< Base::Quantity*>(_v) = value(); break;
        }
        _id -= 5;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setUnitText(*reinterpret_cast< QString*>(_v)); break;
        case 1: setMinimum(*reinterpret_cast< double*>(_v)); break;
        case 2: setMaximum(*reinterpret_cast< double*>(_v)); break;
        case 3: setSingleStep(*reinterpret_cast< double*>(_v)); break;
        case 4: setValue(*reinterpret_cast< Base::Quantity*>(_v)); break;
        }
        _id -= 5;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 5;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}

// SIGNAL 0
void Gui::QuantitySpinBox::valueChanged(const Base::Quantity & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void Gui::QuantitySpinBox::valueChanged(double _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_END_MOC_NAMESPACE

