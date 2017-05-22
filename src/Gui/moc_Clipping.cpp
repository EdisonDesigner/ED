/****************************************************************************
** Meta object code from reading C++ file 'Clipping.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "Clipping.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'Clipping.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__Dialog__Clipping[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      16,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      23,   22,   22,   22, 0x09,
      50,   22,   22,   22, 0x09,
      77,   22,   22,   22, 0x09,
     104,   22,   22,   22, 0x09,
     134,   22,   22,   22, 0x09,
     164,   22,   22,   22, 0x09,
     194,   22,   22,   22, 0x09,
     217,   22,   22,   22, 0x09,
     240,   22,   22,   22, 0x09,
     263,   22,   22,   22, 0x09,
     293,   22,   22,   22, 0x09,
     326,   22,   22,   22, 0x09,
     348,   22,   22,   22, 0x09,
     385,   22,   22,   22, 0x09,
     414,   22,   22,   22, 0x09,
     443,   22,   22,   22, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_Gui__Dialog__Clipping[] = {
    "Gui::Dialog::Clipping\0\0"
    "on_groupBoxX_toggled(bool)\0"
    "on_groupBoxY_toggled(bool)\0"
    "on_groupBoxZ_toggled(bool)\0"
    "on_clipX_valueChanged(double)\0"
    "on_clipY_valueChanged(double)\0"
    "on_clipZ_valueChanged(double)\0"
    "on_flipClipX_clicked()\0on_flipClipY_clicked()\0"
    "on_flipClipZ_clicked()\0"
    "on_groupBoxView_toggled(bool)\0"
    "on_clipView_valueChanged(double)\0"
    "on_fromView_clicked()\0"
    "on_adjustViewdirection_toggled(bool)\0"
    "on_dirX_valueChanged(double)\0"
    "on_dirY_valueChanged(double)\0"
    "on_dirZ_valueChanged(double)\0"
};

void Gui::Dialog::Clipping::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        Clipping *_t = static_cast<Clipping *>(_o);
        switch (_id) {
        case 0: _t->on_groupBoxX_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->on_groupBoxY_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->on_groupBoxZ_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->on_clipX_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 4: _t->on_clipY_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 5: _t->on_clipZ_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 6: _t->on_flipClipX_clicked(); break;
        case 7: _t->on_flipClipY_clicked(); break;
        case 8: _t->on_flipClipZ_clicked(); break;
        case 9: _t->on_groupBoxView_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->on_clipView_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 11: _t->on_fromView_clicked(); break;
        case 12: _t->on_adjustViewdirection_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 13: _t->on_dirX_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 14: _t->on_dirY_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 15: _t->on_dirZ_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::Dialog::Clipping::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::Clipping::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_Gui__Dialog__Clipping,
      qt_meta_data_Gui__Dialog__Clipping, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::Clipping::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::Clipping::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::Clipping::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__Clipping))
        return static_cast<void*>(const_cast< Clipping*>(this));
    return QWidget::qt_metacast(_clname);
}

int Gui::Dialog::Clipping::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 16)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 16;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

