/****************************************************************************
** Meta object code from reading C++ file 'GraphvizView.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "GraphvizView.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'GraphvizView.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__GraphvizView[] = {

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
      24,   19,   18,   18, 0x08,
      48,   18,   18,   18, 0x08,
      56,   18,   18,   18, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__GraphvizView[] = {
    "Gui::GraphvizView\0\0data\0svgFileRead(QByteArray)\0"
    "error()\0done()\0"
};

void Gui::GraphvizView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        GraphvizView *_t = static_cast<GraphvizView *>(_o);
        switch (_id) {
        case 0: _t->svgFileRead((*reinterpret_cast< const QByteArray(*)>(_a[1]))); break;
        case 1: _t->error(); break;
        case 2: _t->done(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::GraphvizView::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::GraphvizView::staticMetaObject = {
    { &MDIView::staticMetaObject, qt_meta_stringdata_Gui__GraphvizView,
      qt_meta_data_Gui__GraphvizView, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::GraphvizView::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::GraphvizView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::GraphvizView::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__GraphvizView))
        return static_cast<void*>(const_cast< GraphvizView*>(this));
    return MDIView::qt_metacast(_clname);
}

int Gui::GraphvizView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = MDIView::qt_metacall(_c, _id, _a);
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
