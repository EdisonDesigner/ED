/****************************************************************************
** Meta object code from reading C++ file 'TaskThickness.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "TaskThickness.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TaskThickness.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_PartGui__ThicknessWidget[] = {

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
      26,   25,   25,   25, 0x08,
      61,   25,   25,   25, 0x08,
      88,   25,   25,   25, 0x08,
     115,   25,   25,   25, 0x08,
     145,   25,   25,   25, 0x08,
     179,   25,   25,   25, 0x08,
     204,   25,   25,   25, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_PartGui__ThicknessWidget[] = {
    "PartGui::ThicknessWidget\0\0"
    "on_spinOffset_valueChanged(double)\0"
    "on_modeType_activated(int)\0"
    "on_joinType_activated(int)\0"
    "on_intersection_toggled(bool)\0"
    "on_selfIntersection_toggled(bool)\0"
    "on_facesButton_clicked()\0"
    "on_updateView_toggled(bool)\0"
};

void PartGui::ThicknessWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ThicknessWidget *_t = static_cast<ThicknessWidget *>(_o);
        switch (_id) {
        case 0: _t->on_spinOffset_valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 1: _t->on_modeType_activated((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->on_joinType_activated((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->on_intersection_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->on_selfIntersection_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->on_facesButton_clicked(); break;
        case 6: _t->on_updateView_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData PartGui::ThicknessWidget::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PartGui::ThicknessWidget::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_PartGui__ThicknessWidget,
      qt_meta_data_PartGui__ThicknessWidget, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PartGui::ThicknessWidget::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PartGui::ThicknessWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PartGui::ThicknessWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PartGui__ThicknessWidget))
        return static_cast<void*>(const_cast< ThicknessWidget*>(this));
    return QWidget::qt_metacast(_clname);
}

int PartGui::ThicknessWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    }
    return _id;
}
static const uint qt_meta_data_PartGui__TaskThickness[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

       0        // eod
};

static const char qt_meta_stringdata_PartGui__TaskThickness[] = {
    "PartGui::TaskThickness\0"
};

void PartGui::TaskThickness::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData PartGui::TaskThickness::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject PartGui::TaskThickness::staticMetaObject = {
    { &Gui::TaskView::TaskDialog::staticMetaObject, qt_meta_stringdata_PartGui__TaskThickness,
      qt_meta_data_PartGui__TaskThickness, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &PartGui::TaskThickness::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *PartGui::TaskThickness::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *PartGui::TaskThickness::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_PartGui__TaskThickness))
        return static_cast<void*>(const_cast< TaskThickness*>(this));
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int PartGui::TaskThickness::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
QT_END_MOC_NAMESPACE
