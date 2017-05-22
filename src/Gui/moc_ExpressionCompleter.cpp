/****************************************************************************
** Meta object code from reading C++ file 'ExpressionCompleter.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "ExpressionCompleter.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'ExpressionCompleter.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__ExpressionCompleter[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      33,   26,   25,   25, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_Gui__ExpressionCompleter[] = {
    "Gui::ExpressionCompleter\0\0prefix\0"
    "slotUpdate(QString)\0"
};

void Gui::ExpressionCompleter::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ExpressionCompleter *_t = static_cast<ExpressionCompleter *>(_o);
        switch (_id) {
        case 0: _t->slotUpdate((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::ExpressionCompleter::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::ExpressionCompleter::staticMetaObject = {
    { &QCompleter::staticMetaObject, qt_meta_stringdata_Gui__ExpressionCompleter,
      qt_meta_data_Gui__ExpressionCompleter, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::ExpressionCompleter::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::ExpressionCompleter::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::ExpressionCompleter::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__ExpressionCompleter))
        return static_cast<void*>(const_cast< ExpressionCompleter*>(this));
    return QCompleter::qt_metacast(_clname);
}

int Gui::ExpressionCompleter::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QCompleter::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
static const uint qt_meta_data_Gui__ExpressionLineEdit[] = {

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
      30,   25,   24,   24, 0x05,

 // slots: signature, parameters, type, tag, flags
      52,   25,   24,   24, 0x0a,
      94,   77,   24,   24, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_Gui__ExpressionLineEdit[] = {
    "Gui::ExpressionLineEdit\0\0text\0"
    "textChanged2(QString)\0slotTextChanged(QString)\0"
    "completionPrefix\0slotCompleteText(QString)\0"
};

void Gui::ExpressionLineEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ExpressionLineEdit *_t = static_cast<ExpressionLineEdit *>(_o);
        switch (_id) {
        case 0: _t->textChanged2((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 1: _t->slotTextChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 2: _t->slotCompleteText((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::ExpressionLineEdit::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::ExpressionLineEdit::staticMetaObject = {
    { &QLineEdit::staticMetaObject, qt_meta_stringdata_Gui__ExpressionLineEdit,
      qt_meta_data_Gui__ExpressionLineEdit, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::ExpressionLineEdit::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::ExpressionLineEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::ExpressionLineEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__ExpressionLineEdit))
        return static_cast<void*>(const_cast< ExpressionLineEdit*>(this));
    return QLineEdit::qt_metacast(_clname);
}

int Gui::ExpressionLineEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QLineEdit::qt_metacall(_c, _id, _a);
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
void Gui::ExpressionLineEdit::textChanged2(QString _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_END_MOC_NAMESPACE

