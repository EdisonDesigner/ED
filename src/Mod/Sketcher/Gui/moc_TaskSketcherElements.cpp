/****************************************************************************
** Meta object code from reading C++ file 'TaskSketcherElements.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "TaskSketcherElements.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TaskSketcherElements.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_SketcherGui__ElementView[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      25,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      26,   25,   25,   25, 0x05,
      52,   25,   25,   25, 0x05,

 // slots: signature, parameters, type, tag, flags
      71,   25,   25,   25, 0x09,
      93,   25,   25,   25, 0x09,
     116,   25,   25,   25, 0x09,
     137,   25,   25,   25, 0x09,
     162,   25,   25,   25, 0x09,
     185,   25,   25,   25, 0x09,
     204,   25,   25,   25, 0x09,
     225,   25,   25,   25, 0x09,
     248,   25,   25,   25, 0x09,
     276,   25,   25,   25, 0x09,
     297,   25,   25,   25, 0x09,
     318,   25,   25,   25, 0x09,
     338,   25,   25,   25, 0x09,
     358,   25,   25,   25, 0x09,
     386,   25,   25,   25, 0x09,
     409,   25,   25,   25, 0x09,
     431,   25,   25,   25, 0x09,
     454,   25,   25,   25, 0x09,
     469,   25,   25,   25, 0x09,
     481,   25,   25,   25, 0x09,
     498,   25,   25,   25, 0x09,
     514,   25,   25,   25, 0x09,
     530,   25,   25,   25, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_SketcherGui__ElementView[] = {
    "SketcherGui::ElementView\0\0"
    "onFilterShortcutPressed()\0signalCloseShape()\0"
    "deleteSelectedItems()\0doHorizontalDistance()\0"
    "doVerticalDistance()\0doHorizontalConstraint()\0"
    "doVerticalConstraint()\0doLockConstraint()\0"
    "doPointCoincidence()\0doParallelConstraint()\0"
    "doPerpendicularConstraint()\0"
    "doLengthConstraint()\0doRadiusConstraint()\0"
    "doAngleConstraint()\0doEqualConstraint()\0"
    "doPointOnObjectConstraint()\0"
    "doSymetricConstraint()\0doTangentConstraint()\0"
    "doToggleConstruction()\0doCloseShape()\0"
    "doConnect()\0doSelectOrigin()\0"
    "doSelectHAxis()\0doSelectVAxis()\0"
    "doSelectConstraints()\0"
};

void SketcherGui::ElementView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ElementView *_t = static_cast<ElementView *>(_o);
        switch (_id) {
        case 0: _t->onFilterShortcutPressed(); break;
        case 1: _t->signalCloseShape(); break;
        case 2: _t->deleteSelectedItems(); break;
        case 3: _t->doHorizontalDistance(); break;
        case 4: _t->doVerticalDistance(); break;
        case 5: _t->doHorizontalConstraint(); break;
        case 6: _t->doVerticalConstraint(); break;
        case 7: _t->doLockConstraint(); break;
        case 8: _t->doPointCoincidence(); break;
        case 9: _t->doParallelConstraint(); break;
        case 10: _t->doPerpendicularConstraint(); break;
        case 11: _t->doLengthConstraint(); break;
        case 12: _t->doRadiusConstraint(); break;
        case 13: _t->doAngleConstraint(); break;
        case 14: _t->doEqualConstraint(); break;
        case 15: _t->doPointOnObjectConstraint(); break;
        case 16: _t->doSymetricConstraint(); break;
        case 17: _t->doTangentConstraint(); break;
        case 18: _t->doToggleConstruction(); break;
        case 19: _t->doCloseShape(); break;
        case 20: _t->doConnect(); break;
        case 21: _t->doSelectOrigin(); break;
        case 22: _t->doSelectHAxis(); break;
        case 23: _t->doSelectVAxis(); break;
        case 24: _t->doSelectConstraints(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData SketcherGui::ElementView::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SketcherGui::ElementView::staticMetaObject = {
    { &QListWidget::staticMetaObject, qt_meta_stringdata_SketcherGui__ElementView,
      qt_meta_data_SketcherGui__ElementView, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SketcherGui::ElementView::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SketcherGui::ElementView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SketcherGui::ElementView::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SketcherGui__ElementView))
        return static_cast<void*>(const_cast< ElementView*>(this));
    return QListWidget::qt_metacast(_clname);
}

int SketcherGui::ElementView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QListWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 25)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 25;
    }
    return _id;
}

// SIGNAL 0
void SketcherGui::ElementView::onFilterShortcutPressed()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}

// SIGNAL 1
void SketcherGui::ElementView::signalCloseShape()
{
    QMetaObject::activate(this, &staticMetaObject, 1, 0);
}
static const uint qt_meta_data_SketcherGui__TaskSketcherElements[] = {

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
      35,   34,   34,   34, 0x0a,
      85,   80,   34,   34, 0x0a,
     137,   34,   34,   34, 0x0a,
     189,  183,   34,   34, 0x0a,
     243,  237,   34,   34, 0x0a,
     274,  237,   34,   34, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_SketcherGui__TaskSketcherElements[] = {
    "SketcherGui::TaskSketcherElements\0\0"
    "on_listWidgetElements_itemSelectionChanged()\0"
    "item\0on_listWidgetElements_itemEntered(QListWidgetItem*)\0"
    "on_listWidgetElements_filterShortcutPressed()\0"
    "index\0on_listWidgetElements_currentFilterChanged(int)\0"
    "state\0on_namingBox_stateChanged(int)\0"
    "on_autoSwitchBox_stateChanged(int)\0"
};

void SketcherGui::TaskSketcherElements::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        TaskSketcherElements *_t = static_cast<TaskSketcherElements *>(_o);
        switch (_id) {
        case 0: _t->on_listWidgetElements_itemSelectionChanged(); break;
        case 1: _t->on_listWidgetElements_itemEntered((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 2: _t->on_listWidgetElements_filterShortcutPressed(); break;
        case 3: _t->on_listWidgetElements_currentFilterChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->on_namingBox_stateChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->on_autoSwitchBox_stateChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData SketcherGui::TaskSketcherElements::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SketcherGui::TaskSketcherElements::staticMetaObject = {
    { &Gui::TaskView::TaskBox::staticMetaObject, qt_meta_stringdata_SketcherGui__TaskSketcherElements,
      qt_meta_data_SketcherGui__TaskSketcherElements, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SketcherGui::TaskSketcherElements::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SketcherGui::TaskSketcherElements::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SketcherGui::TaskSketcherElements::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SketcherGui__TaskSketcherElements))
        return static_cast<void*>(const_cast< TaskSketcherElements*>(this));
    if (!strcmp(_clname, "Gui::SelectionObserver"))
        return static_cast< Gui::SelectionObserver*>(const_cast< TaskSketcherElements*>(this));
    typedef Gui::TaskView::TaskBox QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int SketcherGui::TaskSketcherElements::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
