/****************************************************************************
** Meta object code from reading C++ file 'TaskSketcherSolverAdvanced.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "TaskSketcherSolverAdvanced.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'TaskSketcherSolverAdvanced.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_SketcherGui__TaskSketcherSolverAdvanced[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      22,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      47,   41,   40,   40, 0x08,
      97,   41,   40,   40, 0x08,
     151,  149,   40,   40, 0x08,
     193,  187,   40,   40, 0x08,
     243,   40,   40,   40, 0x08,
     284,   41,   40,   40, 0x08,
     329,   40,   40,   40, 0x08,
     375,   41,   40,   40, 0x08,
     434,   40,   40,   40, 0x08,
     484,  149,   40,   40, 0x08,
     541,  187,   40,   40, 0x08,
     600,   41,   40,   40, 0x08,
     646,   40,   40,   40, 0x08,
     688,   40,   40,   40, 0x08,
     739,   40,   40,   40, 0x08,
     781,   40,   40,   40, 0x08,
     832,   40,   40,   40, 0x08,
     874,   40,   40,   40, 0x08,
     933,  925,   40,   40, 0x08,
     969,   40,   40,   40, 0x28,
    1001,  925,   40,   40, 0x08,
    1034,   40,   40,   40, 0x28,

       0        // eod
};

static const char qt_meta_stringdata_SketcherGui__TaskSketcherSolverAdvanced[] = {
    "SketcherGui::TaskSketcherSolverAdvanced\0"
    "\0index\0on_comboBoxDefaultSolver_currentIndexChanged(int)\0"
    "on_comboBoxDogLegGaussStep_currentIndexChanged(int)\0"
    "i\0on_spinBoxMaxIter_valueChanged(int)\0"
    "state\0on_checkBoxSketchSizeMultiplier_stateChanged(int)\0"
    "on_lineEditConvergence_editingFinished()\0"
    "on_comboBoxQRMethod_currentIndexChanged(int)\0"
    "on_lineEditQRPivotThreshold_editingFinished()\0"
    "on_comboBoxRedundantDefaultSolver_currentIndexChanged(int)\0"
    "on_lineEditRedundantConvergence_editingFinished()\0"
    "on_spinBoxRedundantSolverMaxIterations_valueChanged(int)\0"
    "on_checkBoxRedundantSketchSizeMultiplier_stateChanged(int)\0"
    "on_comboBoxDebugMode_currentIndexChanged(int)\0"
    "on_lineEditSolverParam1_editingFinished()\0"
    "on_lineEditRedundantSolverParam1_editingFinished()\0"
    "on_lineEditSolverParam2_editingFinished()\0"
    "on_lineEditRedundantSolverParam2_editingFinished()\0"
    "on_lineEditSolverParam3_editingFinished()\0"
    "on_lineEditRedundantSolverParam3_editingFinished()\0"
    "checked\0on_pushButtonDefaults_clicked(bool)\0"
    "on_pushButtonDefaults_clicked()\0"
    "on_pushButtonSolve_clicked(bool)\0"
    "on_pushButtonSolve_clicked()\0"
};

void SketcherGui::TaskSketcherSolverAdvanced::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        TaskSketcherSolverAdvanced *_t = static_cast<TaskSketcherSolverAdvanced *>(_o);
        switch (_id) {
        case 0: _t->on_comboBoxDefaultSolver_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->on_comboBoxDogLegGaussStep_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->on_spinBoxMaxIter_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->on_checkBoxSketchSizeMultiplier_stateChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->on_lineEditConvergence_editingFinished(); break;
        case 5: _t->on_comboBoxQRMethod_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->on_lineEditQRPivotThreshold_editingFinished(); break;
        case 7: _t->on_comboBoxRedundantDefaultSolver_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: _t->on_lineEditRedundantConvergence_editingFinished(); break;
        case 9: _t->on_spinBoxRedundantSolverMaxIterations_valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 10: _t->on_checkBoxRedundantSketchSizeMultiplier_stateChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 11: _t->on_comboBoxDebugMode_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 12: _t->on_lineEditSolverParam1_editingFinished(); break;
        case 13: _t->on_lineEditRedundantSolverParam1_editingFinished(); break;
        case 14: _t->on_lineEditSolverParam2_editingFinished(); break;
        case 15: _t->on_lineEditRedundantSolverParam2_editingFinished(); break;
        case 16: _t->on_lineEditSolverParam3_editingFinished(); break;
        case 17: _t->on_lineEditRedundantSolverParam3_editingFinished(); break;
        case 18: _t->on_pushButtonDefaults_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 19: _t->on_pushButtonDefaults_clicked(); break;
        case 20: _t->on_pushButtonSolve_clicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 21: _t->on_pushButtonSolve_clicked(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData SketcherGui::TaskSketcherSolverAdvanced::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SketcherGui::TaskSketcherSolverAdvanced::staticMetaObject = {
    { &Gui::TaskView::TaskBox::staticMetaObject, qt_meta_stringdata_SketcherGui__TaskSketcherSolverAdvanced,
      qt_meta_data_SketcherGui__TaskSketcherSolverAdvanced, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SketcherGui::TaskSketcherSolverAdvanced::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SketcherGui::TaskSketcherSolverAdvanced::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SketcherGui::TaskSketcherSolverAdvanced::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SketcherGui__TaskSketcherSolverAdvanced))
        return static_cast<void*>(const_cast< TaskSketcherSolverAdvanced*>(this));
    typedef Gui::TaskView::TaskBox QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int SketcherGui::TaskSketcherSolverAdvanced::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef Gui::TaskView::TaskBox QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 22)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 22;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
