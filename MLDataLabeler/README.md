# MLDataLabeler

This module is used to label the data for supervised learning. The data is captured from multiple sensors such as color(RGBC), IMU.
The data is read from the serial port and processed into different color space (RGB, XYZ, L\*a\*b\*).

The User interface is written using QT. We have used the QT designer to create the ui layout. 

To convert qt.ui file to python.py file please follow these below instructions.

* Step 1: Go to \Scripts folder in C:\ProgramData\Anaconda3

    example: cd C:\ProgramData\Anaconda3\Scripts

* Step 2: Execute the following instruction --> pyuic5.exe -x filename.ui -o ouputfilename.py

    example: pyuic5.exe -x "C:\Users\HackoMan\Google Drive\MasterThesis\Code\QtDesigner\Lable_Data.ui" -o "C:\Users\HackoMan\Google Drive\MasterThesis\Code\QtDesigner\Lable_Data.py"