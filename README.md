
*** note ***:
 install requirements.txt aforehand before deploying to your own machine
 (compulsory:
    kivy[full] package
    Kivy-Garden==0.1.5 v
    opencv-python
    pyinstaller
    kivy_deps: sdl2, glew should be considered too
  ) 

1) build Graphic Interface with PySimpleGUI: 
 https://habr.com/ru/company/edison/blog/480884/ - russian source (avoided, forgotten) ☒

2) build GRaphic Interface with Kiwy:
https://www.youtube.com/watch?v=WkGFqxHoOfI - ☑

3)pyinstaller route win:
E:\SoftServeItAcademy\airport_petty_algorithms\carrier_register_li - ☑

4)create standlaone executable файл .exe for windows 

4) config setup instruction - ☑:
    1. implement imports
        --> from kivy.config import Config
        --> from configparser import ConfigParser
    1. open python shell, setup kivy config.ini file root
        --> import os
        --> os.environ['KIVY_HOME'] = os.getcwd()
    2. once config.ini file created configure app settings
        instantiate
        --> config = ConfigParser()
        
        parse existing file
        config.read('config.ini')

        read values from a section
        resizable_val = config.get('graphics', 'resizable')
        
        Config.set('graphics', 'resizable', resizable_val)
        --> Config.write()

Fixed: current date report (https://stackoverflow.com/questions/47343643/i-am-using-the-openpyxl-library-on-python-on-a-windows-10-computer-and-trying-to)
• added roots ito current dir
• adder dir to untrusted mode
• added PATH в Python Scripts: 
  SETX PATH "%PATH%;C:\Users\vbalashov\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts" 

