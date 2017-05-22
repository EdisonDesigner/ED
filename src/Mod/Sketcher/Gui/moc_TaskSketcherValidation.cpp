/****************************************************************************
** Meta object code from reading C++ file 'TaskSketcherValidation.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "TaskSketcherValidation.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TaskSketcherValidation.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_SketcherGui__SketcherValidation[] = {

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
      33,   32,   32,   32, 0x08,
      57,   32,   32,   32, 0x08,
      80,   32,   32,   32, 0x08,
     108,   32,   32,   32, 0x08,
     135,   32,   32,   32, 0x08,
     161,   32,   32,   32, 0x08,
     187,   32,   32,   32, 0x08,
     217,   32,   32,   32, 0x08,
     248,   32,   32,   32, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_SketcherGui__SketcherValidation[] = {
    "SketcherGui::SketcherValidation\0\0"
    "on_findButton_clicked()\0on_fixButton_clicked()\0"
    "on_findConstraint_clicked()\0"
    "on_fixConstraint_clicked()\0"
    "on_findReversed_clicked()\0"
    "on_swapReversed_clicked()\0"
    "on_orientLockEnable_clicked()\0"
    "on_orientLockDisable_clicked()\0"
    "on_delConstrExtr_clicked()\0"
};

void SketcherGui::SketcherValidation::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        SketcherValidation *_t = static_cast<SketcherValidation *>(_o);
        switch (_id) {
        case 0: _t->on_findButton_clicked(); break;
        case 1: _t->on_fixButton_clicked(); break;
        case 2: _t->on_findConstraint_clicked(); break;
        case 3: _t->on_fixConstraint_clicked(); break;
        case 4: _t->on_findReversed_clicked(); break;
        case 5: _t->on_swapReversed_clicked(); break;
        case 6: _t->on_orientLockEnable_clicked(); break;
        case 7: _t->on_orientLockDisable_clicked(); break;
        case 8: _t->on_delConstrExtr_clicked(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData SketcherGui::SketcherValidation::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SketcherGui::SketcherValidation::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_SketcherGui__SketcherValidation,
      qt_meta_data_SketcherGui__SketcherValidation, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SketcherGui::SketcherValidation::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SketcherGui::SketcherValidation::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SketcherGui::SketcherValidation::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SketcherGui__SketcherValidation))
        return static_cast<void*>(const_cast< SketcherValidation*>(this));
    return QWidget::qt_metacast(_clname);
}

int SketcherGui::SketcherValidation::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    return _id;
}
static const uint qt_meta_data_SketcherGui__TaskSketcherValidation[] = {

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

static const char qt_meta_stringdata_SketcherGui__TaskSketcherValidation[] = {
    "SketcherGui::TaskSketcherValidation\0"
};

void SketcherGui::TaskSketcherValidation::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData SketcherGui::TaskSketcherValidation::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SketcherGui::TaskSketcherValidation::staticMetaObject = {
    { &Gui::TaskView::TaskDialog::staticMetaObject, qt_meta_stringdata_SketcherGui__TaskSketcherValidation,
      qt_meta_data_SketcherGui__TaskSketcherValidation, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SketcherGui::TaskSketcherValidation::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SketcherGui::TaskSketcherValidation::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SketcherGui::TaskSketcherValidation::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SketcherGui__TaskSketcherValidation))
        return static_cast<void*>(const_cast< TaskSketcherValidation*>(this));
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int SketcherGui::TaskSketcherValidation::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::TaskView::TaskDialog QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
QT_END_MOC_NAMESPACE
