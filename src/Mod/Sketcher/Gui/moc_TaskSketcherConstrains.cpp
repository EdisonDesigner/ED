/****************************************************************************
** Meta object code from reading C++ file 'TaskSketcherConstrains.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "TaskSketcherConstrains.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TaskSketcherConstrains.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_SketcherGui__ConstraintView[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       9,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      41,   29,   28,   28, 0x05,
      86,   28,   28,   28, 0x05,

 // slots: signature, parameters, type, tag, flags
     112,   28,   28,   28, 0x09,
     132,   28,   28,   28, 0x09,
     152,   28,   28,   28, 0x09,
     174,   28,   28,   28, 0x09,
     196,   28,   28,   28, 0x09,
     218,   28,   28,   28, 0x09,
     240,   28,   28,   28, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_SketcherGui__ConstraintView[] = {
    "SketcherGui::ConstraintView\0\0item,status\0"
    "onUpdateDrivingStatus(QListWidgetItem*,bool)\0"
    "emitCenterSelectedItems()\0modifyCurrentItem()\0"
    "renameCurrentItem()\0centerSelectedItems()\0"
    "deleteSelectedItems()\0doSelectConstraints()\0"
    "updateDrivingStatus()\0swapNamedOfSelectedItems()\0"
};

void SketcherGui::ConstraintView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ConstraintView *_t = static_cast<ConstraintView *>(_o);
        switch (_id) {
        case 0: _t->onUpdateDrivingStatus((*reinterpret_cast< QListWidgetItem*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 1: _t->emitCenterSelectedItems(); break;
        case 2: _t->modifyCurrentItem(); break;
        case 3: _t->renameCurrentItem(); break;
        case 4: _t->centerSelectedItems(); break;
        case 5: _t->deleteSelectedItems(); break;
        case 6: _t->doSelectConstraints(); break;
        case 7: _t->updateDrivingStatus(); break;
        case 8: _t->swapNamedOfSelectedItems(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData SketcherGui::ConstraintView::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SketcherGui::ConstraintView::staticMetaObject = {
    { &QListWidget::staticMetaObject, qt_meta_stringdata_SketcherGui__ConstraintView,
      qt_meta_data_SketcherGui__ConstraintView, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SketcherGui::ConstraintView::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SketcherGui::ConstraintView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SketcherGui::ConstraintView::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SketcherGui__ConstraintView))
        return static_cast<void*>(const_cast< ConstraintView*>(this));
    return QListWidget::qt_metacast(_clname);
}

int SketcherGui::ConstraintView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QListWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    return _id;
}

// SIGNAL 0
void SketcherGui::ConstraintView::onUpdateDrivingStatus(QListWidgetItem * _t1, bool _t2)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void SketcherGui::ConstraintView::emitCenterSelectedItems()
{
    QMetaObject::activate(this, &staticMetaObject, 1, 0);
}
static const uint qt_meta_data_SketcherGui__TaskSketcherConstrains[] = {

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
      37,   36,   36,   36, 0x0a,
      80,   36,   36,   36, 0x0a,
     133,  128,   36,   36, 0x0a,
     190,  128,   36,   36, 0x0a,
     257,  245,   36,   36, 0x0a,
     325,   36,   36,   36, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_SketcherGui__TaskSketcherConstrains[] = {
    "SketcherGui::TaskSketcherConstrains\0"
    "\0on_comboBoxFilter_currentIndexChanged(int)\0"
    "on_listWidgetConstraints_itemSelectionChanged()\0"
    "item\0on_listWidgetConstraints_itemActivated(QListWidgetItem*)\0"
    "on_listWidgetConstraints_itemChanged(QListWidgetItem*)\0"
    "item,status\0"
    "on_listWidgetConstraints_updateDrivingStatus(QListWidgetItem*,bool)\0"
    "on_listWidgetConstraints_emitCenterSelectedItems()\0"
};

void SketcherGui::TaskSketcherConstrains::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        TaskSketcherConstrains *_t = static_cast<TaskSketcherConstrains *>(_o);
        switch (_id) {
        case 0: _t->on_comboBoxFilter_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->on_listWidgetConstraints_itemSelectionChanged(); break;
        case 2: _t->on_listWidgetConstraints_itemActivated((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 3: _t->on_listWidgetConstraints_itemChanged((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 4: _t->on_listWidgetConstraints_updateDrivingStatus((*reinterpret_cast< QListWidgetItem*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 5: _t->on_listWidgetConstraints_emitCenterSelectedItems(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData SketcherGui::TaskSketcherConstrains::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SketcherGui::TaskSketcherConstrains::staticMetaObject = {
    { &Gui::TaskView::TaskBox::staticMetaObject, qt_meta_stringdata_SketcherGui__TaskSketcherConstrains,
      qt_meta_data_SketcherGui__TaskSketcherConstrains, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SketcherGui::TaskSketcherConstrains::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SketcherGui::TaskSketcherConstrains::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SketcherGui::TaskSketcherConstrains::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SketcherGui__TaskSketcherConstrains))
        return static_cast<void*>(const_cast< TaskSketcherConstrains*>(this));
    if (!strcmp(_clname, "Gui::SelectionObserver"))
        return static_cast< Gui::SelectionObserver*>(const_cast< TaskSketcherConstrains*>(this));
    typedef Gui::TaskView::TaskBox QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int SketcherGui::TaskSketcherConstrains::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::TaskView::TaskBox QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
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
