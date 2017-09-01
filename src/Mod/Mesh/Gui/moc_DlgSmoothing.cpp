/****************************************************************************
** Meta object code from reading C++ file 'DlgSmoothing.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "DlgSmoothing.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DlgSmoothing.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_MeshGui__DlgSmoothing[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      23,   22,   22,   22, 0x05,

 // slots: signature, parameters, type, tag, flags
      46,   22,   22,   22, 0x08,
      66,   22,   22,   22, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_MeshGui__DlgSmoothing[] = {
    "MeshGui::DlgSmoothing\0\0toggledSelection(bool)\0"
    "method_clicked(int)\0"
    "on_checkBoxSelection_toggled(bool)\0"
};

void MeshGui::DlgSmoothing::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DlgSmoothing *_t = static_cast<DlgSmoothing *>(_o);
        switch (_id) {
        case 0: _t->toggledSelection((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->method_clicked((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->on_checkBoxSelection_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData MeshGui::DlgSmoothing::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject MeshGui::DlgSmoothing::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_MeshGui__DlgSmoothing,
      qt_meta_data_MeshGui__DlgSmoothing, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &MeshGui::DlgSmoothing::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *MeshGui::DlgSmoothing::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *MeshGui::DlgSmoothing::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_MeshGui__DlgSmoothing))
        return static_cast<void*>(const_cast< DlgSmoothing*>(this));
    return QWidget::qt_metacast(_clname);
}

int MeshGui::DlgSmoothing::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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

// SIGNAL 0
void MeshGui::DlgSmoothing::toggledSelection(bool _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
static const uint qt_meta_data_MeshGui__SmoothingDialog[] = {

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

static const char qt_meta_stringdata_MeshGui__SmoothingDialog[] = {
    "MeshGui::SmoothingDialog\0"
};

void MeshGui::SmoothingDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData MeshGui::SmoothingDialog::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject MeshGui::SmoothingDialog::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_MeshGui__SmoothingDialog,
      qt_meta_data_MeshGui__SmoothingDialog, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &MeshGui::SmoothingDialog::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *MeshGui::SmoothingDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *MeshGui::SmoothingDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_MeshGui__SmoothingDialog))
        return static_cast<void*>(const_cast< SmoothingDialog*>(this));
    return QDialog::qt_metacast(_clname);
}

int MeshGui::SmoothingDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
static const uint qt_meta_data_MeshGui__TaskSmoothing[] = {

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

static const char qt_meta_stringdata_MeshGui__TaskSmoothing[] = {
    "MeshGui::TaskSmoothing\0"
};

void MeshGui::TaskSmoothing::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData MeshGui::TaskSmoothing::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject MeshGui::TaskSmoothing::staticMetaObject = {
    { &Gui::TaskView::TaskDialog::staticMetaObject, qt_meta_stringdata_MeshGui__TaskSmoothing,
      qt_meta_data_MeshGui__TaskSmoothing, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &MeshGui::TaskSmoothing::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *MeshGui::TaskSmoothing::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *MeshGui::TaskSmoothing::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_MeshGui__TaskSmoothing))
        return static_cast<void*>(const_cast< TaskSmoothing*>(this));
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int MeshGui::TaskSmoothing::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
QT_END_MOC_NAMESPACE
