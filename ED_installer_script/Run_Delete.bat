@echo off

del Addons.7z
del bin.7z
del data.7z
del doc.7z
del Ext.7z
del lib.7z
del Mod.7z

echo y | rmdir /s Addons
echo y | rmdir /s bin
echo y | rmdir /s data
echo y | rmdir /s doc
echo y | rmdir /s Ext
echo y | rmdir /s lib
echo y | rmdir /s Mod
