/****************************************************************************
** Meta object code from reading C++ file 'DlgSettings3DViewImp.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "DlgSettings3DViewImp.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DlgSettings3DViewImp.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__Dialog__DlgSettings3DViewImp[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      35,   34,   34,   34, 0x08,
      60,   34,   34,   34, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__Dialog__DlgSettings3DViewImp[] = {
    "Gui::Dialog::DlgSettings3DViewImp\0\0"
    "on_mouseButton_clicked()\0"
    "onAliasingChanged(int)\0"
};

void Gui::Dialog::DlgSettings3DViewImp::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DlgSettings3DViewImp *_t = static_cast<DlgSettings3DViewImp *>(_o);
        switch (_id) {
        case 0: _t->on_mouseButton_clicked(); break;
        case 1: _t->onAliasingChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::Dialog::DlgSettings3DViewImp::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::DlgSettings3DViewImp::staticMetaObject = {
    { &PreferencePage::staticMetaObject, qt_meta_stringdata_Gui__Dialog__DlgSettings3DViewImp,
      qt_meta_data_Gui__Dialog__DlgSettings3DViewImp, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::DlgSettings3DViewImp::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::DlgSettings3DViewImp::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::DlgSettings3DViewImp::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__DlgSettings3DViewImp))
        return static_cast<void*>(const_cast< DlgSettings3DViewImp*>(this));
    if (!strcmp(_clname, "Ui_DlgSettings3DView"))
        return static_cast< Ui_DlgSettings3DView*>(const_cast< DlgSettings3DViewImp*>(this));
    return PreferencePage::qt_metacast(_clname);
}

int Gui::Dialog::DlgSettings3DViewImp::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = PreferencePage::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

