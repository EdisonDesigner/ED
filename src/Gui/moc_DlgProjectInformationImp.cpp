/****************************************************************************
** Meta object code from reading C++ file 'DlgProjectInformationImp.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "DlgProjectInformationImp.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DlgProjectInformationImp.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__Dialog__DlgProjectInformationImp[] = {

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
      39,   38,   38,   38, 0x08,
      56,   50,   38,   38, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__Dialog__DlgProjectInformationImp[] = {
    "Gui::Dialog::DlgProjectInformationImp\0"
    "\0open_url()\0index\0onLicenseTypeChanged(int)\0"
};

void Gui::Dialog::DlgProjectInformationImp::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DlgProjectInformationImp *_t = static_cast<DlgProjectInformationImp *>(_o);
        switch (_id) {
        case 0: _t->open_url(); break;
        case 1: _t->onLicenseTypeChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::Dialog::DlgProjectInformationImp::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::DlgProjectInformationImp::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_Gui__Dialog__DlgProjectInformationImp,
      qt_meta_data_Gui__Dialog__DlgProjectInformationImp, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::DlgProjectInformationImp::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::DlgProjectInformationImp::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::DlgProjectInformationImp::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__DlgProjectInformationImp))
        return static_cast<void*>(const_cast< DlgProjectInformationImp*>(this));
    return QDialog::qt_metacast(_clname);
}

int Gui::Dialog::DlgProjectInformationImp::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
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

