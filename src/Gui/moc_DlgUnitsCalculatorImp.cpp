/****************************************************************************
** Meta object code from reading C++ file 'DlgUnitsCalculatorImp.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "DlgUnitsCalculatorImp.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DlgUnitsCalculatorImp.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__Dialog__DlgUnitsCalculator[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      33,   32,   32,   32, 0x09,
      66,   32,   32,   32, 0x09,
      95,   32,   32,   32, 0x09,
     102,   32,   32,   32, 0x09,
     109,   32,   32,   32, 0x09,
     135,  125,   32,   32, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_Gui__Dialog__DlgUnitsCalculator[] = {
    "Gui::Dialog::DlgUnitsCalculator\0\0"
    "unitValueChanged(Base::Quantity)\0"
    "valueChanged(Base::Quantity)\0copy()\0"
    "help()\0returnPressed()\0errorText\0"
    "parseError(QString)\0"
};

void Gui::Dialog::DlgUnitsCalculator::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DlgUnitsCalculator *_t = static_cast<DlgUnitsCalculator *>(_o);
        switch (_id) {
        case 0: _t->unitValueChanged((*reinterpret_cast< const Base::Quantity(*)>(_a[1]))); break;
        case 1: _t->valueChanged((*reinterpret_cast< const Base::Quantity(*)>(_a[1]))); break;
        case 2: _t->copy(); break;
        case 3: _t->help(); break;
        case 4: _t->returnPressed(); break;
        case 5: _t->parseError((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::Dialog::DlgUnitsCalculator::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::DlgUnitsCalculator::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_Gui__Dialog__DlgUnitsCalculator,
      qt_meta_data_Gui__Dialog__DlgUnitsCalculator, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::DlgUnitsCalculator::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::DlgUnitsCalculator::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::DlgUnitsCalculator::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__DlgUnitsCalculator))
        return static_cast<void*>(const_cast< DlgUnitsCalculator*>(this));
    if (!strcmp(_clname, "Ui_DlgUnitCalculator"))
        return static_cast< Ui_DlgUnitCalculator*>(const_cast< DlgUnitsCalculator*>(this));
    return QDialog::qt_metacast(_clname);
}

int Gui::Dialog::DlgUnitsCalculator::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

