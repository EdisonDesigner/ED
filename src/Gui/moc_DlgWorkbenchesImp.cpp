/****************************************************************************
** Meta object code from reading C++ file 'DlgWorkbenchesImp.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "DlgWorkbenchesImp.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DlgWorkbenchesImp.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__Dialog__DlgWorkbenchesImp[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       9,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      32,   31,   31,   31, 0x09,
      61,   31,   31,   31, 0x09,
      93,   31,   31,   31, 0x09,
     125,   31,   31,   31, 0x09,
     169,   31,   31,   31, 0x09,
     218,   31,   31,   31, 0x09,
     254,   31,   31,   31, 0x09,
     292,   31,   31,   31, 0x09,
     334,   31,   31,   31, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_Gui__Dialog__DlgWorkbenchesImp[] = {
    "Gui::Dialog::DlgWorkbenchesImp\0\0"
    "onAddMacroAction(QByteArray)\0"
    "onRemoveMacroAction(QByteArray)\0"
    "onModifyMacroAction(QByteArray)\0"
    "on_add_to_enabled_workbenches_btn_clicked()\0"
    "on_remove_from_enabled_workbenches_btn_clicked()\0"
    "on_shift_workbench_up_btn_clicked()\0"
    "on_shift_workbench_down_btn_clicked()\0"
    "on_sort_enabled_workbenches_btn_clicked()\0"
    "on_add_all_to_enabled_workbenches_btn_clicked()\0"
};

void Gui::Dialog::DlgWorkbenchesImp::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DlgWorkbenchesImp *_t = static_cast<DlgWorkbenchesImp *>(_o);
        switch (_id) {
        case 0: _t->onAddMacroAction((*reinterpret_cast< const QByteArray(*)>(_a[1]))); break;
        case 1: _t->onRemoveMacroAction((*reinterpret_cast< const QByteArray(*)>(_a[1]))); break;
        case 2: _t->onModifyMacroAction((*reinterpret_cast< const QByteArray(*)>(_a[1]))); break;
        case 3: _t->on_add_to_enabled_workbenches_btn_clicked(); break;
        case 4: _t->on_remove_from_enabled_workbenches_btn_clicked(); break;
        case 5: _t->on_shift_workbench_up_btn_clicked(); break;
        case 6: _t->on_shift_workbench_down_btn_clicked(); break;
        case 7: _t->on_sort_enabled_workbenches_btn_clicked(); break;
        case 8: _t->on_add_all_to_enabled_workbenches_btn_clicked(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::Dialog::DlgWorkbenchesImp::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::DlgWorkbenchesImp::staticMetaObject = {
    { &CustomizeActionPage::staticMetaObject, qt_meta_stringdata_Gui__Dialog__DlgWorkbenchesImp,
      qt_meta_data_Gui__Dialog__DlgWorkbenchesImp, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::DlgWorkbenchesImp::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::DlgWorkbenchesImp::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::DlgWorkbenchesImp::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__DlgWorkbenchesImp))
        return static_cast<void*>(const_cast< DlgWorkbenchesImp*>(this));
    if (!strcmp(_clname, "Ui_DlgWorkbenches"))
        return static_cast< Ui_DlgWorkbenches*>(const_cast< DlgWorkbenchesImp*>(this));
    return CustomizeActionPage::qt_metacast(_clname);
}

int Gui::Dialog::DlgWorkbenchesImp::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = CustomizeActionPage::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

