@echo off
set BATCHDIR=%cd%\_Batch_files

call %BATCHDIR%\Copy_Addons_folder.bat
call %BATCHDIR%\Copy_bin_folder.bat
call %BATCHDIR%\Copy_data_folder.bat
call %BATCHDIR%\Copy_doc_folder.bat
call %BATCHDIR%\Copy_Ext_folder.bat
call %BATCHDIR%\Copy_lib_folder.bat
call %BATCHDIR%\Copy_Mod_folder.bat

call %BATCHDIR%\Compress_folders.bat
