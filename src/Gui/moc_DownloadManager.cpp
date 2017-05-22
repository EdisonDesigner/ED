/****************************************************************************
** Meta object code from reading C++ file 'DownloadManager.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "DownloadManager.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DownloadManager.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_Gui__Dialog__DownloadManager[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   14, // methods
       1,   64, // properties
       1,   67, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      54,   30,   29,   29, 0x0a,
      93,   85,   29,   29, 0x2a,
     139,  119,   29,   29, 0x0a,
     163,  159,   29,   29, 0x2a,
     200,  178,   29,   29, 0x0a,
     252,  246,   29,   29, 0x2a,
     293,   29,   29,   29, 0x0a,
     303,   29,   29,   29, 0x08,
     310,   29,   29,   29, 0x08,
     322,  246,   29,   29, 0x08,

 // properties: name, type, flags
     365,  352, 0x0009510b,

 // enums: name, flags, count, data
     352, 0x0,    3,   71,

 // enum data: key, value
     378, uint(Gui::Dialog::DownloadManager::Never),
     384, uint(Gui::Dialog::DownloadManager::Exit),
     389, uint(Gui::Dialog::DownloadManager::SuccessFullDownload),

       0        // eod
};

static const char qt_meta_stringdata_Gui__Dialog__DownloadManager[] = {
    "Gui::Dialog::DownloadManager\0\0"
    "request,requestFileName\0"
    "download(QNetworkRequest,bool)\0request\0"
    "download(QNetworkRequest)\0url,requestFileName\0"
    "download(QUrl,bool)\0url\0download(QUrl)\0"
    "reply,requestFileName\0"
    "handleUnsupportedContent(QNetworkReply*,bool)\0"
    "reply\0handleUnsupportedContent(QNetworkReply*)\0"
    "cleanup()\0save()\0updateRow()\0"
    "replyFinished(QNetworkReply*)\0"
    "RemovePolicy\0removePolicy\0Never\0Exit\0"
    "SuccessFullDownload\0"
};

void Gui::Dialog::DownloadManager::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DownloadManager *_t = static_cast<DownloadManager *>(_o);
        switch (_id) {
        case 0: _t->download((*reinterpret_cast< const QNetworkRequest(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 1: _t->download((*reinterpret_cast< const QNetworkRequest(*)>(_a[1]))); break;
        case 2: _t->download((*reinterpret_cast< const QUrl(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 3: _t->download((*reinterpret_cast< const QUrl(*)>(_a[1]))); break;
        case 4: _t->handleUnsupportedContent((*reinterpret_cast< QNetworkReply*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 5: _t->handleUnsupportedContent((*reinterpret_cast< QNetworkReply*(*)>(_a[1]))); break;
        case 6: _t->cleanup(); break;
        case 7: _t->save(); break;
        case 8: _t->updateRow(); break;
        case 9: _t->replyFinished((*reinterpret_cast< QNetworkReply*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData Gui::Dialog::DownloadManager::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::DownloadManager::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_Gui__Dialog__DownloadManager,
      qt_meta_data_Gui__Dialog__DownloadManager, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::DownloadManager::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::DownloadManager::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::DownloadManager::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__DownloadManager))
        return static_cast<void*>(const_cast< DownloadManager*>(this));
    return QDialog::qt_metacast(_clname);
}

int Gui::Dialog::DownloadManager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
#ifndef QT_NO_PROPERTIES
      else if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< RemovePolicy*>(_v) = removePolicy(); break;
        }
        _id -= 1;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setRemovePolicy(*reinterpret_cast< RemovePolicy*>(_v)); break;
        }
        _id -= 1;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 1;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 1;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 1;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 1;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 1;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 1;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}
static const uint qt_meta_data_Gui__Dialog__DownloadModel[] = {

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

static const char qt_meta_stringdata_Gui__Dialog__DownloadModel[] = {
    "Gui::Dialog::DownloadModel\0"
};

void Gui::Dialog::DownloadModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData Gui::Dialog::DownloadModel::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject Gui::Dialog::DownloadModel::staticMetaObject = {
    { &QAbstractListModel::staticMetaObject, qt_meta_stringdata_Gui__Dialog__DownloadModel,
      qt_meta_data_Gui__Dialog__DownloadModel, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &Gui::Dialog::DownloadModel::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *Gui::Dialog::DownloadModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *Gui::Dialog::DownloadModel::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_Gui__Dialog__DownloadModel))
        return static_cast<void*>(const_cast< DownloadModel*>(this));
    return QAbstractListModel::qt_metacast(_clname);
}

int Gui::Dialog::DownloadModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractListModel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
QT_END_MOC_NAMESPACE

