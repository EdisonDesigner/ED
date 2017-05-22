/****************************************************************************
** Meta object code from reading C++ file 'InputField.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "InputField.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'InputField.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__InputField[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       7,   39, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       3,       // signalCount

 // signals: signature, parameters, type, tag, flags
      17,   16,   16,   16, 0x05,
      46,   16,   16,   16, 0x05,
      77,   67,   16,   16, 0x05,

 // slots: signature, parameters, type, tag, flags
     102,   97,   16,   16, 0x09,
     120,   97,   16,   16, 0x09,

 // properties: name, type, flags
     156,  145, 0x0c095003,
     172,  165, 0x06095103,
     183,  165, 0x06095103,
     191,  165, 0x06095103,
     203,  199, 0x02095103,
     223,  215, 0x0a095003,
     243,  228, 0x0009500b,

       0        // eod
};

static const char qt_meta_stringdata_Gui__InputField[] = {
    "Gui::InputField\0\0valueChanged(Base::Quantity)\0"
    "valueChanged(double)\0errorText\0"
    "parseError(QString)\0text\0newInput(QString)\0"
    "updateIconLabel(QString)\0QByteArray\0"
    "prefPath\0double\0singleStep\0maximum\0"
    "minimum\0int\0historySize\0QString\0unit\0"
    "Base::Quantity\0quantity\0"
};

void Gui::InputField::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        InputField *_t = static_cast<InputField *>(_o);
        switch (_id) {
        case 0: _t->valueChanged((*reinterpret_cast< const Base::Quantity(*)>(_a[1]))); break;
        case 1: _t->valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 2: _t->parseError((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->newInput((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 4: _t->updateIconLabel((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::InputField::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::InputField::staticMetaObject = {
    { &ExpressionLineEdit::staticMetaObject, qt_meta_stringdata_Gui__InputField,
      qt_meta_data_Gui__InputField, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::InputField::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::InputField::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::InputField::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__InputField))
        return static_cast<void*>(const_cast< InputField*>(this));
    if (!strcmp(_clname, "ExpressionBinding"))
        return static_cast< ExpressionBinding*>(const_cast< InputField*>(this));
    return ExpressionLineEdit::qt_metacast(_clname);
}

int Gui::InputField::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = ExpressionLineEdit::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
#ifndef QT_NO_PROPERTIES
      else if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< QByteArray*>(_v) = paramGrpPath(); break;
        case 1: *reinterpret_cast< double*>(_v) = singleStep(); break;
        case 2: *reinterpret_cast< double*>(_v) = maximum(); break;
        case 3: *reinterpret_cast< double*>(_v) = minimum(); break;
        case 4: *reinterpret_cast< int*>(_v) = historySize(); break;
        case 5: *reinterpret_cast< QString*>(_v) = getUnitText(); break;
        case 6: *reinterpret_cast< Base::Quantity*>(_v) = getQuantity(); break;
        }
        _id -= 7;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setParamGrpPath(*reinterpret_cast< QByteArray*>(_v)); break;
        case 1: setSingleStep(*reinterpret_cast< double*>(_v)); break;
        case 2: setMaximum(*reinterpret_cast< double*>(_v)); break;
        case 3: setMinimum(*reinterpret_cast< double*>(_v)); break;
        case 4: setHistorySize(*reinterpret_cast< int*>(_v)); break;
        case 5: setUnitText(*reinterpret_cast< QString*>(_v)); break;
        case 6: setValue(*reinterpret_cast< Base::Quantity*>(_v)); break;
        }
        _id -= 7;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 7;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 7;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}

// SIGNAL 0
void Gui::InputField::valueChanged(const Base::Quantity & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void Gui::InputField::valueChanged(double _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void Gui::InputField::parseError(const QString & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}
QT_END_MOC_NAMESPACE

