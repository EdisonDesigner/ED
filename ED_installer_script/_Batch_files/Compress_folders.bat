@echo off

:: Compress bin folder
bandizip c bin.7z bin

:: Compress Addons folder
bandizip c Addons.7z Addons

:: Compress data folder
bandizip c data.7z data

:: Compress doc folder
bandizip c doc.7z doc

:: Compress Ext folder
bandizip c Ext.7z Ext

:: Compress lib folder
bandizip c lib.7z lib

:: Compress Mod folder
bandizip c Mod.7z Mod
