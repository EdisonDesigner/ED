/****************************************************************************
** Meta object code from reading C++ file 'DownloadItem.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "DownloadItem.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DownloadItem.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_EditTableView[] = {

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
      15,   14,   14,   14, 0x0a,
      27,   14,   14,   14, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_EditTableView[] = {
    "EditTableView\0\0removeOne()\0removeAll()\0"
};

void EditTableView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        EditTableView *_t = static_cast<EditTableView *>(_o);
        switch (_id) {
        case 0: _t->removeOne(); break;
        case 1: _t->removeAll(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData EditTableView::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject EditTableView::staticMetaObject = {
    { &QTableView::staticMetaObject, qt_meta_stringdata_EditTableView,
      qt_meta_data_EditTableView, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &EditTableView::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *EditTableView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *EditTableView::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_EditTableView))
        return static_cast<void*>(const_cast< EditTableView*>(this));
    return QTableView::qt_metacast(_clname);
}

int EditTableView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QTableView::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
static const uint qt_meta_data_SqueezeLabel[] = {

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

static const char qt_meta_stringdata_SqueezeLabel[] = {
    "SqueezeLabel\0"
};

void SqueezeLabel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData SqueezeLabel::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject SqueezeLabel::staticMetaObject = {
    { &QLabel::staticMetaObject, qt_meta_stringdata_SqueezeLabel,
      qt_meta_data_SqueezeLabel, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &SqueezeLabel::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *SqueezeLabel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *SqueezeLabel::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_SqueezeLabel))
        return static_cast<void*>(const_cast< SqueezeLabel*>(this));
    return QLabel::qt_metacast(_clname);
}

int SqueezeLabel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QLabel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
static const uint qt_meta_data_AutoSaver[] = {

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
      11,   10,   10,   10, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_AutoSaver[] = {
    "AutoSaver\0\0changeOccurred()\0"
};

void AutoSaver::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        AutoSaver *_t = static_cast<AutoSaver *>(_o);
        switch (_id) {
        case 0: _t->changeOccurred(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData AutoSaver::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject AutoSaver::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_AutoSaver,
      qt_meta_data_AutoSaver, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &AutoSaver::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *AutoSaver::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *AutoSaver::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_AutoSaver))
        return static_cast<void*>(const_cast< AutoSaver*>(this));
    return QObject::qt_metacast(_clname);
}

int AutoSaver::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
static const uint qt_meta_data_NetworkAccessManager[] = {

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
      33,   22,   21,   21, 0x08,
      99,   88,   21,   21, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_NetworkAccessManager[] = {
    "NetworkAccessManager\0\0reply,auth\0"
    "authenticationRequired(QNetworkReply*,QAuthenticator*)\0"
    "proxy,auth\0"
    "proxyAuthenticationRequired(QNetworkProxy,QAuthenticator*)\0"
};

void NetworkAccessManager::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        NetworkAccessManager *_t = static_cast<NetworkAccessManager *>(_o);
        switch (_id) {
        case 0: _t->authenticationRequired((*reinterpret_cast< QNetworkReply*(*)>(_a[1])),(*reinterpret_cast< QAuthenticator*(*)>(_a[2]))); break;
        case 1: _t->proxyAuthenticationRequired((*reinterpret_cast< const QNetworkProxy(*)>(_a[1])),(*reinterpret_cast< QAuthenticator*(*)>(_a[2]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData NetworkAccessManager::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject NetworkAccessManager::staticMetaObject = {
    { &QNetworkAccessManager::staticMetaObject, qt_meta_stringdata_NetworkAccessManager,
      qt_meta_data_NetworkAccessManager, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &NetworkAccessManager::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *NetworkAccessManager::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *NetworkAccessManager::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_NetworkAccessManager))
        return static_cast<void*>(const_cast< NetworkAccessManager*>(this));
    return QNetworkAccessManager::qt_metacast(_clname);
}

int NetworkAccessManager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QNetworkAccessManager::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
static const uint qt_meta_data_Gui__Dialog__DownloadItem[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      27,   26,   26,   26, 0x05,

 // slots: signature, parameters, type, tag, flags
      43,   26,   26,   26, 0x08,
      50,   26,   26,   26, 0x08,
      61,   26,   26,   26, 0x08,
      68,   26,   26,   26, 0x08,
      81,   26,   26,   26, 0x08,
     106,  101,   26,   26, 0x08,
     166,  141,   26,   26, 0x08,
     198,   26,   26,   26, 0x08,
     216,   26,   26,   26, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_Gui__Dialog__DownloadItem[] = {
    "Gui::Dialog::DownloadItem\0\0statusChanged()\0"
    "stop()\0tryAgain()\0open()\0openFolder()\0"
    "downloadReadyRead()\0code\0"
    "error(QNetworkReply::NetworkError)\0"
    "bytesReceived,bytesTotal\0"
    "downloadProgress(qint64,qint64)\0"
    "metaDataChanged()\0finished()\0"
};

void Gui::Dialog::DownloadItem::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DownloadItem *_t = static_cast<DownloadItem *>(_o);
        switch (_id) {
        case 0: _t->statusChanged(); break;
        case 1: _t->stop(); break;
        case 2: _t->tryAgain(); break;
        case 3: _t->open(); break;
        case 4: _t->openFolder(); break;
        case 5: _t->downloadReadyRead(); break;
        case 6: _t->error((*reinterpret_cast< QNetworkReply::NetworkError(*)>(_a[1]))); break;
        case 7: _t->downloadProgress((*reinterpret_cast< qint64(*)>(_a[1])),(*reinterpret_cast< qint64(*)>(_a[2]))); break;
        case 8: _t->metaDataChanged(); break;
        case 9: _t->finished(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::Dialog::DownloadItem::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::DownloadItem::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_Gui__Dialog__DownloadItem,
      qt_meta_data_Gui__Dialog__DownloadItem, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::DownloadItem::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::DownloadItem::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::DownloadItem::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__DownloadItem))
        return static_cast<void*>(const_cast< DownloadItem*>(this));
    if (!strcmp(_clname, "Ui_DownloadItem"))
        return static_cast< Ui_DownloadItem*>(const_cast< DownloadItem*>(this));
    return QWidget::qt_metacast(_clname);
}

int Gui::Dialog::DownloadItem::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
    return _id;
}

// SIGNAL 0
void Gui::Dialog::DownloadItem::statusChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE

