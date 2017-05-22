/****************************************************************************
** Meta object code from reading C++ file 'SelectionView.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "SelectionView.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'SelectionView.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__DockWnd__SelectionView[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      34,   29,   28,   28, 0x0a,
      56,   50,   28,   28, 0x0a,
      87,   82,   28,   28, 0x0a,
     112,   28,   28,   28, 0x2a,
     121,   28,   28,   28, 0x0a,
     132,   28,   28,   28, 0x0a,
     139,   28,   28,   28, 0x0a,
     152,   28,   28,   28, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_Gui__DockWnd__SelectionView[] = {
    "Gui::DockWnd::SelectionView\0\0text\0"
    "search(QString)\0point\0onItemContextMenu(QPoint)\0"
    "item\0select(QListWidgetItem*)\0select()\0"
    "deselect()\0zoom()\0treeSelect()\0"
    "toPython()\0"
};

void Gui::DockWnd::SelectionView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        SelectionView *_t = static_cast<SelectionView *>(_o);
        switch (_id) {
        case 0: _t->search((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->onItemContextMenu((*reinterpret_cast< const QPoint(*)>(_a[1]))); break;
        case 2: _t->select((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 3: _t->select(); break;
        case 4: _t->deselect(); break;
        case 5: _t->zoom(); break;
        case 6: _t->treeSelect(); break;
        case 7: _t->toPython(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::DockWnd::SelectionView::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::DockWnd::SelectionView::staticMetaObject = {
    { &Gui::DockWindow::staticMetaObject, qt_meta_stringdata_Gui__DockWnd__SelectionView,
      qt_meta_data_Gui__DockWnd__SelectionView, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::DockWnd::SelectionView::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::DockWnd::SelectionView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::DockWnd::SelectionView::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__DockWnd__SelectionView))
        return static_cast<void*>(const_cast< SelectionView*>(this));
    if (!strcmp(_clname, "Gui::SelectionSingleton::ObserverType"))
        return static_cast< Gui::SelectionSingleton::ObserverType*>(const_cast< SelectionView*>(this));
    typedef Gui::DockWindow QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int Gui::DockWnd::SelectionView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::DockWindow QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

