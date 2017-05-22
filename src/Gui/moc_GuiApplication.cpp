/****************************************************************************
** Meta object code from reading C++ file 'GuiApplication.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "GuiApplication.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'GuiApplication.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__GUIApplication[] = {

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

static const char qt_meta_stringdata_Gui__GUIApplication[] = {
    "Gui::GUIApplication\0"
};

void Gui::GUIApplication::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::GUIApplication::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::GUIApplication::staticMetaObject = {
    { &GUIApplicationNativeEventAware::staticMetaObject, qt_meta_stringdata_Gui__GUIApplication,
      qt_meta_data_Gui__GUIApplication, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::GUIApplication::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::GUIApplication::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::GUIApplication::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__GUIApplication))
        return static_cast<void*>(const_cast< GUIApplication*>(this));
    return GUIApplicationNativeEventAware::qt_metacast(_clname);
}

int Gui::GUIApplication::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = GUIApplicationNativeEventAware::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
static const uint qt_meta_data_Gui__GUISingleApplication[] = {

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
      27,   26,   26,   26, 0x05,

 // slots: signature, parameters, type, tag, flags
      62,   26,   26,   26, 0x08,
      82,   26,   26,   26, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__GUISingleApplication[] = {
    "Gui::GUISingleApplication\0\0"
    "messageReceived(QList<QByteArray>)\0"
    "receiveConnection()\0processMessages()\0"
};

void Gui::GUISingleApplication::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        GUISingleApplication *_t = static_cast<GUISingleApplication *>(_o);
        switch (_id) {
        case 0: _t->messageReceived((*reinterpret_cast< const QList<QByteArray>(*)>(_a[1]))); break;
        case 1: _t->receiveConnection(); break;
        case 2: _t->processMessages(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::GUISingleApplication::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::GUISingleApplication::staticMetaObject = {
    { &GUIApplication::staticMetaObject, qt_meta_stringdata_Gui__GUISingleApplication,
      qt_meta_data_Gui__GUISingleApplication, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::GUISingleApplication::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::GUISingleApplication::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::GUISingleApplication::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__GUISingleApplication))
        return static_cast<void*>(const_cast< GUISingleApplication*>(this));
    return GUIApplication::qt_metacast(_clname);
}

int Gui::GUISingleApplication::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = GUIApplication::qt_metacall(_c, _id, _a);
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
void Gui::GUISingleApplication::messageReceived(const QList<QByteArray> & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_END_MOC_NAMESPACE

