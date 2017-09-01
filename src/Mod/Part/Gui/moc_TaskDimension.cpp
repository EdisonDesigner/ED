/****************************************************************************
** Meta object code from reading C++ file 'TaskDimension.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "TaskDimension.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TaskDimension.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_PartGui__SteppedSelection[] = {

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
      35,   27,   26,   26, 0x08,
      55,   26,   26,   26, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_PartGui__SteppedSelection[] = {
    "PartGui::SteppedSelection\0\0checked\0"
    "selectionSlot(bool)\0buildPixmaps()\0"
};

void PartGui::SteppedSelection::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        SteppedSelection *_t = static_cast<SteppedSelection *>(_o);
        switch (_id) {
        case 0: _t->selectionSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->buildPixmaps(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData PartGui::SteppedSelection::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PartGui::SteppedSelection::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_PartGui__SteppedSelection,
      qt_meta_data_PartGui__SteppedSelection, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PartGui::SteppedSelection::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PartGui::SteppedSelection::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PartGui::SteppedSelection::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PartGui__SteppedSelection))
        return static_cast<void*>(const_cast< SteppedSelection*>(this));
    return QWidget::qt_metacast(_clname);
}

int PartGui::SteppedSelection::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
static const uint qt_meta_data_PartGui__DimensionControl[] = {

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
      27,   26,   26,   26, 0x0a,
      46,   26,   26,   26, 0x0a,
      68,   26,   26,   26, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_PartGui__DimensionControl[] = {
    "PartGui::DimensionControl\0\0"
    "toggle3dSlot(bool)\0toggleDeltaSlot(bool)\0"
    "clearAllSlot(bool)\0"
};

void PartGui::DimensionControl::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DimensionControl *_t = static_cast<DimensionControl *>(_o);
        switch (_id) {
        case 0: _t->toggle3dSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->toggleDeltaSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->clearAllSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData PartGui::DimensionControl::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PartGui::DimensionControl::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_PartGui__DimensionControl,
      qt_meta_data_PartGui__DimensionControl, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PartGui::DimensionControl::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PartGui::DimensionControl::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PartGui::DimensionControl::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PartGui__DimensionControl))
        return static_cast<void*>(const_cast< DimensionControl*>(this));
    return QWidget::qt_metacast(_clname);
}

int PartGui::DimensionControl::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}
static const uint qt_meta_data_PartGui__TaskMeasureLinear[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       7,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      36,   28,   27,   27, 0x09,
      57,   28,   27,   27, 0x09,
      78,   27,   27,   27, 0x09,
     100,   27,   27,   27, 0x09,
     119,   27,   27,   27, 0x09,
     141,   27,   27,   27, 0x09,
     160,   27,   27,   27, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_PartGui__TaskMeasureLinear[] = {
    "PartGui::TaskMeasureLinear\0\0checked\0"
    "selection1Slot(bool)\0selection2Slot(bool)\0"
    "resetDialogSlot(bool)\0toggle3dSlot(bool)\0"
    "toggleDeltaSlot(bool)\0clearAllSlot(bool)\0"
    "selectionClearDelayedSlot()\0"
};

void PartGui::TaskMeasureLinear::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        TaskMeasureLinear *_t = static_cast<TaskMeasureLinear *>(_o);
        switch (_id) {
        case 0: _t->selection1Slot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->selection2Slot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->resetDialogSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->toggle3dSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->toggleDeltaSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->clearAllSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->selectionClearDelayedSlot(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData PartGui::TaskMeasureLinear::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PartGui::TaskMeasureLinear::staticMetaObject = {
    { &Gui::TaskView::TaskDialog::staticMetaObject, qt_meta_stringdata_PartGui__TaskMeasureLinear,
      qt_meta_data_PartGui__TaskMeasureLinear, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PartGui::TaskMeasureLinear::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PartGui::TaskMeasureLinear::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PartGui::TaskMeasureLinear::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PartGui__TaskMeasureLinear))
        return static_cast<void*>(const_cast< TaskMeasureLinear*>(this));
    if (!strcmp(_clname, "Gui::SelectionObserver"))
        return static_cast< Gui::SelectionObserver*>(const_cast< TaskMeasureLinear*>(this));
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int PartGui::TaskMeasureLinear::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    }
    return _id;
}
static const uint qt_meta_data_PartGui__TaskMeasureAngular[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       7,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      37,   29,   28,   28, 0x09,
      58,   29,   28,   28, 0x09,
      79,   28,   28,   28, 0x09,
     101,   28,   28,   28, 0x09,
     120,   28,   28,   28, 0x09,
     142,   28,   28,   28, 0x09,
     161,   28,   28,   28, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_PartGui__TaskMeasureAngular[] = {
    "PartGui::TaskMeasureAngular\0\0checked\0"
    "selection1Slot(bool)\0selection2Slot(bool)\0"
    "resetDialogSlot(bool)\0toggle3dSlot(bool)\0"
    "toggleDeltaSlot(bool)\0clearAllSlot(bool)\0"
    "selectionClearDelayedSlot()\0"
};

void PartGui::TaskMeasureAngular::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        TaskMeasureAngular *_t = static_cast<TaskMeasureAngular *>(_o);
        switch (_id) {
        case 0: _t->selection1Slot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->selection2Slot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->resetDialogSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->toggle3dSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->toggleDeltaSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->clearAllSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->selectionClearDelayedSlot(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData PartGui::TaskMeasureAngular::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PartGui::TaskMeasureAngular::staticMetaObject = {
    { &Gui::TaskView::TaskDialog::staticMetaObject, qt_meta_stringdata_PartGui__TaskMeasureAngular,
      qt_meta_data_PartGui__TaskMeasureAngular, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PartGui::TaskMeasureAngular::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PartGui::TaskMeasureAngular::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PartGui::TaskMeasureAngular::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PartGui__TaskMeasureAngular))
        return static_cast<void*>(const_cast< TaskMeasureAngular*>(this));
    if (!strcmp(_clname, "Gui::SelectionObserver"))
        return static_cast< Gui::SelectionObserver*>(const_cast< TaskMeasureAngular*>(this));
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int PartGui::TaskMeasureAngular::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
