/****************************************************************************
** Meta object code from reading C++ file 'Control.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "Control.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'Control.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__ControlSingleton[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      23,   22,   22,   22, 0x0a,
      32,   22,   22,   22, 0x0a,
      41,   22,   22,   22, 0x0a,
      55,   22,   22,   22, 0x0a,
      70,   22,   22,   22, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__ControlSingleton[] = {
    "Gui::ControlSingleton\0\0accept()\0"
    "reject()\0closeDialog()\0showTaskView()\0"
    "closedDialog()\0"
};

void Gui::ControlSingleton::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ControlSingleton *_t = static_cast<ControlSingleton *>(_o);
        switch (_id) {
        case 0: _t->accept(); break;
        case 1: _t->reject(); break;
        case 2: _t->closeDialog(); break;
        case 3: _t->showTaskView(); break;
        case 4: _t->closedDialog(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::ControlSingleton::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::ControlSingleton::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_Gui__ControlSingleton,
      qt_meta_data_Gui__ControlSingleton, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::ControlSingleton::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::ControlSingleton::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::ControlSingleton::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__ControlSingleton))
        return static_cast<void*>(const_cast< ControlSingleton*>(this));
    return QObject::qt_metacast(_clname);
}

int Gui::ControlSingleton::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

