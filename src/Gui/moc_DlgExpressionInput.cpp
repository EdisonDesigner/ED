/****************************************************************************
** Meta object code from reading C++ file 'DlgExpressionInput.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "DlgExpressionInput.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DlgExpressionInput.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__Dialog__DlgExpressionInput[] = {

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
      38,   33,   32,   32, 0x08,
      59,   32,   32,   32, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__Dialog__DlgExpressionInput[] = {
    "Gui::Dialog::DlgExpressionInput\0\0text\0"
    "textChanged(QString)\0setDiscarded()\0"
};

void Gui::Dialog::DlgExpressionInput::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DlgExpressionInput *_t = static_cast<DlgExpressionInput *>(_o);
        switch (_id) {
        case 0: _t->textChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->setDiscarded(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::Dialog::DlgExpressionInput::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::DlgExpressionInput::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_Gui__Dialog__DlgExpressionInput,
      qt_meta_data_Gui__Dialog__DlgExpressionInput, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::DlgExpressionInput::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::DlgExpressionInput::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::DlgExpressionInput::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__DlgExpressionInput))
        return static_cast<void*>(const_cast< DlgExpressionInput*>(this));
    return QDialog::qt_metacast(_clname);
}

int Gui::Dialog::DlgExpressionInput::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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

