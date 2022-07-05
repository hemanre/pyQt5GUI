# pyQt5GUI

OS: Windows 

Tool: Command prompt

Command to install pyQt5 On Python >= 3.6:

>> pip install pyqt5

>> pip install pyqt5-tools

UI creation using designer.exe application (Eg. Location: C:\Users\xyz\qt\5.15.2\msvc2019_64\bin)

Command to convert .ui saved from designer.exe to .py format (Eg. dialog.ui to dialog.py):

Navigate to the folder containing pyuic5.exe and execute the following command,

>> pyuic5 -x dialog.ui -o dialog.py