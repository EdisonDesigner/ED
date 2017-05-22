/****************************************************************************
** Meta object code from reading C++ file 'TaskSketcherMessages.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "TaskSketcherMessages.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TaskSketcherMessages.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_SketcherGui__TaskSketcherMessages[] = {

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
      35,   34,   34,   34, 0x08,
      88,   82,   34,   34, 0x08,
     128,  120,   34,   34, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_SketcherGui__TaskSketcherMessages[] = {
    "SketcherGui::TaskSketcherMessages\0\0"
    "on_labelConstrainStatus_linkActivated(QString)\0"
    "state\0on_autoUpdate_stateChanged(int)\0"
    "checked\0on_manualUpdate_clicked(bool)\0"
};

void SketcherGui::TaskSketcherMessages::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        TaskSketcherMessages *_t = static_cast<TaskSketcherMessages *>(_o);
        switch (_id) {
        case 0: _t->on_labelConstrainStatus_linkActivated((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->on_autoUpdate_stateChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->on_manualUpdate_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData SketcherGui::TaskSketcherMessages::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SketcherGui::TaskSketcherMessages::staticMetaObject = {
    { &Gui::TaskView::TaskBox::staticMetaObject, qt_meta_stringdata_SketcherGui__TaskSketcherMessages,
      qt_meta_data_SketcherGui__TaskSketcherMessages, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SketcherGui::TaskSketcherMessages::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SketcherGui::TaskSketcherMessages::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SketcherGui::TaskSketcherMessages::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SketcherGui__TaskSketcherMessages))
        return static_cast<void*>(const_cast< TaskSketcherMessages*>(this));
    typedef Gui::TaskView::TaskBox QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int SketcherGui::TaskSketcherMessages::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::TaskView::TaskBox QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
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
