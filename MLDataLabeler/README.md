# MLDataLabeler

This module is used to label the data for supervised learning. The data is captured from multiple sensors such as color(RGBC), IMU.
The data is read from the serial port and processed into different color space (RGB, XYZ, L\*a\*b\*).

The User interface is written using QT. We have used the QT designer to create the ui layout. 

To convert qt.ui file to python.py file please follow these below instructions.

* Step 1: Go to \Scripts folder in C:\ProgramData\Anaconda3

    example: cd C:\ProgramData\Anaconda3\Scripts

* Step 2: if you not find the pyuic5.exe file then please install PyQT5 using pip.

    example : pip install PyQT5==5.9

* Step 3: Execute the following instruction --> pyuic5.exe -x filename.ui -o ouputfilename.py

    example: pyuic5 "C:\Users\NUCER\Documents\git\WiCoSens\MLDataLabeler\mlDataLabeler_rack_container_box.ui" -o "C:\Users\NUCER\Documents\git\WiCoSens\MLDataLabeler\mlDataLabeler_rack_container_box.py"